
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

    def writeGameState(s, gs):
        args = []
        args.append(str(gs['paddle1']))
        args.append(str(gs['paddle2']))
        args.append(str(gs['score1']))
        args.append(str(gs['score2']))
        args.append(str(gs['ballX']))
        args.append(str(gs['ballY']))
        args.append(str(gs['gameOver']))

        msg = ' '.join(args)
        print 'Coms write', msg
        s.port.write(msg + s.TERM)

    def readGameState(s):
        m = ''
        while len(m) <= 1:
            m = s.port.readline().strip()

        args = m.split(' ')
        print 'Coms read', args

        gameState = {}
        gameState['paddle1'] = int(args[0])
        gameState['paddle2'] = int(args[1])
        gameState['score1'] = int(args[2])
        gameState['score2'] = int(args[3])
        gameState['ballX'] = int(args[4])
        gameState['ballY'] = int(args[5])
        gameState['gameOver'] = int(args[6])
        return gameState

    def writeByte(s, b):
        print 'Coms write', b
        s.port.write(str(b))

    def readByte(s):
        b = s.port.read()
        print 'Coms read', b
        return b

    def write(s, msg):
        s.port.write(msg + s.TERM)

    def read(s):
        return s.port.readline()
