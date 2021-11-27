package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrintJobProcessingDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
public final class PrintJobProcessingMessage extends PrintJobMessage<PrintJobProcessingDto>
{
	public PrintJobProcessingMessage(PrintJobProcessingDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINTJOB_PROCESSING;
	}
}

