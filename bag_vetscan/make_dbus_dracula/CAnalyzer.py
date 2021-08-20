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


class CZoetisAnalyzerInterface(ServiceInterface):
    def __init__(self, strAnalyzerName):
        super().__init__(strAnalyzerName)
        self._bar = 105

    ########################################################
    # from configuration_controller.py
    ########################################################
    @method()
    def configuration_factory_reset_put(self):
        return configuration_controller.configuration_factory_reset_put()

    @method()
    def configuration_get(self):
        return configuration_controller.configuration_get()

    @method()
    def configuration_put(body):
        return configuration_controller.configuration_put()

    @method()
    def configuration_schema_get(self):
        return configuration_controller.configuration_schema_get()

    ########################################################
    # from control_channel_controller.py
    ########################################################
    def control_light_blink_put(self):
        return control_channel_controller.control_light_blink_put()

    def control_light_off_put(self):
        return control_channel_controller.control_light_off_put()

    def control_power_off_put(self):
        return control_channel_controller.control_power_off_put()

    def control_power_reboot_put(self):
        return control_channel_controller.control_power_reboot_put()

    ########################################################
    # from measurement_channel_controller.py
    ########################################################
    def channel_measurement_get_measurement_status(self):
        return measurement_channel_controller.channel_measurement_get_measurement_status()

    def measurement_cancel_delete(self):
        return measurement_channel_controller.measurement_cancel_delete()

    def measurement_consumable_consumable_uuid_post(consumable_uuid):
        return measurement_channel_controller.measurement_consumable_consumable_uuid_post(consumable_uuid)

    def measurement_file_post(inline_object1):
        return measurement_channel_controller.measurement_file_post(inline_object1)

    def measurement_past_results_get(start_time, start_date, end_time, end_date):
        return measurement_channel_controller.measurement_past_results_get(start_time, start_date, end_time, end_date)

    def measurement_result_get(self):
        return measurement_channel_controller.measurement_result_get()

    def measurement_script_post(inline_object):
        return measurement_channel_controller.measurement_script_post(inline_object)

    @method()
    def measurement_supported_consumables_get(self) -> 's':
        # returns dictionary type
        dictRtn = measurement_channel_controller.measurement_supported_consumables_get()

        return str(dictRtn)


    ########################################################
    # from status_channel_controller.py
    ########################################################
    def status_currently_activated_events_get(self):
        return status_channel_controller.configuration_schema_get()

    def status_operational_get(self):
        return status_channel_controller.status_operational_get()


    @method()
    def Frobate(self, foo: 'i', bar: 's') -> '{sa{sv}}':
        print(f'called Frobate with foo={foo} and bar={bar}')

        """
        lst = {
            1: 'one',
            2: 'two'
        }
        return lst
        """
        return {
            1: 'one',
            2: 'two'
        } 

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

    @dbus_property()
    def Bar(self) -> 'y':
        return self._bar

    @Bar.setter
    def Bar(self, val: 'y'):
        if self._bar == val:
            return

        self._bar = val

        self.emit_properties_changed({'Bar': self._bar})

