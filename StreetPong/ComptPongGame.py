"""
Street Pong
Build 18 2015
Leanna Pancoast, Spencer Barton, Justin Frye

Pong Game View
"""

#=====================================================
# Imports
#=====================================================

import pygame as pg
import sys

#=====================================================
# Constants
#=====================================================

WIDTH = 480
HEIGHT = 480
END_ZONE = 30
PADDLE_WIDTH = 20

#=====================================================
# PongGame
#=====================================================

class PongGame(object):
    def __init__(s, game, windowW, windowH):
        s.w = WIDTH
        s.h = HEIGHT
        s.endZone = END_ZONE
        s.paddleWidth = PADDLE_WIDTH

        pg.init()
        s.screen = pg.display.set_mode((s.w,s.h))

    #==== Public Methods ========================================

    def run(s):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        
if __name__ == '__main__':
    pongGame = PongGame()
    pongGame.run()