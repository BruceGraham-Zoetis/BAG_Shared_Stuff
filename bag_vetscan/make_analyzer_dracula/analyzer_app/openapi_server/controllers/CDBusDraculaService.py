#!/usr/bin/env python3

"""
File: CDBusDraculaService.py

TODO: Intergrate this code into the analyzer app.

pip3 install pydbus
"""

from pydbus import SessionBus
from pydbus import SystemBus
import threading
import dbus
import os
import subprocess
import time
import pathlib


def get_analyzer_name() -> str:
    strAnalyzerName = "dracula"
    return strAnalyzerName

def get_analyzer_dbus_request_name() -> str:
    strRequestName = 'com.zoetis.' + get_analyzer_name()
    return strRequestName


"""
Class for the Dracula service. This is a singleton.

"""
class CDBusDraculaService():
    # bus: single instance of the session bus
    # draculad: the single instance of the dracula demon

    _instance = None
    _lock = threading.Lock()

    def get_request_name(self) -> str:
        strRequestName = get_analyzer_dbus_request_name()
        return strRequestName


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            # another thread could have created the instance
            # before we acquired the lock. So check that the
            # instance is still nonexistent.
            if not cls._instance:
                cls._instance = super(CDBusDraculaService, cls).__new__(cls)
                # Put any initialization here.
                strRequestName = get_analyzer_dbus_request_name()

                cls.bus      = SessionBus()
                cls.draculad = cls.bus.get(strRequestName)
                #print('Created new singleton ', cls._instance)
            else:
                #print("using singleton ", cls._instance)
                pass

        return cls._instance

    @property
    def nTest(self) -> int:
        return self.draculad.nTest

    @nTest.setter
    def nTest(self, iValue : int):
        self.draculad.nTest = iValue

"""
TODO - Create a DBus .service file

File: com.zoetis.dracula.service 

[D-BUS Service]
Name=com.zoetis.dracula
Exec=/home/myuser/Workspace/service-start
User=myuser

"""

if __name__ == '__main__':
    print("Test - Call all APIs")

    """
    REQUEST_NAME_REPLY_ALREADY_OWNER = 4
    REQUEST_NAME_REPLY_EXISTS        = 3
    REQUEST_NAME_REPLY_IN_QUEUE      = 2
    REQUEST_NAME_REPLY_PRIMARY_OWNER = 1

    strRequestName = get_analyzer_dbus_request_name()
    #strRequestName = "com.xxxx"
    iRtn = dbus.SessionBus().request_name(strRequestName)
    if (REQUEST_NAME_REPLY_PRIMARY_OWNER == iRtn):
        #print("REQUEST_NAME_REPLY_PRIMARY_OWNER")
        print("Starting Dracula service")
        path = pathlib.Path(__file__)
        path = path.parent
        path = pathlib.Path(path)
        path = path.parent
        path = pathlib.Path(path)
        path = path.parent
        path = pathlib.Path(path)
        path = path.parent
        path = pathlib.Path(path)
        strPath = str(path.parent)
        strPath += "/make_dbus_dracula/test_run_dbus_dracula.py"
        #iRtn = subprocess.call(["python3", strPath, "&"])
        #execfile(strPath)
        os.system("python3 " + strPath)
        if (0 == iRtn):
            time.sleep(10)
        else:
            print("Error failed to start dracula service")

    elif (REQUEST_NAME_REPLY_IN_QUEUE == iRtn):
        #print("REQUEST_NAME_REPLY_IN_QUEUE")
        pass
    elif (REQUEST_NAME_REPLY_EXISTS == iRtn):
        #print("REQUEST_NAME_REPLY_EXISTS")
        pass
    elif (REQUEST_NAME_REPLY_ALREADY_OWNER == iRtn):
        #print("REQUEST_NAME_REPLY_ALREADY_OWNER")
        pass
    """

    oDracula = CDBusDraculaService()


    # get and set nTest 
    iValue = oDracula.nTest
    print("nTest: %d" % oDracula.nTest)
    oDracula.nTest += 10
    print("nTest after += 10: %d" % oDracula.nTest)

    oDracula = CDBusDraculaService()

    print("\nfile: configuration_controller.py")
    print("=========================================")
    strRtn = oDracula.draculad.configuration_factory_reset_put()
    print("configuration_factory_reset_put()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.configuration_get()
    print("configuration_get()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.configuration_put("body")
    print("configuration_put()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.configuration_schema_get()
    print("configuration_schema_get()\n\t%s" % strRtn)


    print("\nfile: control_channel_controller.py")
    print("=========================================")
    strRtn = oDracula.draculad.control_light_blink_put()
    print("control_light_blink_put()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.control_light_off_put()
    print("control_light_off_put()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.control_power_off_put()
    print("control_power_off_put()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.control_power_reboot_put()
    print("control_power_reboot_put()\n\t%s" % strRtn)


    print("\nfile: measurement_channel_controller.py")
    print("=========================================")
    strRtn = oDracula.draculad.measurement_cancel_delete()
    print("measurement_cancel_delete()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_consumable_consumable_uuid_post("consumable_uuid")
    print("measurement_consumable_consumable_uuid_post()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_file_post("inline_object1")
    print("measurement_file_post()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_past_results_get("start_time", "start_date", "end_time", "end_date")
    print("measurement_past_results_get()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_result_get()
    print("measurement_result_get()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_script_post("inline_object")
    print("measurement_script_post()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.measurement_supported_consumables_get()
    print("measurement_supported_consumables_get()\n\t%s" % strRtn)


    print("\nfile: status_channel_controller.py")
    print("=========================================")
    strRtn = oDracula.draculad.status_currently_activated_events_get()
    print("status_currently_activated_events_get()\n\t%s" % strRtn)

    strRtn = oDracula.draculad.status_operational_get()
    print("status_operational_get()\n\t%s" % strRtn)
