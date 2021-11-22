package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
public final class PrintFileMessage extends PrintAccessObjectMessage<PrintFileRequestDto>
{
	public PrintFileMessage(PrintFileRequestDto payload)
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
