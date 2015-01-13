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

#=====================================================
# PongGame
#=====================================================

class PongGameView(object):
    MV_RIGHT = 0
    MV_LEFT  = 1
    SCORE_NONE = 0
    SCORE_P1 = 1
    SCORE_P2 = 2

    """
    PongGame model for paddles and ball dynamics and control

    Parameters
    ----------

    """
    def __init__(s, game, windowW, windowH, endZone, paddleWidth):
        s.game = game
        s.w = windowW
        s.h = windowH
        s.endZone = endZone
        s.paddleWidth = paddleWidth

    #==== Public Methods ========================================

    def show(s):
        """
        Show the game
        """
        s._showBoard()
        s._showPaddle(s.game.p1)
        s._showPaddle(s.game.p2)
        s._showBall(s.game.ball)

    def _showBoard(s):
        # Background

        # Midline

    def _showPaddle(s, player):
        
