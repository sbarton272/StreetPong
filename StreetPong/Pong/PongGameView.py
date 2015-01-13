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

#=====================================================
# Constants
#=====================================================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
MIDLINE_H = 6
FONT_SIZE = 36

#=====================================================
# PongGame
#=====================================================

class PongGameView(object):

    def __init__(s, game, screen, windowW, windowH, endZone, paddleW, paddleH, radius):
        s.game = game
        s.screen = screen
        s.w = windowW
        s.h = windowH
        s.endZone = endZone
        s.paddleW = paddleW
        s.paddleH = paddleH
        s.ballRadius = int(radius)

        s.midLine = pg.Rect(0, s.h/2 - MIDLINE_H/2, s.w, MIDLINE_H)

    #==== Public Methods ========================================

    def show(s):
        """
        Show the game
        """
        s._showBoard()
        s._showPaddles()
        s._showBall()
        #s._showScore()
        pg.display.flip()

    def _showBoard(s):
        # Background
        s.screen.fill(BLACK)

        # Midline
        pg.draw.line(s.screen, GRAY, (0, s.h/2), (s.w, s.h/2))

    def _showPaddles(s):
        p1 = s.game.p1
        rect = pg.Rect(p1.paddleLoc - s.paddleW/2, s.endZone, s.paddleW, s.paddleH)
        pg.draw.rect(s.screen, WHITE, rect)

        p2 = s.game.p2
        rect = pg.Rect(p2.paddleLoc - s.paddleW/2, s.h - s.endZone, s.paddleW, s.paddleH)
        pg.draw.rect(s.screen, WHITE, rect)
        
    def _showScore(s):
        # TODO
        font = pg.font.Font(None, FONT_SIZE)
        text = font.render(str(s.game.p1.score), 1, GRAY)
        textpos = text.get_rect()
        textpos.centerx = s.screen.get_rect().centerx
        s.screen.blit(text, textpos)

    def _showBall(s):
        ball = s.game.ball
        pos = (ball.x, ball.y)
        pg.draw.circle(s.screen, WHITE, pos, s.ballRadius)
        