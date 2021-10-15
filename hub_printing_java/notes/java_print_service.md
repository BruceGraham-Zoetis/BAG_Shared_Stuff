Java Print Service
======================
https://docs.oracle.com/javase/6/docs/technotes/guides/jps/index.html

The Java Print Service API, introduced in v1.4, allows printing on all Java platforms 
including those requiring a small footprint, such as a J2ME profile, but also supports 
the java.awt.print.PrinterJob API introduced in J2SE v1.2. The Java Print Service API 
includes an extensible print attribute set based on the standard attributes specified 
in the Internet Printing Protocol (IPP) 1.1 from the IETF. With the attributes, 
client and server applications can discover and select printers that have the 
capabilities specified by the attributes. In addition to the included StreamPrintService, 
which allows applications to transcode data to different formats, third parties can dynamically 
install their own print services through the Service Provider Interface.


API Specification
======================
The Java Print Service API consists of these four packages:
javax.print:
Provides the principal classes and interfaces for the Java Print Service API.

javax.print.attribute:
Provides classes and interfaces that describe the types of Java Print Service attributes and how they can be collected into attribute sets.

javax.print.attribute.standard:
Contains classes defining specific printing attributes.

javax.print.event:
Contains event classes and listener interfaces for monitoring print services and the progress of a specific print job.

