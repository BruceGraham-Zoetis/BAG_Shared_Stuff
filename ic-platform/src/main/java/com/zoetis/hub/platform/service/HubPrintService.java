package com.zoetis.hub.platform.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

@Service
public class HubPrintService {
    
    @Autowired
    PrinterAccessObject obj;
    
	@KafkaListener(topics="printFile", groupId="ic-platform")
	public void consumePrintFile(PrintFileRequestDto requestDetails) throws PrintAccessException
	{
		System.out.println("Consume Topic: printFile");
		System.out.println("\tprinterName: " + requestDetails.getPrinterName());
		System.out.println("\tfileName: " + requestDetails.getFileName());
		System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
		System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
		System.out.println("\tcopies: " + requestDetails.getCopies());
		
		try
		{
			obj.setDebugTrace(true);
			obj.printFile(requestDetails);
		}
		catch (PrintAccessException e)
		{
			System.err.println(e.getErrorMsg());
		}
	}
}