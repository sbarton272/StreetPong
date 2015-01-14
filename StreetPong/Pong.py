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
import Pong.PongGameModel as Model
import Pong.PongGameView as View
#=====================================================
# Pong
#=====================================================

class Pong(object):

    WIDTH, HEIGHT = 480, 480
    PADDLE_W = 200
    PADDLE_H = 6
    END_ZONE = 30
    BALL_RADIUS = 10
    FPS = 20

    def __init__(s):
        s.size = (s.WIDTH, s.HEIGHT)

        pg.init()
        s.screen = pg.display.set_mode(s.size)

        s.model = Model.PongGameModel('Player1', 'Player2', s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W,
                s.BALL_RADIUS)
        s.view = View.PongGameView(s.model, s.screen, s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W, s.PADDLE_H, 
                s.BALL_RADIUS)

    #==== Public Methods ========================================

    def run(s):
        clock = pg.time.Clock()

        while True:
            cmds = s._handleEvts()

            s.model.step(cmds[0], cmds[1])
            s.view.show()
            print s.model.ball.x, s.model.ball.y,
            print s.model.ball.vX, s.model.ball.vY

            clock.tick(s.FPS)

            # TODO pause behavior
       
    def _handleEvts(s):
        move1 = s.model.MV_STAY
        move2 = s.model.MV_STAY

        pressed = pg.key.get_pressed()
        if pressed[pg.K_a]:
            move1 = s.model.MV_LEFT
        elif pressed[pg.K_d]:
            move1 = s.model.MV_RIGHT
        elif pressed[pg.K_j]:
            move2 = s.model.MV_LEFT
        elif pressed[pg.K_l]:
            move2 = s.model.MV_RIGHT

        for event in pg.event.get():
            if event.type == pg.QUIT:
                # TODO end game behavior
                sys.exit()

        return (move1, move2)

if __name__ == '__main__':
    pong = Pong()
    pong.run()