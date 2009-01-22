from Instrument import Instrument
from random import random, randrange
from mingus.containers.Note import Note
from mingus.core import notes

class RandomSoloist(Instrument):


	def generate_note(self, state):
		if random() < state["wild"]:
			note = notes.int_to_note(randrange(0, 12))
			octave = randrange(2, 7)
			return [Note(note, octave)]
		else:
			return None


