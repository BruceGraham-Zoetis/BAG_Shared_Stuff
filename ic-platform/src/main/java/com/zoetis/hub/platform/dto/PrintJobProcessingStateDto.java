package com.zoetis.hub.platform.dto;

import java.io.Serializable;


/**
 * 
 * @author bag
 */

/**
Print Job Processing State Descriptions
============================================
Field					Description
====================	======================
ABORTED					The job has been aborted by the system (usually while the job was in the PROCESSING or
						PROCESSING_STOPPED state), the printer has completed aborting the job, and all job status
						attributes have reached their final values for the job.

CANCELED				The job has been canceled by some human agency, the printer has completed canceling the job,
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


/** 
 * Example JSON string
 * 
 * {
 * 		"printJobName": "job-5481863",
 * 		"state": "PENDING",
 * 		"printerStateReasons": "Out of paper."
 * }
*/

public class PrintJobProcessingStateDto implements Serializable
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;


}
