from Instrument import Instrument
from mingus.containers.NoteContainer import NoteContainer
from random import random, randrange

class Strings(Instrument):

	def __init__(self, params):
		if 'midi_instr' not in params:
			params["midi_instr"] = randrange(49, 51)
		Instrument.__init__(self, params)

	def generate_note(self, state):
		wild = state['wild']
		if state["tick"] % state["resolution"] == 0 and \
				random() < 4.0 * wild:
			return NoteContainer(state["chord"])
		return None

