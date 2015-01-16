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

    WIDTH, HEIGHT = 480, 480
    PADDLE_W = 50
    PADDLE_H = 6
    END_ZONE = 30
    BALL_RADIUS = 10
    FPS = 50
    MAX_SCORE = 3
    GAME_OVER_DELAY = 180
    LEFT_BTN = 7
    RIGHT_BTN = 12

    def __init__(s):
        s.size = (s.WIDTH, s.HEIGHT)

        s.coms = Communications()
        s.btns = Buttons(s.LEFT_BTN, s.RIGHT_BTN)

        pg.init()
        # s.screen = pg.display.set_mode(s.size, pg.FULLSCREEN)
        s.screen = pg.display.set_mode(s.size)

        s.model = Model.PongGameModel('Player1', 'Player2', s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W,
                s.BALL_RADIUS)
        s.view = View.PongGameView(s.model, s.screen, s.WIDTH, s.HEIGHT, s.END_ZONE, s.PADDLE_W, s.PADDLE_H, 
                s.BALL_RADIUS)

        s.paused = False
        s.gameOver = False


    #==== Public Methods ========================================

    def run(s):
        s.coms.testMaster()

        clock = pg.time.Clock()

        while True:

            # Get moves
            mv = int(s.coms.readByte())
            cmds = s._handleEvts()
            score = s.model.step(cmds[0], mv)
            
            if max(score) == s.MAX_SCORE:
                
                # Game over start
                s.view.gameOver()
                s.gameOver = s.GAME_OVER_DELAY

            elif s.gameOver > 0:

                # Cont game over
                s.view.gameOver()

            else:

                # Playing
                s.view.show()
                clock.tick(s.FPS)

            gameState = s._packageGameState();

            # Send state to remote
            s.coms.writeGameState(gameState)

            if s.gameOver > 0:
                s.gameOver -= 1
                s.model.reset()

       
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
        res = s.model.MV_STAY
        mv = s.btns.getMove()

        if mv == Buttons.RIGHT:
            res = s.model.MV_RIGHT
        elif mv == Buttons.LEFT:
            res = s.model.MV_LEFT

        return res

    def _packageGameState(s):
        gameState = {}
        gameState['paddle1'] = s.model.p1.paddleLoc
        gameState['paddle2'] = s.model.p2.paddleLoc
        gameState['score1'] = s.model.p1.score
        gameState['score2'] = s.model.p2.score
        gameState['ballX'] = s.model.ball.x
        gameState['ballY'] = s.model.ball.y
        if s.gameOver:
            gameState['gameOver'] = 1
        else:
            gameState['gameOver'] = 0
        return gameState

    def _quit(s):
        pg.display.quit()
        sys.exit()

class PongSlave(PongMaster):
    
    def __init__(s):
        PongMaster.__init__(s)

    def run(s):
        s.coms.testSlave()

        clock = pg.time.Clock()

        while True:
            # Send button presses
            s.coms.writeByte(s._getBtns())

            gameState = s.coms.readGameState()

            # Playing
            s.model.set(gameState['paddle1'], gameState['paddle2'],
                gameState['score1'], gameState['score2'], (gameState['ballX'], gameState['ballY']))

            if gameState['gameOver'] == 1:
                s.view.gameOver()
            else:
                s.view.show()

            clock.tick(s.FPS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--master', dest='isMaster', action='store_true')
    parser.add_argument('--slave', dest='isMaster', action='store_false')
    parser.set_defaults(isMaster=True)
    args = parser.parse_args()

    if args.isMaster:
        print 'Starting MASTER'
        pong = PongMaster()
    else:
        print 'Starting SLAVE'
        pong = PongSlave()
    pong.run()