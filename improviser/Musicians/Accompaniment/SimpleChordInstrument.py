from Instrument import Instrument
from mingus.containers.NoteContainer import NoteContainer
from random import random

class SimpleChordInstrument(Instrument):

	def generate_note(self, state):
		wild = state['wild']

		if state["tick"] % state["resolution"] == 0 and \
				random() < 1.0 * wild:
			return NoteContainer(state["chord"])
		else:
			return None

