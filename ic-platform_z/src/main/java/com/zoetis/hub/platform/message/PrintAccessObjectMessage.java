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
	@JsonSubTypes.Type(value = PrintFileMessage.class, name = "PRINT_FILE"),
	@JsonSubTypes.Type(value = PrintJobCancelMessage.class, name = "PRINTJOB_CANCEL")
})
public abstract class PrintAccessObjectMessage<D>
	extends ApplicationMessage<PrintAccessObjectMessage.Action, D>
{
	public static final String TOPIC = "printAccessObject";
	
	public enum Action
	{
		PRINT_FILE,
		PRINTJOB_CANCEL
	}
	
	public PrintAccessObjectMessage(D payload)
	{
	    super(payload);
	}
}
