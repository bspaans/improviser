from Drum import Drum
from random import random

class Bongo(Drum):

	def generate_note(self, state):

		if state["tick"] % (state["resolution"] / 2) == 0:
			return [self.high_bongo()]
		if random() < (state["wild"] / 3):
			return [self.low_bongo()]
		elif random() < (state["wild"] / 6):
			return [self.high_bongo()]



