#!/usr/bin/env python3

"""
File: CDBusDraculaService.py

TODO:
* Create a DBus .service file

    File: com.zoetis.dracula.service 

    [D-BUS Service]
    Name=com.zoetis.dracula
    Exec=/home/myuser/Workspace/service-start
    User=myuser

pip3 install pydbus
"""

import os, sys
from pydbus import SessionBus
import threading

strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/..")
from models import inline_object1


def get_analyzer_name() -> str:
    str_analyzer_name = "dracula"
    return str_analyzer_name

def get_analyzer_dbus_request_name() -> str:
    str_request_name = 'com.zoetis.' + get_analyzer_name()
    return str_request_name


"""
Class for the Dracula service. This is a singleton.

"""
class CDBusDraculaService():
    # bus: single instance of the session bus
    # draculad: the single instance of the dracula demon

    _instance = None
    _lock = threading.Lock()

    def get_request_name(self) -> str:
        str_request_name = get_analyzer_dbus_request_name()
        return str_request_name


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            # another thread could have created the instance
            # before we acquired the lock. So check that the
            # instance is still nonexistent.
            if not cls._instance:
                cls._instance = super(CDBusDraculaService, cls).__new__(cls)
                # Put any initialization here.
                str_request_name = get_analyzer_dbus_request_name()

                cls.bus      = SessionBus()
                cls.draculad = cls.bus.get(str_request_name)
                #print('Created new singleton ', cls._instance)
            else:
                #print("using singleton ", cls._instance)
                pass

        return cls._instance

    @property
    def measurement_id(self) -> str:
        return self.draculad.measurement_id

    @measurement_id.setter
    def measurement_id(self, str_value : str):
        self.draculad.measurement_id = str_value



if __name__ == '__main__':
    print("Test - Call all low-level 'Dracula' DBus service APIs")

    oDracula = CDBusDraculaService()

    # get and set measurement_id 
    str_value = oDracula.measurement_id
    print("measurement_id: %s" % oDracula.measurement_id)
    oDracula.measurement_id = "xyz123"
    print("measurement_id after set: %s" % oDracula.measurement_id)

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

    inline_object1 = inline_object1.InlineObject1(filename="dummy", local_vars_configuration=None)
    strRtn = oDracula.draculad.measurement_file_post(inline_object1)
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
