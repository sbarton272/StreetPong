
import serial, time

class Communications(object):

    BAUD = 115200
    PORT = '/dev/ttyS1'
    TERM = '\n'
    TEST_MSG = 'Huston we have a problem'

    def __init__(s):

        s.port = serial.Serial(s.PORT, s.BAUD)

        print 'Connected to', s.port.portstr

    def testMaster(s):
        print 'Testing coms'
        msg = s.read()
        print 'Master recieved', msg
        time.sleep(.5)
        s.write(msg)
        print 'Master sent', msg
        print 'Communincations spec out'

    def testSlave(s):
        print 'Testing coms'
        msg = s.TEST_MSG
        s.write(msg)
        print 'Slave sent', msg
        rsp = s.read()
        print 'Slave recieved', rsp
        print 'Communincations spec out'

    def writeDict(s, d):
        s.port.write(repr(d) + s.TERM)

    def readDict(s):
        return eval(s.port.readline())

    def writeByte(s, b):
        s.port.write(str(b))

    def readByte(s):
        return s.port.read()

    def write(s, msg):
        s.port.write(msg + s.TERM)

    def read(s):
        return s.port.readline()
