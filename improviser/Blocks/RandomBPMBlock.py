from Block import Block
from random import randrange


class RandomBPMBlock(Block):

	def get_bpm(self, iteration, tick):
		return randrange(80,180)
