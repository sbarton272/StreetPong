
import pygame as pg

class PongAI(object):

	def __init__(s, model, player):
		s.model = model
		s.player = player

	def getMove(s):

		ballX = s.model.ball.x
		paddleX = s.model.getPlayer(s.player).paddleLoc
		paddleWidth = s.model.getPlayer(s.player).paddleWidth/3
		diff = paddleX - ballX

		move = s.model.MV_STAY
		if abs(diff) < (paddleWidth):
			move = s.model.MV_STAY
		elif diff > (paddleWidth):
			move = s.model.MV_LEFT
		elif diff < -(paddleWidth):
			move = s.model.MV_RIGHT

		return move