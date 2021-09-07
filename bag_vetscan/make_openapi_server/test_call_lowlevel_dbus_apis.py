

"""
File: test_call_lowlevel_dbus_apis.py
"""

import os, sys

strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/analyzer_app")
from analyzer_app.openapi_server.models.inline_object1 import InlineObject1
from analyzer_app.openapi_server.controllers import CDBusDraculaService


if __name__ == '__main__':
    print("Test - Call all low-level 'Dracula' DBus service APIs")

    # get and set measurement_id 
    str_value = CDBusDraculaService.g_dbus_dracula_service.measurement_id
    print("measurement_id: %s" % CDBusDraculaService.g_dbus_dracula_service.measurement_id)
    CDBusDraculaService.g_dbus_dracula_service.measurement_id = "xyz123"
    print("measurement_id after set: %s" % CDBusDraculaService.g_dbus_dracula_service.measurement_id)

    print("\nfile: configuration_controller.py")
    print("=========================================")
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_factory_reset_put()
    print("configuration_factory_reset_put()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_get()
    print("configuration_get()\n\t%s" % strRtn)

    oSomeObject = {"bla": "bla"}
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_put(str(oSomeObject))
    print("configuration_put()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_schema_get()
    print("configuration_schema_get()\n\t%s" % strRtn)


    print("\nfile: control_channel_controller.py")
    print("=========================================")
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_light_blink_put()
    print("control_light_blink_put()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_power_off_put()
    print("control_power_off_put()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_power_reboot_put()
    print("control_power_reboot_put()\n\t%s" % strRtn)


    print("\nfile: measurement_channel_controller.py")
    print("=========================================")
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_cancel_post()
    print("measurement_cancel_post()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_consumable_consumable_uuid_post("consumable_uuid")
    print("measurement_consumable_consumable_uuid_post()\n\t%s" % strRtn)

    inline_object1 = InlineObject1(filename="dummy")
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_file_post(str(inline_object1))
    print("measurement_file_post()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_results_get("2020-11-05T13:15:30+00:00", "2020-12-02T14:29:27+00:00")
    print("measurement_results_get()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_result_get()
    print("measurement_result_get()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_results_latest_get()
    print("measurement_results_latest_get()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_script_post("inline_object")
    print("measurement_script_post()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_supported_consumables_get()
    print("measurement_supported_consumables_get()\n\t%s" % strRtn)


    print("\nfile: status_channel_controller.py")
    print("=========================================")
    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.status_currently_activated_events_get()
    print("status_currently_activated_events_get()\n\t%s" % strRtn)

    strRtn = CDBusDraculaService.g_dbus_dracula_service.draculad.status_operational_get()
    print("status_operational_get()\n\t%s" % strRtn)
