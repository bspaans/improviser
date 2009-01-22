from Drum import Drum
from random import random

class Conga(Drum):

	def generate_note(self, state):

		if state["tick"] % (state["resolution"] / 4) == 0:
			return [self.low_conga()]

		if random() < (state["wild"] / 3):
			return [self.mute_high_conga()]
		elif random() < (state["wild"] / 6):
			return [self.open_high_conga()]
