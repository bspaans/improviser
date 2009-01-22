from Drum import Drum
from random import random

class DanceBeat(Drum):

	def generate_note(self, state):

		r = []

		if state["iteration_tick"] == 0:
			if random() < state["wild"]:
				r += self.crash()
			
		if state["wild"] > 0.25:
			if state["tick"] % (state["resolution"] / 4) == 0:
				r += self.bass()

		if state["wild"] > 0.5:
			if state["tick"] % (state["resolution"] / 4) == (state["resolution"] / 8):
				r += self.hihat_opened()
			elif random() < state["wild"]:
				r += self.hihat_closed()

		if state["wild"] > 0.75:
			if state["tick"] % (state["resolution"] / 2) == 0 and state["tick"] != 0:
				r += self.clap()


		return r
