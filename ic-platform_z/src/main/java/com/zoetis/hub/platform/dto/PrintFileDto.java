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
	
	private boolean sheetCollate;
	private boolean colorEnabled;
	private boolean duplexEnabled;
	private int     copies;
	
	public static void PrintFileDto_clear(PrintFileDto printFileDto)
	{
		printFileDto.correlationID = -1;
		printFileDto.printerName = "";
		printFileDto.fileName = "";
		printFileDto.sheetCollate = false;
		printFileDto.colorEnabled = false;
		printFileDto.duplexEnabled = false;
		printFileDto.copies = 0;	
	}

	public static void PrintFileDto_init(
			PrintFileDto printFileDto,
			int correlationID,
			String printerName,
			String fileName,
			boolean sheetCollate,
			boolean colorEnabled,
			boolean duplexEnabled,
			int     copies)
	{
		printFileDto.correlationID = correlationID;
		printFileDto.printerName = printerName;
		printFileDto.fileName = fileName;
		printFileDto.sheetCollate = sheetCollate;
		printFileDto.colorEnabled = colorEnabled;
		printFileDto.duplexEnabled = duplexEnabled;
		printFileDto.copies = copies;	
	}

	public String toString()
	{ 
		String str;
		str = "{\n";
		str += "\t\"correlationID\": " + this.correlationID + ", \n";
		str += "\t\"printerName\": \"" + this.printerName + "\", \n";
		str += "\t\"fileName\": \"" + this.fileName + "\", \n";
		str += "\t\"sheetCollate\": " + this.sheetCollate + ", \n";
		str += "\t\"colorEnabled\": " + this.colorEnabled + ", \n";
		str += "\t\"duplexEnabled\": " + this.duplexEnabled + ", \n";
		str += "\t\"copies\": " + this.copies + "\n";
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

	public boolean getSheetCollate() {
		return sheetCollate;
	}

	public void setSheetCollate(boolean sheetCollate) {
		this.sheetCollate = sheetCollate;
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