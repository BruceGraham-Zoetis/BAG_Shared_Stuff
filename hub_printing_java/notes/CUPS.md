Common UNIX Printing System (CUPS)
=====================================
CUPS consists of a print spooler and scheduler, a filter system that converts 
the print data to a format that the printer will understand, and a backend system 
that sends this data to the print device. CUPS uses the Internet Printing Protocol (IPP) 
as the basis for managing print jobs and queues.


CUPS Raster Format
======================
https://www.cups.org/doc/spec-raster.html
CUPS Raster files are device-dependent raster image files that contain a 
PostScript page device dictionary and device-dependent raster imagery for each page in the document. 
These files are used to transfer raster data from the PostScript and image file RIPs 
to device-dependent filters that convert the raster data to a printable format.

CUPS 1.0 and 1.1 used version 1 of the raster format. CUPS 1.2 and later use 
version 2 (compressed) and version 3 (uncompressed) that are a superset of the 
version 1 raster format. All three versions of CUPS Raster are streamable formats, 
and applications using the CUPS Imaging API (the cupsRaster* functions) can 
read all formats without code changes.

The registered MIME media type for CUPS Raster files is application/vnd.cups-raster.


CUPS Components
======================
CUPS scheduler
CUPS filters
    /usr/lib/cups/filter
    converts app's default PostScript PDL to printer's PDL
CUPS backends
    /usr/lib/cups/backends
    provides interface from scheduler to printer hardware interface
PostScript Printer Description (PPD) files


Print job data flow to printer
================================
cupsd = CUPS system print deamon

app -> cupsd -> /var/spool/cups -> filter -> backend -> printer hardware


