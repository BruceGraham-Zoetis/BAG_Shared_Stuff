package com.zoetis.hub.platform.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

@Service
public class Producer {
	
	@Autowired
	private KafkaTemplate<String, PrintFileRequestDto> kafkaPrintFile;
	
	public void publishPrintFile(PrintFileRequestDto requestDetails) {
		final String topic = "printFile";
		
		String strFileName = requestDetails.getFileName();
		if ("" == strFileName)
		{
			return;
		}
		
		System.out.println("Producer Topic: " + topic);
		System.out.println("\tprinterName: " + requestDetails.getPrinterName());
		System.out.println("\tfileName: " + requestDetails.getFileName());
		System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
		System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
		System.out.println("\tcopies: " + requestDetails.getCopies());
				
		this.kafkaPrintFile.send(topic, requestDetails);
	}
	
	/*
	@Autowired
	private KafkaTemplate<String, DefaultPrinterDto> kafkaDefaultPrinter;
	
	public void send(DefaultPrinterDto requestDetails) {
		String topic = "default-printer";
	    
	    kafkaDefaultPrinter.send(topic, requestDetails);
	}
	*/

	/*
	@Autowired
	private KafkaTemplate<String, SystemPrintersDto> kafkaSystemPrinters;
	
	public void send(SystemPrintersDto requestDetails) {
		String topic = "system-printers";
	    
	    kafkaSystemPrinters.send(topic, requestDetails);
	}
	*/
}
