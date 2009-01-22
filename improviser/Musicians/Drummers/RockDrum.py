from Drum import Drum
from random import random 

class RockDrum(Drum):

	def generate_note(self, state):
		n = []
		t = state["tick"] % state["resolution"]
		if state["tick"] > 0:
			if (t == state["resolution"] / 2 or \
			    t == state["resolution"] / 4 * 3) and \
			    random() < 0.3 * state["wild"]:

				n += self.hihat_opened()
			else:
				n += self.hihat_closed()

		if state["iteration_tick"] == 0 and random() < state["wild"]:
			n += self.crash()
			n += self.bass()
		elif t == 0 and random() < state["wild"]:
			n += self.bass()

		snare_scalar = 0.5
		if state["meter"][0] in [4, 8]:
			snare_scalar = 0.5
		elif state["meter"][0] in [3, 6]:
			snare_scalar = 0.66

		if state["tick"] == int(round(snare_scalar * state["ticks"])):
			n += self.snare()
		elif random() > 0.95:
			n += self.snare()

		return n
