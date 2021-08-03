#!/usr/bin/env python3
 
"""
File: audio_play.py

Purpose: Python wrapper for playing wav files, etc.

download https://pypi.org/project/pyalsaaudio/#files
$ tar xf pyalsaaudio-0.9.0.tar.gz
$ cd Downloads/pyalsaaudio-0.9.0/
$ python3 setup.py build
$ sudo python3 setup.py install

Test Python app
=========================
$ python3 playwav.py ./beep-08b.wav

"""

#from subprocess import call
#import sys
from typing import Text
import wave
import select
import alsaaudio

"""
Purpose: Play a wav file, given a path and file name

Example:
	playWaveFileAndBlock("./beep-08b.wav")

@param[in] txtPathFileName = path and file name of a wav file.

@returns True = played file
@returns False = failed
"""
def playWaveFileAndBlock(txtPathFileName : Text) -> bool:	
	try:
		oFile = wave.open(txtPathFileName, 'rb')
	except:
		print("ERROR: File not found %s" % (txtPathFileName))
		return False

	format = None

	# 8bit is unsigned in wav files
	if oFile.getsampwidth() == 1:
		format = alsaaudio.PCM_FORMAT_U8
	# Otherwise we assume signed data, little endian
	elif oFile.getsampwidth() == 2:
		format = alsaaudio.PCM_FORMAT_S16_LE
	elif oFile.getsampwidth() == 3:
		format = alsaaudio.PCM_FORMAT_S24_3LE
	elif oFile.getsampwidth() == 4:
		format = alsaaudio.PCM_FORMAT_S32_LE
	else:
		raise ValueError('Unsupported format')

	periodsize = oFile.getframerate() // 8
	txtOutputDeviceName = 'default'

	"""
	print('%d channels, %d sampling rate, format %d, periodsize %d\n' % (oFile.getnchannels(),
																		 oFile.getframerate(),
																		 format,
																		 periodsize))
	"""

	# Setup PCM device
	pcmDevice = alsaaudio.PCM(channels=oFile.getnchannels(),
							mode=alsaaudio.PCM_NORMAL,
							rate=oFile.getframerate(),
							format=format,
							periodsize=periodsize,
							device=txtOutputDeviceName)
	
	# get master mixer
	mixer = alsaaudio.Mixer(control='Master')

	# get descriptors from mixer
	descriptors = mixer.polldescriptors()
	#print(descriptors)

	# setup polling with mixer's descriptors
	poll = select.poll()
	#poll.register(descriptors[0][0])
	poll.register(descriptors[0][0], select.POLLOUT)
	#poll.register(descriptors[0][0], select.POLLOUT | select.POLLIN | select.POLLPRI)
	#poll.register(descriptors[0][0])

	# read first data from the file
	data = oFile.readframes(periodsize)

	while data:
		# clear the events for the write
		mixer.handleevents()

		print("write: %d bytes to PCM Device" % (len(data)))
		pcmDevice.write(data)

		print("wait for events from the mixer")
		events = poll.poll()                   ########## TODO -stuck here - poll.register() is not setup correctly.
		for event in events:
			print("fd: %d  event: %d " % (event[0], event[1]))
			if (event[1] == select.POLLOUT):
				print("POLLOUT - queue is writable")
			elif (event[1] == select.POLLIN):
				print("POLLIN - can read without blocking")
			elif (event[1] == select.POLLPRI):
				print("POLLPRI - high-pri msg at head of queue")

		# read more data from the file
		data = oFile.readframes(periodsize)

	oFile.close()
	return True

