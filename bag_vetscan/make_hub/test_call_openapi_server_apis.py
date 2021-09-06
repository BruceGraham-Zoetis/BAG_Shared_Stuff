
"""
File: test_call_openapi_server_apis.py

"""

import hub_app_gui.class_analyzer_openapi
from hub_app.openapi_client.rest import ApiException
from hub_app.openapi_client.models.inline_object1 import InlineObject1


if __name__ == '__main__':
    print("")

    str_ip_address = "127.0.0.1"
    str_client_name = "dracula"

    oAna = hub_app_gui.class_analyzer_openapi.analyzer_client(str_ip_address, str_client_name)

    ################################################
    # Class: ConfigurationApi
    ################################################
    """
    configuration_factory_reset_put
    configuration_get
    configuration_put
    configuration_schema_get
    """
    ################################################
    # Class: ControlChannelApi
    ################################################
    oAna.control_light_blink_put()
    oAna.control_power_off_put()
    oAna.control_power_reboot_put()

    ################################################
    # File: measurement_channel_api
    ################################################
    oAna.channel_measurement_get_measurement_status()
    oAna.measurement_cancel_delete()
    oAna.measurement_consumable_consumable_uuid_post("consumable_uuid")

    #inline_object1 = InlineObject1(filename="dummy", local_vars_configuration=None)
    #oAna.measurement_file_post(inline_object1)
    oAna.measurement_file_post("dummy_file")
    oAna.measurement_past_results_get("start_time", "start_date", "end_time", "end_date")
    oAna.measurement_result_get()
    #oAna.measurement_script_post(inline_object1)
    oAna.measurement_script_post("dummy_file")
    oAna.measurement_supported_consumables_get()

    ################################################
    # Class: StatusChannelApi
    ################################################
    """
    status_currently_activated_events_get
    status_operational_get
    """
