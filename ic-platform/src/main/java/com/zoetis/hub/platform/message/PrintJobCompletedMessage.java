package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrintJobCompletedDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;


@NoArgsConstructor
public final class PrintJobCompletedMessage extends PrintAccessObjectMessage<PrintJobCompletedDto>
{
	public PrintJobCompletedMessage(PrintJobCompletedDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINTJOB_COMPLETED;
	}
}
