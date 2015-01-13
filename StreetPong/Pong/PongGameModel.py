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

class PongGameModel(object):
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
    def __init__(s, name1, name2, windowW, windowH, endZone, paddleWidth):
        s.w = windowW
        s.h = windowH
        s.endZone = endZone
        s.size = (s.w, w.h)
        s.startVelMag = STARTING_VELOCITY_MAGNITUDE
        s.startVelAngle = STARTING_VELOCITY_ANGLE
        s.ball = Ball()
        s.p1 = Player(name1, s.w, paddleWidth)
        s.p2 = Player(name2, s.w, paddleWidth)

    #==== Public Methods ========================================

    def reset(s):
        """
        Reset the game to the start state
        1) Set paddle locations
        2) Set ball location
        3) Set random ball velocity

        Parameters
        ----------

        """
        s._resetBoard()
        s.p1.setScore(0)
        s.p2.setScore(0)

    def step(s,paddleMove1,paddleMove2):
        """
        Step the game
        1) Set the paddle locations
        2) Set ball location
        3) Check for collisions and update ball location
        4) Check and update score
        5) Check win condition

        Parameters
        ----------
        paddleMove1     right or left
        paddleMove2     right or left

        Returns
        -------
        Current scores tuple

        """
        s.p1.move(paddleMove1)
        s.p2.move(paddleMove2)
        s.ball.step()
        isScore = s._checkCollisions()

        if (isScore == s.SCORE_P1):
            s.p1.addScore()
            s._resetBoard()
        elif (isScore == s.SCORE_P2):
            s.p2.addScore()
            s._resetBoard()

        return (s.p1.score, s.p2.score)

    #==== Private Methods ======================================

    def _checkCollisions(s):

        s._checkWallBouce()

        # Check paddle collisions and scores
        if (s.ball.y < s.endZone):

            m = s.ball.vY / s.ball.vX
            dY = s.endZone - s.ball.y
            crossingPt = s.ball.x + dY/m

            if (s.p1.isPaddleHit(crossingPt)):
                s.ball.y += 2*dY

        elif ((s.h - s.ball.y) < s.endZone):

            m = s.ball.vY / s.ball.vX
            dY = s.endZone - (s.h - s.ball.y)
            crossingPt = s.ball.x - dY/m

            if (s.p1.isPaddleHit(crossingPt)):
                s.ball.y -= 2*dY

        # Check wall bounce again for corner case
        s._checkWallBouce()

    def _checkWallBounce(s):
        # If collision, flip velocity and lose no energy
        if (s.ball.x < 0):

            s.ball.x *= -1
            s.ball.vX *= -1

        elif (s.ball.x > s.w):

            s.ball.x += 2*(s.w - s.ball.x)
            s.ball.vX *= -1

    def _resetBoard(s):
        s.ball.setLoc(s.w/2, s.h/2)
        s.ball.setVel(s._rndBallVel(s.startVelAngle, s.startVelMag))
        s.p1.setLoc(s.w/2)
        s.p2.setLoc(s.w/2)

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
    
    def __init__(s):
        s.x = 0
        s.y = 0
        s.vX = 0
        s.vY = 0

    def setLoc(s,x,y):
        s.x = x
        s.y = y

    def setVel(s,v):
        s.vX = v[0]
        s.vY = v[1]

    def step(s):
        s.x += s.vX
        s.y += s.vY

#=====================================================
# Player
#=====================================================

class Player(object):
    N_PADDLE_STEPS = 20

    def __init__(s, name, boardWidth, paddleWidth):
        s.name = name
        s.boardWidth = boardWidth
        s.paddleWidth = paddleWidth
        s.paddleStep = boardWidth / 10
        s.paddleLoc = boardWidth / 2
        s.score = 0

    def setLoc(s, loc):
        s.paddleLoc = loc

    def move(s, paddleMove):
        if (paddleMove == PongGameModel.MV_RIGHT):
            
            edge = s.paddleLoc + s.paddleWidth/2
            if ((s.boardWidth - edge) > s.paddleStep):
                s.paddleLoc += s.paddleStep
        
        elif (paddleMove == PongGameModel.MV_LEFT):        
            
            edge = s.paddleLoc - s.paddleWidth/2
            if (edge > s.paddleStep):
                s.paddleLoc -= s.paddleStep

    def isPaddleHit(s, loc):
        right = s.paddleLoc + s.paddleWidth/2
        left  = s.paddleLoc - s.paddleWidth/2
        return (left <= loc) and (loc <= right)

    def addScore(s):
        s.score += 1

    def setScore(s, score):
        s.score = score
