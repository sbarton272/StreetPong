"""
Street Pong
Build 18 2015
Leanna Pancoast, Spencer Barton, Justin Frye

Pong Game
"""

#=====================================================
# Imports
#=====================================================

import random as rnd
import math

#=====================================================
# Constants
#=====================================================

# TODO figure out how else to get this const
STARTING_VELOCITY_MAGNITUDE = 3
STARTING_VELOCITY_ANGLE = 30 # degrees

#=====================================================
# PongGame
#=====================================================

class PongGame(object):
    """
    PongGame model for paddles and ball dynamics and control

    Parameters
    ----------

    """
    def __init__(s, windowW, windowH):
        s.w = windowW
        s.h = windowH
        s.size = (s.w, w.h)
        s.startVelMag = STARTING_VELOCITY_MAGNITUDE
        s.startVelAngle = STARTING_VELOCITY_ANGLE

    #==== Public Methods ========================================

    def start(s):
        """
        Reset the game to the start state
        1) Set paddle locations
        2) Set ball location
        3) Set random ball velocity

        Parameters
        ----------

        """
        s.ball.setLoc(s.w/2, s.h/2)
        s.ball.setVel(s._rndBallVel(s.startVelAngle, s.startVelMag))
        s.p1.paddle.setLoc(s.w/2)
        s.p2.paddle.setLoc(s.w/2)
        s.p1.setScore(0)
        s.p2.setScore(0)

    def step(s):
        """
        Step the game
        1) Set the paddle locations
        2) Set ball location
        3) Check for collisions and update ball location
        4) Check and update score
        5) Check win condition

        Parameters
        ----------

        """
        pass

    #==== Private Methods ======================================

    def _rndBallVel(s, angle, mag):
        """
        Generate a random velocity with the specified magnitude that points
        either up or down but no more than the specified angle off of the 
        horizontal line.

        Parameters
        ----------
        s       PongGame object
        angle   Maximum offset from horizontal in degrees
        mag     Magnitude of the velocity vector

        Returns
        -------
        Velocity tuple (x,y)        
        """
        maxX = math.sin(math.radians(angle))
        x = rnd.uniform(-maxX, maxX)
        y = 1 - x*x

        # Randomly determine up or down
        y = y * rnd.sample([-1,1], 1)[0]
        
        return (x*mag, y*mag)

#=====================================================
# Ball
#=====================================================

class Ball(object):
    pass

#=====================================================
# Player
#=====================================================

class Player(object):
    pass

#=====================================================
# Paddle
#=====================================================

class Paddle(object):
    pass