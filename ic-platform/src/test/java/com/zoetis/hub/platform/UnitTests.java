package com.zoetis.hub.platform;

import org.junit.jupiter.api.Test;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;
import com.zoetis.hub.platform.service.Producer;


/**
 * Unit tests
 * 
 * @author Bruce Graham
 * 
 * Add a "PDF Printer" by installing the cups-pdf package:
 * sudo apt-get install printer-driver-cups-pdf
 */
class UnitTests
{
	@Test
	void discoveryMessageSerDe ()
	{
		/**
		 * print the file to a PDF printer
		 */
		PrintFileRequestDto requestDetails = new PrintFileRequestDto();
		
		requestDetails.setColorEnabled(true);
		requestDetails.setDuplexEnabled(true);
		requestDetails.setCopies(2);
		requestDetails.setPrinterName("Print_to_PDF");
		requestDetails.setPrintJobName("PRINTJOB1");
		requestDetails.setFileName("/home/bag/test_files/file.pdf");
		
		Producer producer = new Producer();
		producer.publishPrintFile(requestDetails);
		
		assert true;
	}
}
