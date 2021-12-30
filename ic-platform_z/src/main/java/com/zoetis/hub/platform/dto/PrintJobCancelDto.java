package com.zoetis.hub.platform.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

/**
 * 
 * @author bag
 * 
 * Example JSON string
 * 
 * {
 * 		"correlationID": 5481863
 * }
*/

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrintJobCancelDto
{
	/**
	 * The ID provided by Hub apps to identify a print job.
	 * The ID is used to identify response topic messages. 
	 */
	private int correlationID;

	@NonNull
	private String printerName;
	
	public String toString()
	{ 
		String str;
		str = "{\n";
		str += "\"correlationID\":" + this.correlationID + ",\n";
		str += "\"printerName\":" + this.printerName + "\n";
		str += "}";
	    return str;
	}
	
}
