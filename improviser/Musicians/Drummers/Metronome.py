from Drum import Drum
from mingus.containers.Note import Note

class Metronome(Drum):

	def generate_note(self, state):
		if state["resolution"] > 4:
			step = state["resolution"] / 4

			if state["tick"] % step == 0:
				i = state["tick"] / step


		else:
			i = state["tick"]

		if i % 2 == 0:
			return [Note("E", 5)]
		else:
			return [Note("F", 5)]

	def generate_velocity(self, state):
		if state["resolution"] > 4:
			step = state["resolution"] / 4
			if state["tick"] % step == 0:
				i = state["tick"] / step
				
			else:
				return 0
		elif state["resolution"] < 4:
			i = state["tick"] * state["resolution"]
		else:
			i = state["tick"]

		if i == 0:
			return 120
		elif i == 1:
			return 80
		elif i == 2:
			return 110
		elif i == 3:
			return 90
		return 0



			

