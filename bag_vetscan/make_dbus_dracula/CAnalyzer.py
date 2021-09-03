"""
File: CAnalyzer.py

"""

from dbus_next.service import (ServiceInterface,
                               method, dbus_property, signal)
from dbus_next import Variant, DBusError

import configuration_controller
import control_channel_controller
import measurement_channel_controller
import status_channel_controller

# ServiceInterface exports Methods: @method(), Properties: @property, Signals:@signal()
class CZoetisAnalyzerInterface(ServiceInterface):
    def __init__(self, str_analyzer_name):
        super().__init__(str_analyzer_name)
        self.__measurement_id = ""

    ########################################################
    # from configuration_controller.py
    ########################################################
    @method()
    def configuration_factory_reset_put(self) -> 's':
        # returns dictionary type
        dict_rtn = configuration_controller.configuration_factory_reset_put()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_get(self) -> 's':
        # returns dictionary type
        dict_rtn = configuration_controller.configuration_get()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_put(self, body : 's') -> 's':
        # returns dictionary type
        dict_rtn = configuration_controller.configuration_put(body)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def configuration_schema_get(self) -> 's':
        # returns dictionary type
        dict_rtn = configuration_controller.configuration_schema_get()
        # return a str to caller
        return str(dict_rtn)

    ########################################################
    # from control_channel_controller.py
    ########################################################
    @method()
    def control_light_blink_put(self) -> 's':
        # returns dictionary type
        dict_rtn = control_channel_controller.control_light_blink_put()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def control_light_off_put(self) -> 's':
        # returns dictionary type
        dict_rtn = control_channel_controller.control_light_off_put()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def control_power_off_put(self) -> 's':
        # returns dictionary type
        dict_rtn = control_channel_controller.control_power_off_put()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def control_power_reboot_put(self) -> 's':
        # returns dictionary type
        dict_rtn = control_channel_controller.control_power_reboot_put()
        # return a str to caller
        return str(dict_rtn)

    ########################################################
    # from measurement_channel_controller.py
    ########################################################
    @method()
    def channel_measurement_get_measurement_status(self) -> 's':
        # returns str type
        str_rtn = measurement_channel_controller.channel_measurement_get_measurement_status()
        # return a str to caller
        return str_rtn

    @method()
    def measurement_cancel_delete(self) -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_cancel_delete()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_consumable_consumable_uuid_post(self, consumable_uuid : 's') -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_consumable_consumable_uuid_post(consumable_uuid)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_file_post(self, inline_object1 : 's') -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_file_post(inline_object1)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_past_results_get(self, start_time: 's', start_date: 's', end_time: 's', end_date: 's') -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_past_results_get(start_time, start_date, end_time, end_date)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_result_get(self) -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_result_get()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_script_post(self, inline_object : 's') -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_script_post(inline_object)
        # return a str to caller
        return str(dict_rtn)

    @method()
    def measurement_supported_consumables_get(self) -> 's':
        # returns dictionary type
        dict_rtn = measurement_channel_controller.measurement_supported_consumables_get()
        # return a str to caller
        return str(dict_rtn)


    ########################################################
    # from status_channel_controller.py
    ########################################################
    @method()
    def status_currently_activated_events_get(self) -> 's':
        # returns dictionary type
        dict_rtn = status_channel_controller.status_currently_activated_events_get()
        # return a str to caller
        return str(dict_rtn)

    @method()
    def status_operational_get(self) -> 's':
        # returns dictionary type
        dict_rtn = status_channel_controller.status_operational_get()
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
        return self.__measurement_id

    @measurement_id.setter
    def measurement_id(self, val: 's'):
        if self.__measurement_id == val:
            return

        self.__measurement_id = val

        self.emit_properties_changed({'measurement_id': self.__measurement_id})

