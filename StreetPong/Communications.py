
import serial

class Communications(object):

	BAUD = 115200
	PORT = '/dev/ttyS1'
	TERM = '\n'

	def __init__(s):

		s.port = serial.Serial(s.PORT, s.BAUD)

		print 'Connected to', s.port.portstr

	def writeDict(s, d):
		s.port.write(repr(d) + s.TERM)

	def readDict(s):
		return eval(s.port.readline().strip())

	def writeByte(s, b):
		s.port.write(str(b))

	def readByte(s):
		return s.port.read()
