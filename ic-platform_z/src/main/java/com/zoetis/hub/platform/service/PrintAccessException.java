package com.zoetis.hub.platform.service;

public class PrintAccessException extends Exception
{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private final E_EXCEPTION_ID m_id;
    private final String         m_strErrorMsg;

    enum E_EXCEPTION_ID
    {
        // occurs during print job creation
        FILE_NOT_FOUND,
        PRINTER_DEFAULT_NOT_FOUND,
        PRINTER_NAME_NOT_FOUND,
        PRINTER_PDF_NOT_SUPPORTED,
        PRINTER_COLOR_NOT_SUPPORTED,
        PRINTER_DUPLEX_NOT_SUPPORTED,
        PRINTER_SHEETCOLLATE_NOT_SUPPORTED,

        /// occurs when print job has started
        PRINTJOB_IN_PROCESS,
        PRINTJOB_FAILED,
        PRINTJOB_PROCESSING_FAILED,
        PRINTJOB_REQUIRES_ATTENTION,
        // occurs when waiting for print job to complete
        THREAD_INTERRUPT,

        // occurs when attempting to cancel print job
        PRINTJOB_CANCEL_FAILED

    }

    public PrintAccessException(
            E_EXCEPTION_ID id,
            String strErrorMsg)
    {
        m_id         = id;
        m_strErrorMsg = strErrorMsg;
    }

    public String getErrorMsg()
    {
        return m_strErrorMsg;
    }
    
    public E_EXCEPTION_ID getErrorID()
    {
        return m_id;
    }
}
    