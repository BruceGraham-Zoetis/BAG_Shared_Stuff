
"""
File: test_call_openapi_server_apis.py

Purpose: Call the DBus service APIs in the 'Dracula' deamon. The openapi server will call the DBus APIs at run time.

"""

#import json
#from hub_app.openapi_client.models import inline_object1

import hub_app_gui.class_analyzer_openapi
from hub_app.openapi_client.rest import ApiException
from hub_app.openapi_client.models.inline_object1 import InlineObject1


if __name__ == '__main__':
    print("")

    str_ip_address = "127.0.0.1"
    str_client_name = "dracula"

    oAna = hub_app_gui.class_analyzer_openapi.analyzer_client(str_ip_address, str_client_name)

    ################################################
    # Class: ConfigurationChannelApi
    ################################################
    oAna.configuration_factory_reset_put()
    oAna.configuration_get()
    oSomeObject = {"bla": "bla"}
    oAna.configuration_put(oSomeObject)
    oAna.configuration_schema_get()

    ################################################
    # Class: ControlChannelApi
    ################################################
    oAna.control_light_blink_put()
    oAna.control_power_off_put()
    oAna.control_power_reboot_put()

    ################################################
    # File: measurement_channel_api
    ################################################
    oAna.measurement_cancel_post()
    oAna.measurement_consumable_consumable_uuid_post("consumable_uuid")

    #TODO How to pass object to openapi?
    #objectx = InlineObject1(filename="dummy")
    #oAna.measurement_file_post(inline_object1=objectx)
    oAna.measurement_results_get(start_datetime="2020-11-05T13:15:30+00:00", end_datetime="2020-12-02T14:29:27+00:00")
    #oAna.measurement_results_get()

    oAna.measurement_results_latest_get()

    #TODO How to pass object to openapi?
    #oAna.measurement_script_post(inline_object1)
    #oAna.measurement_script_post("dummy_file")

    oAna.measurement_supported_consumables_get()

    ################################################
    # Class: StatusChannelApi
    ################################################
    oAna.status_currently_activated_events_get()
    oAna.status_operational_get()
