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

    # TODO pausing/timeout
    # TODO better graphics
    # TODO AI when in resting mode
    # TODO full screen
    # TODO ball goes over endline

    WIDTH, HEIGHT = 480, 480
    PADDLE_W = 50
    PADDLE_H = 6
    END_ZONE = 30
    BALL_RADIUS = 10
    FPS = 50
    MAX_SCORE = 3
    GAME_OVER_DELAY = 4800

    def __init__(s):
        s.size = (s.WIDTH, s.HEIGHT)

        pg.init()
        s.screen = pg.display.set_mode(s.size, pg.FULLSCREEN)
        # s.screen = pg.display.set_mode(s.size)

        s.model = Model.PongGameModel('Player1', 'Player2', s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W,
                s.BALL_RADIUS)
        s.view = View.PongGameView(s.model, s.screen, s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W, s.PADDLE_H, 
                s.BALL_RADIUS)

    #==== Public Methods ========================================

    def run(s):
        clock = pg.time.Clock()

        while True:
            cmds = s._handleEvts()

            score = s.model.step(cmds[0], cmds[1])
            
            if max(score) == s.MAX_SCORE:
                s.view.gameOver()
                s.model.reset()
                pg.time.wait(s.GAME_OVER_DELAY)
            else:
                s.view.show()
                clock.tick(s.FPS)
       
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
        elif pressed[pg.K_q]:
            s._quit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                s._quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    s._quit()

        return (move1, move2)

    def _quit(s):
        pg.display.quit()
        sys.exit()


if __name__ == '__main__':
    pong = Pong()
    pong.run()
