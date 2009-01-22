from Block import Block
from random import random

class RandomWildnessBlock(Block):

	def get_wildness(self, iteration, tick):
		return random() * self.wildness
