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
 * 		"printJobName": "job-5481863",
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
	@NonNull
	private String action;
	
	@NonNull
	private String name;
	
	/**
	 * The name for the print job that is provided by Hub apps. 
	 */
	@NonNull
	private String printJobName;
	
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
		str = "{\"action\":\"" + this.action + "\", ";
		str += "\"name\":\"" + this.name + "\", ";
		str += "\"printJobName\":\"" + this.printJobName + "\", ";
		str += "\"printerName\":\"" + this.printerName + "\", ";
		str += "\"fileName\":\"" + this.fileName + "\", ";
		str += "\"colorEnabled\":" + this.colorEnabled + ", ";
		str += "\"duplexEnabled\":" + this.duplexEnabled + ", ";
		str += "\"copies\":" + this.copies + "}";
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

	public String getPrintJobName() {
		return printJobName;
	}

	public void setPrintJobName(String printJobName) {
		this.printJobName = printJobName;
	}
   
}