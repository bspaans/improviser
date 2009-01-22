from Drum import Drum
from random import random, choice

class Toms(Drum):


	def generate_note(self, state):

		if random() < state["wild"]:
			return [choice([self.lowest_tom, self.lower_tom, self.low_tom, 
				self.middle_tom, self.high_tom, self.highest_tom])()]
