from Block import Block
from improviser.Progressions import *
from mingus.core import progressions
from random import random, choice

class DoubleTimeBlock(Block):
	double_time = True

	def get_resolution(self, iteration):
		i = iteration % (self.progressions[-1][0] - self.progressions[0][0])
		if i == 0:
			if self.double_time:
				self.double_time = False
				self.resolution *= 2
			else:
				self.double_time = True
				self.resolution /= 2
		return self.resolution
