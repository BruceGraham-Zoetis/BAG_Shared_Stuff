package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrintJobAbortedDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;


@NoArgsConstructor
public final class PrintJobAbortedMessage extends PrintAccessObjectMessage<PrintJobAbortedDto>
{
	public PrintJobAbortedMessage(PrintJobAbortedDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINTJOB_ABORTED;
	}
}
