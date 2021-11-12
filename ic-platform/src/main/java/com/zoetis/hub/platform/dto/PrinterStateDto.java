package com.zoetis.hub.platform.dto;

import java.io.Serializable;

/**
 * @author bag
 *
 */


/**
 * Printer State Reason
==================================
Field					Description
====================	======================
CONNECTING_TO_DEVICE	The printer has scheduled a job on the output device and is in the process of connecting to a shared network output device (and might not be able to actually start printing the job for an arbitrarily long time depending on the usage of the output device by other servers on the network).
COVER_OPEN				One or more covers on the device are open.
DEVELOPER_EMPTY			The device is out of developer.
DEVELOPER_LOW			The device is low on developer.
DOOR_OPEN				One or more doors on the device are open.
FUSER_OVER_TEMP			The fuser temperature is above normal.
FUSER_UNDER_TEMP		The fuser temperature is below normal.
INPUT_TRAY_MISSING		One or more input trays are not in the device.
INTERLOCK_OPEN			One or more interlock devices on the printer are unlocked.
INTERPRETER_RESOURCE_UNAVAILABLE	An interpreter resource is unavailable (e.g., font, form).
MARKER_SUPPLY_EMPTY		The device is out of at least one marker supply (e.g. toner, ink, ribbon).
MARKER_SUPPLY_LOW		The device is low on at least one marker supply (e.g. toner, ink, ribbon).
MARKER_WASTE_ALMOST_FULL	The device marker supply waste receptacle is almost full.
MARKER_WASTE_FULL		The device marker supply waste receptacle is full.
MEDIA_EMPTY				At least one input tray is empty.
MEDIA_JAM				The device has a media jam.
MEDIA_LOW				At least one input tray is low on media.
MEDIA_NEEDED		A tray has run out of media.
MOVING_TO_PAUSED	Someone has paused the printer, but the device(s) are taking an appreciable time to stop.
OPC_LIFE_OVER		The optical photo conductor is no longer functioning.
OPC_NEAR_EOL		The optical photo conductor is near end of life.
OTHER			The printer has detected an error other than ones listed below.
OUTPUT_AREA_ALMOST_FULL One or more output areas are almost full (e.g. tray, stacker, collator).
OUTPUT_AREA_FULL	One or more output areas are full (e.g. tray, stacker, collator).
OUTPUT_TRAY_MISSING	One or more output trays are not in the device.
PAUSED			Someone has paused the printer and the printer's PrinterState is STOPPED.
SHUTDOWN		Someone has removed a printer from service, and the device may be powered down or physically removed.
SPOOL_AREA_FULL	The limit of persistent storage allocated for spooling has been reached.
STOPPED_PARTLY		When a printer controls more than one output device, this reason indicates that one or more output devices are stopped.
STOPPING		The printer is in the process of stopping the device and will be stopped in a while.
TIMED_OUT		The server was able to connect to the output device (or is always connected), but was unable to get a response from the output device.
TONER_EMPTY		The device is out of toner.
TONER_LOW		The device is low on toner.

 */


public class PrinterStateDto implements Serializable
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;


}
