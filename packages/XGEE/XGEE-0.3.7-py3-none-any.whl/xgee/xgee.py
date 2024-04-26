import socket
import json
import sys
import pkg_resources
import tornado.ioloop
import tornado.web
from  .eoqserver import PyEoq2WebServer as eoqserver
import signal
import time
import mimetypes # usually imported by tornado, but needed for the mimetypes workaround
import contextlib
from tabulate import tabulate
from functools import partial
from pathlib import Path
from os.path import exists
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import __main__

__version__ = '0.3.7'

DEFAULT_PATH='./'
DEFAULT_HOST=socket.gethostname()
localpath=str(Path().resolve())
FRAMEWORK_RUN_FLAG=True
apps=[]

xgeedir = pkg_resources.resource_filename(__name__, "core")
xgeelayoutmeta = pkg_resources.resource_filename(__name__, "meta/layout.ecore")

# Fix for XGEE Core Issue #1 Set MIME-Type of static files according to file type
# Ignores system settings for .js and .css since they might be wrongly defined, e.g. as text/plain
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

class XGEEConfigHandler(tornado.web.RequestHandler):
    ''' Returns the XGEE configuration as JSON '''
    def initialize(self, xgee_app):
        self.xgee_app=xgee_app
    def get(self):
        xgeeapp_conf='/* Generated XGEE app configuration by XGEE launcher */\n var $XGEE='+str(json.dumps({'app':{'url':self.xgee_app.getWebInstanceUrl()},'eoq':{'url': self.xgee_app.getEoqInstanceUrl()}}))+';'
        self.write(xgeeapp_conf)
    
class EoqConfiguration:
    '''' Default EOQ Configuration '''
    def __init__(self):
        self.ws='/ws/eoq.do'
        self.port=8000
        self.workspaceDir='./workspace'
        self.metaDir='./.meta'
        self.actions=1 # actions are enabled by default
        self.actionsDir='./workspace/actions'
        self.timeout=10.0
        self.backup=0 # backups are disabled by default
        self.backupDir='./backup'
        self.logDir='./log'
        self.logToFile=1 # logging to file is enabled by default
        self.logToConsole=0 # logging to console is disabled by default
        self.autosave=5.0 # the timeout after which autosave is triggered
        self.trackFileChanges=0 # whether tracking of changes on the filesystems is enabled (default:OFF)
        self.maxChanges=10000 # how many changes shall be remembered until the oldest change is forgotten (1 to 1000000)
        self.enableBenchmark=0 # measure time for queries and commands




class XGEEApp:
    def __init__(self, app_path, app_folder_name, app_conf):
        self.app_conf=app_conf
        self.path=app_path
        self.app_folder_name=app_folder_name

        # Prepare Application configuration
        self.name=str(self.get_conf_parameter('app/name'))
        if self.get_conf_parameter('app/name') is None:
            self.name='Unnamed Application'

        self.appHost=str(self.get_conf_parameter('app/host'))
        if self.get_conf_parameter('app/host') is None:
            self.appHost=DEFAULT_HOST       
        self.port=self.get_conf_parameter('app/port')
        self.webInstance=None

        # Prepare EOQ configuration
        self.eoqHost=str(self.get_conf_parameter('eoq/host'))
        if self.get_conf_parameter('eoq/host') is None:
            self.eoqHost=DEFAULT_HOST     
        self.eoqPort=self.get_conf_parameter('eoq/port')
        self.eoqInstance=None
        self.eoqThread=None
        self.eoqConfiguration=None
        if self.eoqPort is not None:
            self.eoqConfiguration=EoqConfiguration()
            self.eoqConfiguration.port=self.eoqPort

            # Configure workspace directory
            if self.get_conf_parameter('eoq/workspace') is not None:
                self.eoqConfiguration.workspaceDir=self.path+str(self.get_conf_parameter('eoq/workspace')).lstrip("./")
            else:
                self.eoqConfiguration.workspaceDir=self.path+'workspace'

            # Configure meta directory
            if self.get_conf_parameter('eoq/meta') is not None:
                self.eoqConfiguration.metaDir=localpath+'/'+self.path+str(self.get_conf_parameter('eoq/meta')).lstrip("./")
            else:
                self.eoqConfiguration.metaDir=localpath+'/'+self.path+'meta'

            # Configure actions directory
            if self.get_conf_parameter('eoq/actions') is not None:
                self.eoqConfiguration.actionsDir=localpath+'/'+self.path+str(self.get_conf_parameter('eoq/actions')).lstrip("./")
            else:
                self.eoqConfiguration.actionsDir=localpath+'/'+self.path+'actions'

            # Configure log directory
            if self.get_conf_parameter('eoq/log') is not None:
                self.eoqConfiguration.logDir=localpath+'/'+self.path+str(self.get_conf_parameter('eoq/log')).lstrip("./")
            else:
                self.eoqConfiguration.logDir=localpath+'/'+self.path+'log'

            # Configure backup directory
            if self.get_conf_parameter('eoq/backup') is not None:
                self.eoqConfiguration.backupDir=localpath+'/'+self.path+str(self.get_conf_parameter('eoq/backup')).lstrip("./")
                self.eoqConfiguration.backup=1 # backups are enabled if a directory was set
            else:
                self.eoqConfiguration.backupDir=localpath+'/'+self.path+'backup'

            # option to log to console
            if self.get_conf_parameter('eoq/consolelog') is not None:
                self.eoqConfiguration.logToConsole=self.get_conf_parameter('eoq/consolelog')

            # Configure autosave
            if self.get_conf_parameter('eoq/autosave') is not None:
                self.eoqConfiguration.autosave=self.get_conf_parameter('eoq/consolelog')

    def getName(self):
        return self.name

    def getPath(self):
        return self.path
    
    def getWebInstanceUrl(self, default='---'):
        ''' Gets the web instance URL '''
        res=default
        if self.webInstance is not None:
            res='http://'+self.appHost+':'+str(self.port)
        return res

    def getEoqInstanceUrl(self,default='---'):
        ''' Gets the eoq instance URL '''
        res=default
        if self.eoqInstance is not None:
            res='ws://'+self.eoqHost+':'+str(self.eoqPort)+'/ws/eoq.do'
        return res

    def launch(self): 
        ''' Launches an XGEE application '''
        webInstance=0
        eoqInstance=0
        if self.port is not None:
            application = tornado.web.Application([
            (r"/xgee-core/(.*)", tornado.web.StaticFileHandler, {"path": str(xgeedir)}),
            (r"/xgee-conf/app.conf.js", XGEEConfigHandler, {"xgee_app":self}),
            (r"/(.*)", tornado.web.StaticFileHandler, {"path": self.path+"/app","default_filename":"index.html"}),
            ])
            self.webInstance=None                           
            self.webInstance = tornado.httpserver.HTTPServer(application)
            self.webInstance.listen(self.port)
            webInstance=1
        else:
            print('App not hosted.')
        if self.eoqPort is not None:
            self.eoqInstance = eoqserver.PyeoqWebSocketServer()
            self.eoqThread=eoqserver.threading.Thread(target=self.eoqInstance.Start, args=(self.eoqConfiguration,))
            self.eoqThread.start()
            while(True):
                if self.eoqInstance.mdbProvider is not None:
                    break
            # Inject meta
            self.eoqInstance.mdbProvider._PyEcoreWorkspaceMdbProvider__LoadMetaModelResource(str(xgeelayoutmeta))
            eoqInstance=1
        else:
            print('EOQ workspace not hosted')
        return webInstance,eoqInstance


    def shutdownWebInstance(self):
        ''' Shuts down the web-instance if applicable'''
        if self.webInstance is not None:
            self.webInstance.stop()

    def shutdownEoqInstance(self):
        ''' Shuts down the web-instance if applicable'''
        if self.eoqInstance is not None:
            self.eoqInstance.Stop(None,None)
        time.sleep(1)
        if self.eoqThread is not None:
            self.eoqThread.join()

    def get_conf_parameter(self,name):
        ''' Retrieves the configuration parameters from the app configuration '''
        res=None
        parameters=name.split("/")
        conf_item=self.app_conf
        for param in parameters:
            if conf_item is None:
                break
            else:
                if param in conf_item:
                    conf_item=conf_item[param]
                else:
                    conf_item=None  
        else:
            res=conf_item        
        return res


