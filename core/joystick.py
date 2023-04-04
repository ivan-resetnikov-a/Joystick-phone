import pygame as pg

from math import sin, cos, dist, atan2



class Joystick :
	def __init__ (self, pos) :
		self.offset = [0, 0]

		self.pos = pos


	def render (self, window) :
		self.offset = [0, 0]

		mouse = pg.mouse.get_pos()
		distance = dist(self.pos, mouse)

		if pg.mouse.get_pressed()[0] and distance < 150:

			distance = pg.math.clamp(distance, 0, 75)

			deg = atan2(
				self.pos[0] - mouse[0],
				self.pos[1] - mouse[1]) - 1.37

			self.offset = [
				cos(deg) * -distance,
				sin(deg) * distance
			]

		pg.draw.circle(window, (255, 255, 255), self.pos, 75, 3)
		pg.draw.circle(window, (255, 255, 255), (self.pos[0] + self.offset[0], self.pos[1] + self.offset[1]), 10, 0)

		pg.draw.circle(window, (100, 100, 100), self.pos, 150, 1)