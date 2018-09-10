CPP             = g++
CPPFLAGS        = -g -O1 -Wall -fPIC -D_REENTRANT -Wno-deprecated -I. 

ROOTCFLAGS      := $(shell root-config --cflags)
ROOTLIBS        := $(shell root-config --libs) -lMinuit -lEG #-lg2c
# ROOTLIBS        += $(shell echo ${MY_LDLib})
ROOTGLIBS       := $(shell root-config --glibs)

CPPFLAGS        += $(ROOTCFLAGS)
LIBS            = $(ROOTLIBS) -lm -L.
GLIBS           = $(ROOTGLIBS)

TARGET = main

OBJS =  main.o

all: ${TARGET}
	echo "- - - - - - - - - - - - - - \n- - - - Successfully - - - - \n- - - - - - - - - - - - - -"

${TARGET}: $(OBJS)
	$(CPP) -o $@ $(CPPFLAGS) $(OBJS) $(LIBS) $(EXTERNAL_OBJS)

main.o :  main.cc 
	$(CPP) -c $(CPPFLAGS) main.cc

clean: 
	-rm ${TARGET}
	-rm ${OBJS}
	-rm *~
