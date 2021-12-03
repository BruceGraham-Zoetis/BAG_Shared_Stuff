package com.zoetis.hub.platform.service;


import javax.print.attribute.standard.JobState;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;
import com.zoetis.hub.platform.dto.PrintJobStateDto;
import com.zoetis.hub.platform.message.PrintAccessObjectMessage;
import com.zoetis.hub.platform.message.PrintFileMessage;
import com.zoetis.hub.platform.message.PrintJobCancelMessage;

@Service
public class HubPrintServiceMessageListener
{
    @Autowired
    PrinterAccessObject prtAccObj;
    
    private Logger logger = LoggerFactory.getLogger (HubPrintServiceMessageListener.class);
	
	@Autowired
    private ObjectMapper objectMapper;
    
	@Autowired
	private KafkaTemplate<String, PrintJobStateDto> kafkaPrintJobState;
    
	@KafkaListener(topics = PrintAccessObjectMessage.TOPIC)
	public void PrintAccessObjectListener(String messageJson) throws PrintAccessException
	{
        try
        {
            logger.info ("Received Topic printAccessObject message: {}", messageJson);
            var message = objectMapper.readValue (messageJson, PrintAccessObjectMessage.class);
            logger.info ("Parsed Topic printAccessObject message: {}", message);

            if (message instanceof PrintFileMessage)
            {
            	PrintFileDto requestDetails;
            	try
            	{
            		requestDetails = (PrintFileDto) message.getPayload();
            	    handlePrintFileMessage(requestDetails);
            	}
                catch (Exception e)
                {
                	logger.error("Error message to printFileDto", e);
                }
            }
            else if (message instanceof PrintJobCancelMessage)
            {
            	PrintJobCancelDto requestDetails;
            	try
            	{
	            	requestDetails = (PrintJobCancelDto) message.getPayload();
	    			handlePrintJobCancelMessage(requestDetails);  
            	}
                catch (Exception e)
                {
                	logger.error("Error message to PrintJobCancelDto", e);
                }
            }
            else
            {
                logger.error("Unrecognized message received: {}", message);
            }
        }
        catch (Exception e)
        {
            logger.error("Error PrintAccessObjectListener", e);
        }
	}

	private void handlePrintFileMessage(PrintFileDto requestDetails)
	{
		try
		{
			logger.debug("Message: printFile PrintJobStateDto: " + 
					requestDetails.toString());

			if (prtAccObj.printFile(requestDetails))
			{
				PrintJobStateDto data = new PrintJobStateDto();
				data.setCorrelationID(requestDetails.getCorrelationID());
				data.jobState = JobState.PROCESSING.getValue(); 
				sendPrintJobState(data);
			}
			else
			{
				PrintJobStateDto data = new PrintJobStateDto();
				data.setCorrelationID(requestDetails.getCorrelationID());
				data.jobState = JobState.ABORTED.getValue();
				sendPrintJobState(data);
			}
		}
		catch (PrintAccessException e)
		{
			logger.error("printFile " + e.getErrorMsg());
		}
	}
	
	private void handlePrintJobCancelMessage(PrintJobCancelDto printJobCancelDto)
	{
   		try
		{
   			logger.debug("Message: printJobCancel PrintJobCancelDto: " +
					printJobCancelDto.toString());

			prtAccObj.stopPrintJobProcessing(printJobCancelDto);
   			
		}
		catch (PrintAccessException e)
		{
			logger.error("printJobCancel", e.getErrorMsg());
		}
	}
	
	private void sendPrintJobState(PrintJobStateDto data)
	{
		final String topic = "printJobState";
		
		logger.debug("Producer Topic: " + topic + " PrintJobStateDto: " + data.toString());

		kafkaPrintJobState.send(topic, data);
	}
}
