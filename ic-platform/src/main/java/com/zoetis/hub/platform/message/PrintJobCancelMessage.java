package com.zoetis.hub.platform.message;

import com.fasterxml.jackson.annotation.JsonTypeName;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
@JsonTypeName("PRINTJOB_CANCEL")
public final class PrintJobCancelMessage extends PrintAccessObjectMessage<PrintJobCancelDto>
{
	public PrintJobCancelMessage(PrintJobCancelDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINTJOB_CANCEL;
	}
}
