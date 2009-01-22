from PygameVisualization import PygameVisualization
from random import randrange
import pygame
from pygame.locals import *


class PygameBlockVisualization(PygameVisualization):

	def __init__(self, width, height):
		PygameVisualization.__init__(self, width, height)
		for x in range(5):
			pygame.draw.line(self.raster, (10,10,10), \
					(x * (width / 4), 0), \
					(x * (width / 4), height))
			pygame.draw.line(self.raster, (10,10,10), \
					(0, x * (height / 4)), \
					(width, x * (height / 4)))
		self.chanx_dict = {}
		self.chany_dict = {}
		for x in range(16):
			self.chanx_dict[x] = width / 4 * (x % 4) + 1
			self.chany_dict[x] = height /4 * (x / 4) + 1

		self.notex_dict = {}
		self.notey_dict = {}
		for x in range(128):
			self.notex_dict[x] = width / 48 * x % 12
			self.notey_dict[x] = height / 48 * (x / 12)

		self.bw = width / 48
		self.bh = height / 48
		self.chanw = width / 4
		self.chanh = height / 4


	def paint_screen(self, notes, channel):
		chanx = self.chanx_dict[channel]
		chany = self.chany_dict[channel]

		r = randrange
		chanc = (r(200,255), r(200,255), r(200,255))

		pygame.draw.rect(self.screen, chanc, (chanx, chany, \
				self.chanw -1, self.chanh - 1))

		for note in notes:

			bx = self.notex_dict[int(note)] + chanx
			by = self.notey_dict[int(note)] + chany
			bc = (255,0,0)
		
			pygame.draw.rect(self.screen, bc, (bx, by, \
					self.bw, self.bh))
		self.refresh_rects.append(pygame.Rect((chanx, chany, \
				self.chanw - 1, self.chanh - 1)))
