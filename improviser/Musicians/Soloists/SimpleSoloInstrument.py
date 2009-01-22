from Instrument import Instrument
from mingus.containers.Note import Note
from random import choice

class SimpleSoloInstrument(Instrument):

	def __init__(self, params):
		Instrument.__init__(self, params)

	def generate_note(self, state):
		return [Note(choice(state["chord"]))]

