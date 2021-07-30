CC = g++

PLATFORM = GNU
ARCH = x64
LIB=libSPV4L2.a 

SOURCE=main.cpp
OUTPUT=main

#static
LIBPATH = ../lib/libSPV4L2/$(PLATFORM)/$(ARCH)/$(LIB)

all:
	$(CC) -o $(OUTPUT) $(SOURCE) $(LIBPATH)
	
.PHONY:	clean

clean:
	$(RM) $(OUTPUT)
	$(RM) ./*.o
	$(RM) ./*.so
	$(RM) ./*.a
