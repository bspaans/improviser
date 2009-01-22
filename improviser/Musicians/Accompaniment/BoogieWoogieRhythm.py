from mingus.core.intervals import perfect_fifth, major_sixth
from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.Note import Note
from Instrument import Instrument
from random import random

class BoogieWoogieRhythm(Instrument):

	def generate_note(self, state):

		chance = 0.95

		n = [Note(state["chord"][0])]

		if state["tick"] < state["ticks"] / 4 or \
			state["tick"] >= state["ticks"] / 2 and\
			state["tick"] < state["ticks"] / 4 * 3:
			n += [Note(perfect_fifth(n[0].name))]
		else:
			n += [Note(major_sixth(n[0].name))]

		n[0].octave_down()
		n[1].octave_down()

		if random() < chance:
			return NoteContainer(n)
		else:
			return None
		
