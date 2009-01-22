from Instrument import Instrument
from mingus.containers.Note import Note
from mingus.core import notes
from random import choice, random, randrange

class BassInstrument(Instrument):

	def __init__(self, params):
		if 'midi_instr' not in params:
			params["midi_instr"] = randrange(33, 40)
		Instrument.__init__(self, params)

	def generate_note(self, state):
		wild = 1.0
		if 'wild' in state:
			wild = state['wild']

		if state["tick"] % (state["resolution"] / 4.0) == 0 and \
				random() < 1.0 * wild:
			n = Note(choice(state["chord"]))
			while n > Note("E", 3):
				if n.octave >= 3:
					n.octave_down()
				else:
					break
			return [n]
		elif state["resolution"] > 4 and state["tick"] % \
			(state["resolution"] / 4.0) == \
			state["resolution"] / 8 and \
			random() < 0.2 * wild:
			
			n = Note(choice(state["chord"]))
			while n > Note("E", 3):
				if n.octave >= 3:
					n.octave_down()
				else:
					break
			n.name = notes.diminish(n.name)
			return [n]
