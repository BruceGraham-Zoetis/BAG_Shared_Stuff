package com.zoetis.hub.platform.service;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.dto.PrintFileRequestDto;
import com.zoetis.hub.platform.dto.PrintJobAbortedDto;
import com.zoetis.hub.platform.dto.PrintJobCompletedDto;
import com.zoetis.hub.platform.message.PrintAccessObjectMessage;
import com.zoetis.hub.platform.message.PrintFileMessage;

@Service
public class HubPrintServiceMessageListener
{
    @Autowired
    PrinterAccessObject prtAccObj;
    
    private Logger logger = LoggerFactory.getLogger (HubPrintServiceMessageListener.class); 
	
	@Autowired
    private ObjectMapper objectMapper;
    
	@Autowired
	private KafkaTemplate<String, PrintJobCompletedDto> kafkaPrintJobCompleted;
    
	@Autowired
	private KafkaTemplate<String, PrintJobAbortedDto> kafkaPrintJobAborted;
    
	@KafkaListener(topics="printAccessObject")
	public void consumePrintFile(String messageJson) throws PrintAccessException
	{
		prtAccObj.setDebugTrace(true);
        try
        {
            logger.info ("Received Topic printAccessObject message: {}", messageJson);
            var message = objectMapper.readValue (messageJson, PrintAccessObjectMessage.class);
            logger.info ("Parsed Topic printAccessObject message: {}", message);

            if (message instanceof PrintFileMessage)
            {
    			PrintFileRequestDto requestDetails = (PrintFileRequestDto) message.getPayload();  
	       		try
	    		{
	    			System.out.println("Message: printFile");
	    			System.out.println("\tprintJobName: " + requestDetails.getPrintJobName());
	    			System.out.println("\tprinterName: " + requestDetails.getPrinterName());
	    			System.out.println("\tfileName: " + requestDetails.getFileName());
	    			System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
	    			System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
	    			System.out.println("\tcopies: " + requestDetails.getCopies());

	    			if (prtAccObj.printFile(requestDetails))
	    			{
	    				PrintJobCompletedDto data = new PrintJobCompletedDto();
	    				data.setPrintJobName(requestDetails.getPrintJobName());
	    				sendPrintJobCompleted(data);
	    			}
	    			else
	    			{
	    				PrintJobAbortedDto data = new PrintJobAbortedDto();
	    				data.setPrintJobName(requestDetails.getPrintJobName());
	    				sendPrintJobAborted(data);
	    			}
	    		}
	    		catch (PrintAccessException e)
	    		{
	    			logger.error(e.getErrorMsg());
	    			
    				PrintJobAbortedDto data = new PrintJobAbortedDto();
    				data.setPrintJobName(requestDetails.getPrintJobName());
    				sendPrintJobAborted(data);
	    		}
            }
            else
            {
                logger.warn("Unrecognized message received: {}", message);
            }
        }
        catch (Exception e)
        {
            logger.error("Error handling printFile message", e);
        }
	}
	
	public void sendPrintJobCompleted(PrintJobCompletedDto data)
	{
		final String topic = "printJobState";
		
		System.out.println("Producer Topic: " + topic);
		System.out.println("\tprintJobName: " + data.getPrintJobName());
				
		kafkaPrintJobCompleted.send(topic, data);
	}

	public void sendPrintJobAborted(PrintJobAbortedDto data)
	{
		final String topic = "printJobState";
		
		System.out.println("Producer Topic: " + topic);
		System.out.println("\tprintJobName: " + data.getPrintJobName());
				
		kafkaPrintJobAborted.send(topic, data);
	}
}
