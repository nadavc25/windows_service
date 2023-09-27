import os
import sys
import time
import logging
import requests
import win32serviceutil
import win32service
import win32event
import servicemanager

class WebsiteMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'WebsiteMonitorService'
    _svc_display_name_ = 'Website Monitor Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_alive = True
        self.url_to_monitor = "https://www.google.com"  # Replace with the website you want to monitor
        self.log_file = "C:\python\python\windows_service\windows_service.log"  

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

def main(self):
    logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    while self.is_alive:
        try:
            response = requests.get(self.url_to_monitor)
            if response.status_code == 200:
                logging.info(f"The website {self.url_to_monitor} is alive.")
            else:
                logging.warning(f"The website {self.url_to_monitor} is not alive. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"An error occurred while checking the website: {str(e)}")

        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WebsiteMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(WebsiteMonitorService)
