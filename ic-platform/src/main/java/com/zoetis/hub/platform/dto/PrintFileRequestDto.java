package com.zoetis.hub.platform.dto;

import java.io.Serializable;

/**
 * 
 * @author bag
 * 
 * Example JSON string
 * 
 * {
 * 		"printerName": "HP-Color-LaserJet-Pro-M453-4",
 * 		"fileName": /home/bag/test_files/file.txt",
 * 		"colorEnabled": false,
 * 		"duplexEnabled": true,
 * 		"copies": 3,
 * 		"printJobName": "job-5481863"
 * }
*/

public class PrintFileRequestDto implements Serializable
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String printerName;
	private String fileName;
	private boolean colorEnabled;
	private boolean duplexEnabled;
	private int     copies;
	private String printJobName;
	
	public PrintFileRequestDto()
	{
		this.printerName = "";
		this.fileName = "";
		this.colorEnabled = false;
		this.duplexEnabled = false;
		this.copies = 0;
		this.printJobName = "";
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