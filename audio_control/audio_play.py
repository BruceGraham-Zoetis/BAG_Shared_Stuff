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
import wave
#import getopt
import alsaaudio

"""
Purpose: Play a wav file, given a file handle to the file

Example:
	with wave.open("./beep-08b.wav", 'rb') as f:
		play(f)

@param[in] f = file handle to a wav file.

"""
def play(f):	

	format = None

	# 8bit is unsigned in wav files
	if f.getsampwidth() == 1:
		format = alsaaudio.PCM_FORMAT_U8
	# Otherwise we assume signed data, little endian
	elif f.getsampwidth() == 2:
		format = alsaaudio.PCM_FORMAT_S16_LE
	elif f.getsampwidth() == 3:
		format = alsaaudio.PCM_FORMAT_S24_3LE
	elif f.getsampwidth() == 4:
		format = alsaaudio.PCM_FORMAT_S32_LE
	else:
		raise ValueError('Unsupported format')

	periodsize = f.getframerate() // 8
	device = 'default'

	"""
	print('%d channels, %d sampling rate, format %d, periodsize %d\n' % (f.getnchannels(),
																		 f.getframerate(),
																		 format,
																		 periodsize))
	"""

	device = alsaaudio.PCM(channels=f.getnchannels(), rate=f.getframerate(), format=format, periodsize=periodsize, device=device)
	
	data = f.readframes(periodsize)
	while data:
		# Read data from stdin
		device.write(data)
		data = f.readframes(periodsize)



