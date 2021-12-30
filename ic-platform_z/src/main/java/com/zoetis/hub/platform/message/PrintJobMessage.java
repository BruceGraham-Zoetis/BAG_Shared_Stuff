package com.zoetis.hub.platform.message;

/**
*/

import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.zoetis.hub.message.ApplicationMessage;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@JsonTypeInfo (
	use = JsonTypeInfo.Id.NAME,
	// Makes Jackson use the existing getAction() method for serialization
	include = JsonTypeInfo.As.EXISTING_PROPERTY,
	property = "action"
)
@JsonSubTypes ({
	@JsonSubTypes.Type(value = PrintJobProcessingMessage.class, name = "PRINTJOB_PROCESSING"),
	@JsonSubTypes.Type(value = PrinterStateMessage.class, name = "PRINTER_STATE")
})
public abstract class PrintJobMessage<D>
	extends ApplicationMessage<PrintJobMessage.Action, D>
{
	public static final String TOPIC = "printAccessObject";
	
	public enum Action
	{
		PRINTJOB_PROCESSING,
		PRINTER_STATE
	}
	
	public PrintJobMessage(D payload)
	{
	    super(payload);
	}
}
