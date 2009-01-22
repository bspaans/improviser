import Movement
from random import choice

class RandomBlockMovement(Movement.Movement):
	"""Randomizes block order."""

	def get_block(self):
		return choice(self.blocks)
