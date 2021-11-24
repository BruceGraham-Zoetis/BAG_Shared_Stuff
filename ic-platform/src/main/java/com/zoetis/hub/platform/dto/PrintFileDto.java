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
 * 		"correlationID": 5481863,
 * 		"printerName": "HP-Color-LaserJet-Pro-M453-4",
 * 		"fileName": /home/bag/test_files/file.txt",
 * 		"colorEnabled": false,
 * 		"duplexEnabled": true,
 * 		"copies": 3
 * }
*/
@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrintFileDto
{
	/**
	 * The ID provided by Hub apps to identify a print job.
	 * The ID is used to identify response topic messages. 
	 */
	private int correlationID;
	
	@NonNull
	private String printerName;
	
	@NonNull
	private String fileName;
	
	private boolean colorEnabled;
	private boolean duplexEnabled;
	private int     copies;

	public String toString()
	{ 
		String str;
		str = "{\n";
		str += "\"correlationID\":" + this.correlationID + ", \n";
		str += "\"printerName\":\"" + this.printerName + "\", \n";
		str += "\"fileName\":\"" + this.fileName + "\", \n";
		str += "\"colorEnabled\":" + this.colorEnabled + ", \n";
		str += "\"duplexEnabled\":" + this.duplexEnabled + ", \n";
		str += "\"copies\":" + this.copies + "\n";
		str += "}";
	    return str;
	}
	
	public String getPrinterName() {
		return printerName;
	}

	public void setPrinterName(String printerName) {
		this.printerName = printerName;
	}

	public String getFileName() {
		return fileName;
	}

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}

	public boolean getColorEnabled() {
		return colorEnabled;
	}

	public void setColorEnabled(boolean colorEnabled) {
		this.colorEnabled = colorEnabled;
	}

	public boolean getDuplexEnabled() {
		return duplexEnabled;
	}

	public void setDuplexEnabled(boolean duplexEnabled) {
		this.duplexEnabled = duplexEnabled;
	}

	public int getCopies() {
		return copies;
	}

	public void setCopies(int copies) {
		this.copies = copies;
	}

	public int getCorrelationID() {
		return correlationID;
	}

	public void setCorrelationID(int correlationID) {
		this.correlationID = correlationID;
	}
   
}