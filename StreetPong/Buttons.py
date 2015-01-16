
import os

class Buttons(object):
    GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
    GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
    GPIO_FILENAME = "gpio"

    HIGH = "1"
    LOW = "0"
    INPUT = "0"
    OUTPUT = "1"
    INPUT_PU = "8"

    NONE = 0
    RIGHT = 1
    LEFT = 2

    def __init__(s, pin1, pin2):
        buttonL_pin_mode = os.path.join(s.GPIO_MODE_PATH, 'gpio'+str(pin1))
        buttonR_pin_mode = os.path.join(s.GPIO_MODE_PATH, 'gpio'+str(pin2))

        s.buttonL_pin = os.path.join(s.GPIO_PIN_PATH, 'gpio'+str(pin1))
        s.buttonR_pin = os.path.join(s.GPIO_PIN_PATH, 'gpio'+str(pin2))

        FP = open(buttonL_pin_mode, 'r+')
        FP.write(s.INPUT_PU)
        FP.close()

        FP = open(buttonR_pin_mode, 'r+')
        FP.write(s.INPUT_PU)
        FP.close()

    def getMove(s):

        # getting input from L button
        tempL = ['']
        FP = open(s.buttonL_pin, 'r')
        tempL[0] = FP.read()
        FP.close()
        
        # getting input from R button
        tempR = ['']
        FP = open(s.buttonR_pin, 'r')
        tempR[0] = FP.read()
        FP.close()

        for i in xrange(1,30):
            print 'Buttons', tempL, tempR

        if ( '0' in tempL[0] ):
            move = s.LEFT
        elif ( '0' in tempR[0] ):
            move = s.RIGHT
        else:
            move = s.NONE

        return move

