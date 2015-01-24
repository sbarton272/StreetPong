
import pygame as pg

class Keys(object):

    NONE = 0
    RIGHT = 1
    LEFT = 2

    def __init__(s, leftKey, rightKey):
        s.rightKey = rightKey
        s.leftKey = leftKey

    def getMove(s):

        pressed = pg.key.get_pressed()

        if pressed[s.leftKey]:
            move = s.LEFT
        elif pressed[s.rightKey]:
            move = s.RIGHT
        else:
            move = s.NONE

        return move

