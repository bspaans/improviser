import Movement
from random import choice

class RandomProgressionMovement(Movement.Movement):
	"""Randomizes progression order."""

	def get_prog(self):
		return choice(self.progressions)