def shutdownTornado():
    ''' '''
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.stop()
    global FRAMEWORK_RUN_FLAG
    for app in apps:
        app.shutdownWebInstance()
    FRAMEWORK_RUN_FLAG=False


def stop(signal,frame):
    ''' Stop XGEE framework '''
    global FRAMEWORK_RUN_FLAG
    print('Shutting down XGEE framework...')
    FRAMEWORK_RUN_FLAG=False    
    tornado.ioloop.IOLoop.current().add_callback_from_signal(shutdownTornado)  

  

 
    


def start(path2apps):    
    ''' Start XGEE framework '''

    global FRAMEWORK_RUN_FLAG
    print("""   
                 _  _  ___  ____  ____ 
                ( \/ )/ __)( ___)( ___)
                 )  (( (_-. )__)  )__) 
                (_/\_)\___/(____)(____)
                VERSION """+str(__version__)+"""

                        """);
                    

    p = Path(path2apps)
    conffile = Path(str(p)+'/configuration.yml')
    if conffile.is_file():
        appname='.'
        app_conf=load(conffile.read_text(),Loader=Loader)
        apps.append(XGEEApp(str(p)+'/'+str(appname)+"/",str(appname),app_conf))
    else:
        # Read app folder and configure XGEE apps   
        if p.is_dir():
            # Instantiate XGEE apps
            appnames=set([f.name for f in p.iterdir() if f.is_dir()])
            for appname in appnames:
                conf = Path(str(p)+'/'+str(appname)+"/configuration.yml")       
                if conf.is_file():
                    app_conf=load(conf.read_text(),Loader=Loader)
                    apps.append(XGEEApp(str(p)+'/'+str(appname)+"/",str(appname),app_conf))
        else:
            print('Invalid directory supplied')

    # Launch XGEE apps
    if len(apps):      
        webInstances=0
        eoqInstances=0
        for app in apps:
            webInstance,eoqInstance=app.launch()
            webInstances+=webInstance
            eoqInstances+=eoqInstance

        print('')
        print('Your XGEE apps are ready:')
        table=[[app.getName(),app.getPath(),app.getWebInstanceUrl(),app.getEoqInstanceUrl()] for app in apps ]
        print(tabulate(table,["App Name","App Path","Web Instance", "EOQ Instance"],tablefmt="fancy_grid"))
        print('')

        if webInstances>0:        
            tornado.ioloop.IOLoop.instance().start()

        if eoqInstances==0:
            FRAMEWORK_RUN_FLAG=False

        # Loop To keep running even if no webinstance is hosted until termination
        while(FRAMEWORK_RUN_FLAG):
            time.sleep(1)

        for app in apps:
            app.shutdownEoqInstance()

        print('XGEE framework stopped.')



          
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT,  stop)
    path2apps=DEFAULT_PATH
    if len(sys.argv)>1:
        path2apps=sys.argv[1]
    start(path2apps) 

        
    



