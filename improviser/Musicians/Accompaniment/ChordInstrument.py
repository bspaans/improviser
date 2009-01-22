from Instrument import Instrument
from mingus.containers.NoteContainer import NoteContainer
from random import random, randrange

class ChordInstrument(Instrument):

	def __init__(self, params):
		Instrument.__init__(self, params)

	def generate_note(self, state):
		chance = 0.05
		wild = 1.0

		if 'chance' in self.params:
			chance = self.params["chance"]
		if 'wild' in state:
			wild = state['wild']

		if random() < chance * wild:
			return NoteContainer(state["chord"])
		else:
			return None


