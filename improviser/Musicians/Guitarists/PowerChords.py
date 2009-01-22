from Instrument import Instrument
from mingus.containers.NoteContainer import NoteContainer
from mingus.core.intervals import perfect_fifth

class PowerChords(Instrument):

	def generate_note(self, state):
		n = state["chord"][0]
		n = [n, perfect_fifth(n)]
		n =  NoteContainer(n)
		for i in n:
			i.octave_down()
		return n
