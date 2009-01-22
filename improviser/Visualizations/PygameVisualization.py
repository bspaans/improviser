from Visualization import Visualization
from os import sys
try:
	import pygame
	from pygame.locals import *
except:
	print "Couldn't load the pygame library."
	print "A download is available at http://www.pygame.org"
	sys.exit(1)

class PygameVisualization(Visualization):
	"""Visualizations using pygame should subclass this class and """
	"""implement their own paint_screen(). refresh_rects should be set """
	"""to set the rectangles that need to be refreshed. See the pygame docs """
	"""for display.update() if unsure."""

	def __init__(self, width, height):
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Improviser")
		
		self.raster = pygame.Surface((width, height))
		self.raster.fill((255,255,255))

		self.width = width
		self.height = height
		self.refresh_rects = [pygame.Rect((0, 0, width, height))]



	def paint_screen(self, notes, channel):
		pass




	def refresh_screen(self):
		self.screen.blit(self.raster, (0,0))
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
			elif event.type == QUIT:
				sys.exit()



	def update_screen(self):
		pygame.display.update(self.refresh_rects)
		self.refresh_rects = []
