from Instrument import Instrument
from mingus.core import chords
from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer
from random import random, randrange


class FastStridePianist(Instrument):

	def __init__(self, params):
		if 'let_ring' not in params:
			params["let_ring"] = True
		if 'channel' not in params:
			params["channel"] = 1
		if 'midi_instr' not in params:
			params["midi_instr"] = randrange(1, 9)
		Instrument.__init__(self, params)

	def generate_note(self, state):

		if state["tick"] % (state["resolution"] / 2.0) == 0 \
				and random() < 5.0 * state["wild"]:
			if random() > 0.1:
				n = Note(state["chord"][0])
			else:
				if len(state["chord"]) == 1:
					n = Note(state["chord"][0])
				if len(state["chord"]) == 2:
					n = Note(state["chord"][1])
				else:
					n = Note(state["chord"][2])
			n.octave_down()
			return [n]
		
		if state["tick"] % (state["resolution"] / 2.0) == \
				state["resolution"] / 4 \
				and random() < 5.0 *state["wild"]:
			c = state["chord"]

			for i in range(len(state["chord"])):
				if random() < 0.3 * state["wild"]:
					c = chords.invert(c)

			n = NoteContainer(c)

			return n
		return None
