package com.zoetis.hub.platform.message;

/**
Print Job Processing State Descriptions
============================================
Field					Description
====================	======================
ABORTED					The job has been aborted by the system
						(usually while the job was in the PROCESSING or PROCESSING_STOPPED state),
						the printer has completed aborting the job,
						and all job status attributes have reached their final values for the job.

CANCELED				The job has been canceled by some human agency,
						the printer has completed canceling the job,
						and all job status attributes have reached their final values for the job.

COMPLETED				The job has completed successfully or with warnings or errors after processing, all of the
						job media sheets have been successfully stacked in the appropriate output bin(s), and all
						job status attributes have reached their final values for the job.

PENDING					The job is a candidate to start processing, but is not yet processing.

PENDING_HELD			The job is not a candidate for processing for any number of reasons but will return to the
 						PENDING state as soon as the reasons are no longer present.

PROCESSING				The job is processing.

PROCESSING_STOPPED		The job has stopped while processing for any number of reasons and will return to the
 						PROCESSING state as soon as the reasons are no longer present.

UNKNOWN					The job state is unknown.

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
	@JsonSubTypes.Type(value = PrintJobAbortedMessage.class, name = "PRINTJOB_ABORTED"),
	//@JsonSubTypes.Type(value = PrintJobCanceledMessage.class, name = "PRINTJOB_CANCELED"),
	@JsonSubTypes.Type(value = PrintJobCompletedMessage.class, name = "PRINTJOB_COMPLETED"),
	//@JsonSubTypes.Type(value = PrintJobPendingMessage.class, name = "PRINTJOB_PENDING"),
	//@JsonSubTypes.Type(value = PrintJobPendingHeldMessage.class, name = "PRINTJOB_PENDING_HELD"),
	//@JsonSubTypes.Type(value = PrintJobProcessingMessage.class, name = "PRINTJOB_PROCESSING"),
	//@JsonSubTypes.Type(value = PrintJobProcessingStoppedMessage.class, name = "PRINTJOB_PROCESSING_STOPPED"),
	//@JsonSubTypes.Type(value = PrintJoUnknownMessage.class, name = "PRINTJOB_UNKNOWN")
})
public abstract class PrintAccessObjectMessage<D>
	extends ApplicationMessage<PrintAccessObjectMessage.Action, D>
{
	public static final String TOPIC = "printAccessObject";
	
	public enum Action
	{
		PRINT_FILE,
		PRINTJOB_ABORTED,
		//PRINTJOB_CANCELED,
		PRINTJOB_COMPLETED,
		//PRINTJOB_PENDING,
		//PRINTJOB_PENDING_HELD,
		//PRINTJOB_PROCESSING,
		//PRINTJOB_PROCESSING_STOPPED,
		//PRINTJOB_UNKNOWN
	}
	
	public PrintAccessObjectMessage(D payload)
	{
	    super(payload);
	}
}
