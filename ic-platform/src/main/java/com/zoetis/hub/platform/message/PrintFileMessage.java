package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrintJobAbortedDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
public final class PrintFileMessage extends PrintAccessObjectMessage<PrintJobAbortedDto>
{

	public PrintFileMessage(PrintJobAbortedDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINT_FILE;
	}
}
