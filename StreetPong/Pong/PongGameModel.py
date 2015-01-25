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
# PongGame
#=====================================================

class PongGameModel(object):
    MV_STAY = 0
    MV_RIGHT = 1
    MV_LEFT  = 2
    SCORE_NONE = 0
    SCORE_P1 = 1
    SCORE_P2 = 2
    STARTING_VEL_ANGLE = 30
    STARTING_VEL_MAG = 15
    VEL_INC = 1;

    """
    PongGame model for paddles and ball dynamics and control

    Parameters
    ----------

    """
    def __init__(s, name1, name2, windowW, windowH, endZone, paddleWidth,
            ballRadius):
        s.w = windowW
        s.h = windowH
        s.endZone = endZone
        s.size = (s.w, s.h)
        s.ball = Ball(ballRadius)
        s.p1 = Player(name1, s.w, paddleWidth)
        s.p2 = Player(name2, s.w, paddleWidth)
        s.players = {name1: s.p1, name2: s.p2}

        s.reset()

    #==== Public Methods ========================================

    def reset(s):
        s._resetBoard()
        s.p1.setScore(0)
        s.p2.setScore(0)

    def step(s,paddleMove1,paddleMove2):
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

        return s.getScore()

    def set(s, paddle1, paddle2, score1, score2, ball):
        s.p1.setLoc(paddle1)
        s.p2.setLoc(paddle2)
        s.p1.setScore(score1)
        s.p2.setScore(score2)
        s.ball.setLoc(ball[0],ball[1])

    def getScore(s):
        return (s.p1.score, s.p2.score)

    def getPlayer(s, name):
        return s.players.get(name, None)

    #==== Private Methods ======================================

    def _checkCollisions(s):

        rsp = s.SCORE_NONE

        s._checkWallBounce()

        # Check paddle collisions and scores
        if (s.ball.bottom() < s.endZone):

            m = s.ball.vX / s.ball.vY
            dY = s.endZone - s.ball.bottom()
            crossingPt = s.ball.x + dY*m

            if (s.p1.isPaddleHit(crossingPt)):
                s.ball.y += 2*dY
                s.ball.vY *= -1 
                s.ball.vY += s.VEL_INC
            else:
                rsp = s.SCORE_P1

        elif (s.ball.top() > (s.h - s.endZone)):

            m = s.ball.vX / s.ball.vY
            dY = s.ball.top() - (s.h - s.endZone)
            crossingPt = s.ball.x + dY*m

            if (s.p2.isPaddleHit(crossingPt)):
                s.ball.y -= 2*dY
                s.ball.vY *= -1
                s.ball.vY -= s.VEL_INC
            else:
                rsp = s.SCORE_P2

        # Check wall bounce again for corner case
        s._checkWallBounce()

        return rsp

    def _checkWallBounce(s):

        # If collision, flip velocity and lose no energy
        if (s.ball.left() < 0):

            s.ball.x = s.ball.x - 2*s.ball.left()
            s.ball.vX *= -1

        elif (s.ball.right() > s.w):

            s.ball.x = s.ball.x + 2*(s.w - s.ball.right())
            s.ball.vX *= -1

    def _resetBoard(s):
        s.ball.setLoc(s.w/2, s.h/2)
        s.ball.setVel(s._rndBallVel(s.STARTING_VEL_ANGLE/2,
                s.STARTING_VEL_ANGLE, s.STARTING_VEL_MAG))
        s.p1.setLoc(s.w/2)
        s.p2.setLoc(s.w/2)

    def _rndBallVel(s, minAngle, maxAngle, mag):
        angle = rnd.uniform(minAngle,maxAngle)
        x = math.sin(math.radians(angle))
        y = 1 - x*x

        # Randomly determine up or down/right or left
        x = x * rnd.sample([-1,1], 1)[0]
        y = y * rnd.sample([-1,1], 1)[0]
        
        return (int(x*mag), int(y*mag))

#=====================================================
# Ball
#=====================================================

class Ball(object):
    
    def __init__(s, radius):
        s.x = 0
        s.y = 0
        s.vX = 0
        s.vY = 0
        s.radius = radius

    def setLoc(s,x,y):
        s.x = x
        s.y = y

    def setVel(s,v):
        s.vX = v[0]
        s.vY = v[1]

    def step(s):
        s.x += s.vX
        s.y += s.vY

    def left(s):
        return s.x - s.radius

    def right(s):
        return s.x + s.radius

    def bottom(s):
        return s.y - s.radius

    def top(s):
        return s.y + s.radius

#=====================================================
# Player
#=====================================================

class Player(object):
    N_PADDLE_STEPS = 50

    def __init__(s, name, boardWidth, paddleWidth):
        s.name = name
        s.boardWidth = boardWidth
        s.paddleWidth = paddleWidth
        s.paddleStep = boardWidth / s.N_PADDLE_STEPS
        s.paddleLoc = boardWidth / 2
        s.score = 0

    def setLoc(s, loc):
        s.paddleLoc = loc

    def move(s, paddleMove):
        if (paddleMove == PongGameModel.MV_RIGHT):
            
            edge = s.paddleLoc + s.paddleWidth/2
            diff = s.boardWidth - edge
            if (diff > s.paddleStep):
                s.paddleLoc += s.paddleStep
            else:
                s.paddleLoc += diff
        
        elif (paddleMove == PongGameModel.MV_LEFT):        
            
            edge = s.paddleLoc - s.paddleWidth/2
            if (edge > s.paddleStep):
                s.paddleLoc -= s.paddleStep
            else:
                s.paddleLoc -= edge

    def isPaddleHit(s, loc):
        right = s.paddleLoc + s.paddleWidth/2
        left  = s.paddleLoc - s.paddleWidth/2
        return (left <= loc) and (loc <= right)

    def addScore(s):
        s.score += 1

    def setScore(s, score):
        s.score = score
