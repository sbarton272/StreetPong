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
import sys, argparse
import Pong.PongGameModel as Model
import Pong.PongGameView as View
from Buttons import Buttons
from Communications import Communications

#=====================================================
# Pong
#=====================================================

class PongMaster(object):

    # TODO pausing/timeout if no input
    # TODO better graphics
    # TODO AI when in resting mode
    # TODO correct screen size
    # TODO ball goes over endline
    # TODO larger paddles
    # TODO ball speed-up

    def __init__(s):
        s.WIDTH = 480
        s.HEIGHT = 480
        s.PADDLE_W = 50
        s.PADDLE_H = 6
        s.END_ZONE = 30
        s.BALL_RADIUS = 10
        s.FPS = 50
        s.MAX_SCORE = 3
        s.GAME_OVER_DELAY = 4800
        s.LEFT_BTN = 7
        s.RIGHT_BTN = 12

        s.size = (s.WIDTH, s.HEIGHT)

        s.btns = Buttons(s.LEFT_BTN, s.RIGHT_BTN)
        s.coms = Communications()

        pg.init()
        # s.screen = pg.display.set_mode(s.size, pg.FULLSCREEN)
        s.screen = pg.display.set_mode(s.size)

        s.model = Model.PongGameModel('Player1', 'Player2', s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W,
                s.BALL_RADIUS)
        s.view = View.PongGameView(s.model, s.screen, s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W, s.PADDLE_H, 
                s.BALL_RADIUS)

        s.paused = False

    #==== Public Methods ========================================

    def run(s):
        clock = pg.time.Clock()

        while True:

            # Get moves
            mv = s.coms.readByte()
            cmds = s._handleEvts()
            score = s.model.step(cmds[0], mv)
            
            if max(score) == s.MAX_SCORE:
                
                # Game over
                s.view.gameOver()
                s.model.reset()

            elif s.paused:

                # Paused
                pass

            else:
                
                # Playing
                s.view.show()
                clock.tick(s.FPS)

            gameState = s._packageGameState();

            # Send state to remote
            s.coms.writeDict(gameState)

            if gameState['gameOver']:
                pg.time.wait(s.GAME_OVER_DELAY)

       
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

    def _getBtns(s):
        res = s.MV_STAY
        mv = s.btns.getMove()

        if mv == Buttons.RIGHT:
            res = s.MV_RIGHT
        elif mv == Buttons.LEFT:
            res = s.MV_LEFT

        return res

    def _packageGameState(s):
        gameState = {}
        gameState['paddle1'] = s.model.p1.paddleLoc
        gameState['paddle2'] = s.model.p2.paddleLoc
        gameState['score1'] = s.model.p1.score
        gameState['score2'] = s.model.p2.score
        gameState['ball'] = (s.model.ball.x, s.model.ball.y)
        return gameState

    def _quit(s):
        pg.display.quit()
        sys.exit()

class PongSlave(PongMaster):
    
    def __init__(s):
        PongMaster.__init__(s)

    def run(s):

        clock = pg.time.Clock()

        while True:
            # Send button presses
            s.coms.writeByte(s._getBtns())

            gameState = s.coms.readDict()

            # Playing
            s.model.set(gameState['paddle1'], gameState['paddle2'],
                gameState['score1'], gameState['score2'], gameState['ball'])

            if gameState['gameOver']:
                s.view.gameOver()
            else:
                s.view.show()

            clock.tick(s.FPS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--master', nargs='?', help='specify master')
    args = parser.parse_args()

    if args.master:
        print 'Starting MASTER'
        pong = PongMaster()
    else:
        print 'Starting SLAVE'
        pong = PongSlave()
    pong.run()