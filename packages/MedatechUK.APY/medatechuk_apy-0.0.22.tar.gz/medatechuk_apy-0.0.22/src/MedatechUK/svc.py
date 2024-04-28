import os , time , sys
from pathlib import Path

import win32serviceutil , win32service , win32event, servicemanager
import configparser , debugpy

from MedatechUK.mLog import mLog 
from MedatechUK.cl import clArg

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        
class AppSvc (win32serviceutil.ServiceFramework):

#region "Properties"
    @property
    def Main(self):    
        try: return self._Main
        except: return None
    @Main.setter
    def Main(self, value):
        self._Main = value        

    @property
    def Init(self):    
        try: return self._Init
        except: return None
    @Init.setter
    def Init(self, value):
        self._Init = value      

    @property
    def Folder(self):    
        try: return self._Folder
        except: return os.getcwd()
    @Folder.setter
    def Folder(self, value):
        if os.path.isdir(str(value)):
            self._Folder = value 
        else: raise "Invalid folder spec."

#endregion
        
#region "Ctor"        
    def __init__(self,args):               
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        
        self.stop = False                                
        self.settingsini = str(self.Folder) + "\\settings.ini"      
        os.chdir(self.Folder)      

        #region "Verify .ini"
        if os.path.isfile(self.settingsini):                
            config = configparser.ConfigParser()                        
            config.read(self.settingsini)
            save = False
            if 'debug' not in config.sections():
                config['debug'] = {} 
                save = True  
            if not config['debug'].__contains__("verbosity"):
                config['debug']['VERBOSITY'] = 'DEBUG'    
                save = True
            if not config['debug'].__contains__("port"):
                config['debug']['PORT'] = '5678'                    
                save = True
            if save :
                with open(self.settingsini, 'w') as configfile:
                    config.write(configfile)                                    
        else:            
            config = configparser.ConfigParser()
            config['debug'] = {}    
            config['debug']['VERBOSITY'] = 'DEBUG'
            config['debug']['PORT'] = '5678'
            with open(self.settingsini, 'w') as configfile:
                config.write(configfile)      
        
        #endregion      
        
        config = configparser.ConfigParser(dict_type=AttrDict)
        config.read(self.settingsini)
        self.config = config._sections           

        self.log = mLog()                       
        self.log.start( str(self.Folder) , self.config.debug.verbosity )
        self.log.logger.info("Using Settings file: [{}]".format( self.settingsini ))     
        self.log.logger.info("Intialising Service [{}] with Verbosity [{}]...".format(
            self._svc_name_ 
            , self.config.debug.verbosity 
        ))            

        self.clArg = clArg(args=args)      
        self.debug = 'debug' in self.clArg.kwargs()
        if self.debug:                    
            self.log.logger.info("debugpy listening on: [{}]".format(self.config.debug.port))                     
            debugpy.configure(python=str(Path(sys.executable).parent) + "\\python.exe")
            debugpy.listen( int( self.config.debug.port ) )             
        
        self.debuginit = False            
        if self.Init != None:                        
            if self.debug and self.clArg.kwargs()["debug"] != None:
                if self.clArg.kwargs()["debug"].lower() == "init" :
                    self.debuginit = True
                    debugpy.wait_for_client()           
            self.Init(self)

#endregion        

#region "Methods"        
    def SvcStop(self):
        self.log.logger.info("Service [{}] Stopping...".format(self._svc_name_ ))  
        if self.debug: debugpy.wait_for_client.cancel()

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop = True

    def SvcDoRun(self):        
        if self.Main == None:            
            raise "No Main() entry point."
        
        self.log.logger.info("Starting Service [{}]...".format(self._svc_name_ ))
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                        servicemanager.PYS_SERVICE_STARTED,
                        (self._svc_name_,''))        

        while not self.stop: 
            try:   
                if self.debug: debugpy.wait_for_client()    
                self.Main(self)

            except Exception as error: 
                self.log.logger.critical(error)   
                raise
            
            for i in range(50): # 5 seconds
                if not self.stop:
                    time.sleep(.1)
                if self.stop: break

#endregion