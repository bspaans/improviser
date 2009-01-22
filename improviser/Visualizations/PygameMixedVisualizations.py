from PygameVisualization import PygameVisualization
from PygameBlockVisualization import PygameBlockVisualization
from PygameLineVisualization import PygameLineVisualization
from random import random
import pygame


class PygameMixedVisualizations(PygameVisualization):


 	def __init__(self, width, height):
		PygameVisualization.__init__(self, width, height)
		self.blocks = PygameBlockVisualization(width, height)
		self.lines = PygameLineVisualization(width, height)
		self.current = self.lines

	def paint_screen(self, notes, channel):
		if random() > 0.5:
			if random() > 0.95:
				self.current = self.blocks
			elif random() > 0.95:
				self.current = self.lines
			self.current.refresh_screen()

		self.current.paint_screen(notes, channel)
		

	def refresh_screen(self):
		self.current.refresh_screen()

	def update_screen(self):
		pygame.display.update()
