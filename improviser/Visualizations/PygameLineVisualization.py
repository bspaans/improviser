from PygameVisualization import PygameVisualization
import pygame
from pygame.locals import *
from random import randrange as r
from mingus.core import notes

class PygameLineVisualization(PygameVisualization):

	def __init__(self, width, height):
		PygameVisualization.__init__(self, width, height)
		pygame.font.init()
		f = pygame.font.SysFont("monospace", width / 30)
		self.offsety = height % 24 / 2
		self.offsetx = width % 16 / 2 
		self.radius = height / 24 
		self.chanw = width / 32

		no = []
		for n in range(12):
			no.append(f.render(notes.int_to_note(n), 
				False, (169,169,169)))

		for x in range(17):
			if x % 2:
				pygame.draw.rect(self.raster, (230,230,230), 
					(x * self.chanw  * 2+ self.offsetx, 0, 
					self.chanw * 2, height))
		
		for x in range(17):
			pygame.draw.line(self.raster, (210,210,210),
				(x * self.chanw * 2 + self.offsetx ,0),
				(x * self.chanw * 2 + self.offsetx, height))
			for y in range(13):
				pygame.draw.line(self.raster, (200,200,200),
					(self.offsetx, y * self.radius * 2 + self.offsety), 
					(width - self.offsetx , y * self.radius * 2 + self.offsety))
				if y < 12:
					self.raster.blit(no[y], (x * self.chanw * 2 + self.chanw / 2 + self.offsetx, 
						y * self.radius * 2 + self.radius))




	def paint_screen(self, notes, channel):
		for note in notes:
			n = int(note) % 12
			x = self.chanw * 2 * channel - self.chanw+ self.offsetx
			y = n * self.radius * 2 + self.radius + self.offsety
			c = r(0,150) + 75
			pygame.draw.circle(self.screen, (c,c,c),
					(x, y), min(self.radius, self.chanw) - 1)
		self.refresh_rects.append(pygame.Rect((0,0,self.width, self.height)))
