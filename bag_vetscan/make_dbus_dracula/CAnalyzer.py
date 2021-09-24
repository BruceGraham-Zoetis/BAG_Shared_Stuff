"""
File: CAnalyzer.py

"""

from dbus_next.service import (method, dbus_property, signal)
from dbus_next import Variant, DBusError

import configuration_channel_controller
import control_channel_controller
import measurement_channel_controller
import status_channel_controller
import prompts_channel_controller
from CAnalyzerBase import CAnalyzerBase
from CMeasurementOperation import CMeasurementOperation


# ServiceInterface exports Methods: @method(), Properties: @property, Signals:@signal()
class CZoetisAnalyzerInterface(CAnalyzerBase):
    def __init__(self, str_analyzer_name):
        super().__init__(str_analyzer_name)
        self.operation_current = CMeasurementOperation(
                                    measurement_id     = 'THX 1138',
                                    elapsed_time_msec  = '12345',
                                    measurement_status = 'Running',
                                    status_detail      = 'JUST HAVING FUN!')


    ########################################################
    # from configuration_channel_controller.py
    ########################################################
    @method()
    def configuration_factory_reset_put(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = configuration_channel_controller.configuration_factory_reset_put(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = configuration_channel_controller.configuration_get(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_put(self, str_request_body : 's') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = configuration_channel_controller.configuration_put(self, str_request_body)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_schema_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = configuration_channel_controller.configuration_schema_get(self)
        # return a str to caller
        return str(dict_rtn)

    ########################################################
    # from control_channel_controller.py
    ########################################################
    @method()
    def control_light_blink_put(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = control_channel_controller.control_light_blink_put(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def control_power_off_put(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = control_channel_controller.control_power_off_put(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def control_power_reboot_put(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = control_channel_controller.control_power_reboot_put(self)
        # return a str to caller
        return str(dict_rtn)

    ########################################################
    # from measurement_channel_controller.py
    ########################################################
    @method()
    def measurement_cancel_post(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_cancel_post(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_consumable_consumable_uuid_post(self, consumable_uuid : 's') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_consumable_consumable_uuid_post(self, consumable_uuid)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_file_post(self, body_file_json : 'a{ss}') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_file_post(self, body_file_json)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_results_get(self, start_datetime : 's', end_datetime : 's') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_results_get(self, start_datetime, end_datetime)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_result_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_result_get(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_results_latest_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_results_latest_get(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_script_post(self, body_script_json : 'a{ss}') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_script_post(self, body_script_json)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_supported_consumables_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = measurement_channel_controller.measurement_supported_consumables_get(self)
        # return a str to caller
        return str(dict_rtn)


    ########################################################
    # from status_channel_controller.py
    ########################################################
    @method()
    def status_currently_activated_events_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = status_channel_controller.status_currently_activated_events_get(self)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def status_operational_get(self) -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = status_channel_controller.status_operational_get(self)
        # return a str to caller
        return str(dict_rtn)


    ########################################################
    # from prompts_channel_controller.py
    ########################################################
    # TODO Pass inline_object3
    @method()
    def prompts_notification_ack_post(self, body_notification_ack : 'a{ss}') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = prompts_channel_controller.prompts_notification_ack_post(self, body_notification_ack)
        # return a str to caller
        return str(dict_rtn)

    # TODO Pass inline_object2
    @method()
    def prompts_option_chosen_post(self, body : 'a{ss}') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = prompts_channel_controller.prompts_option_chosen_post(self, body)
        # return a str to caller
        return str(dict_rtn)

    # TODO Pass inline_object4
    @method()
    def prompts_qr_scanned_post(self, body : 'a{ss}') -> 's':
        # over-ride CAnalyzerBase

        dict_rtn = prompts_channel_controller.prompts_qr_scanned_post(self, body)
        # return a str to caller
        return str(dict_rtn)

    ########################################################
    # from here - test methods, signals
    ########################################################
    @method()
    def Frobate(self, foo: 'i', bar: 's') -> 'a{us}':
        print(f'called Frobate with foo={foo} and bar={bar}')

        lst = {
            1: 'one',
            2: 'two'
        }
        return lst


    @method()
    async def Bazify(self, bar: '(iiu)') -> 'vv':
        print(f'called Bazify with bar={bar}')

        return [Variant('s', 'zoetis'), Variant('s', 'bazify')]

    @method()
    def Mogrify(self, bar: '(iiav)'):
        raise DBusError('com.zoetis.error.CannotMogrify',
                        'it is not possible to mogrify')

    @signal()
    def Changed(self) -> 'b':
        return True

    ########################################################
    # from here - measurement_id Property getter and setter
    ########################################################

    @dbus_property()
    def measurement_id(self) -> 's':
        return self.operation_current.measurement_id

    @measurement_id.setter
    def measurement_id(self, val: 's'):
        if self.operation_current.measurement_id == val:
            return

        self.operation_current.measurement_id = val

        self.emit_properties_changed({'measurement_id': self.operation_current.measurement_id})

