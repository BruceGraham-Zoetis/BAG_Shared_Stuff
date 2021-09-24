#!/usr/bin/env python3
"""
@breif CAnalyzerBase.py

Purpose: DBus service interface for the analyzer app.

Notes:
The parameters and return types must be type cast. For example: use 's' for str type.
See https://python-dbus-next.readthedocs.io/en/latest/type-system

"""

from dbus_next.service import (ServiceInterface, method)

# ServiceInterface exports Methods: @method(), Properties: @property, Signals:@signal()
class CAnalyzerBase(ServiceInterface):
	def __init__(self, str_analyzer_name):
		super().__init__(str_analyzer_name)

	@method()
	def configuration_get(self) -> 's':
		"""Request the configuration from the analyzer

		"""
		return "OK"

	@method()
	def configuration_put(self, body : 'a{ss}') -> 's':
		"""Set the configuration of the analyzer
		@param[in] body - object An object containing the full configuration for the analyzer
		"""
		return "OK"

	@method()
	def configuration_schema_get(self) -> 's':
		"""Request the configuration schema from the analyzer

		"""
		return "OK"

	@method()
	def configuration_factory_reset_put(self) -> 's':
		"""Restore the analyzer to the state it was in when it left the factory. All settings and data are removed.

		"""
		return "OK"

	@method()
	def control_light_blink_put(self) -> 's':
		"""Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it.

		"""
		return "OK"

	@method()
	def control_power_reboot_put(self) -> 's':
		"""Request sent from a client to reboot the analyzer (power off and power back on), leaving all settings and data intact

		"""
		return "OK"

	@method()
	def control_power_off_put(self) -> 's':
		"""Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn't support power off, go to 'deep sleep' mode

		"""
		return "OK"

	@method()
	def measurement_supported_consumables_get(self) -> 's':
		"""Return a list of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/).

		"""
		return "OK"

	@method()
	def measurement_script_post(self, body : 'a{ss}') -> 's':
		"""Start an analyzer measurement script sent as a string.  This is intended for R&D use only and should not be used during normal operation
		@param[in] body - object This JSON object will contain the name of a script (full path and file name) on the analyzer. The script will be executed
		"""
		return "OK"

	@method()
	def measurement_file_post(self, body : 'a{ss}') -> 's':
		"""Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&D use only and should not be used during normal operation
		@param[in] body - object This JSON object will contain the name of a file (full path and file name) on the analyzer. The file shall contain the name of a measurement script that will be executed
		"""
		return "OK"

	@method()
	def measurement_consumable_post(self, consumable_uuid : 's') -> 's':
		"""Start an analyzer measurement with a specific consumable
		@param[in] consumable_uuid - string The UUID of the consumable
		"""
		return "OK"

	@method()
	def measurement_cancel_post(self) -> 's':
		"""The HUB is requesting the analyzer cancel the measurement that is currently being performed

		"""
		return "OK"

	@method()
	def measurement_results_latest_get(self) -> 's':
		"""The client requests that the analyzer return the result of the most recent measurement performed

		"""
		return "OK"

	@method()
	def measurement_results_get(self) -> 's':
		"""The client is requesting the analyzer to send past results between two times

		"""
		return "OK"

	@method()
	def status_operational_get(self) -> 's':
		"""The HUB can use send this message to get the status of an analyzer

		"""
		return "OK"

	@method()
	def status_currently_activated_events_get(self) -> 's':
		"""The HUB is requesting the analyzer respond with a list of all currently activated events

		"""
		return "OK"

	@method()
	def prompts_option_chosen_post(self, body : 'a{ss}') -> 's':
		"""Hub is informing the analyzer of an option that was made by the operator in response to a websocket message named choose_option on the prompts channel.
		@param[in] body - object 
		"""
		return "OK"

	@method()
	def prompts_notification_ack_post(self, body : 'a{ss}') -> 's':
		"""Hub is informing the analyzer a notification was acknowledged by the operator in response to a websocket message named notification on the prompts channel.
		@param[in] body - object 
		"""
		return "OK"

	@method()
	def prompts_qr_scanned_post(self, body : 'a{ss}') -> 's':
		"""Hub is informing the analyzer of a QR scan attempt in response to a websocket message named scan_qr on the prompts channel.
		@param[in] body - object 
		"""
		return "OK"

