from Instrument import Instrument
from mingus.containers.Note import Note

class Drum(Instrument):

	def __init__(self, params):
		params["channel"] = 9
		Instrument.__init__(self, params)

	def acoustic_bass(self):
		return [Note("B", 2)]

	def bass(self):
		return [Note("C", 2)]

	def crash(self):
		return [Note("C#", 3)]

	def clap(self):
		return [Note("D#", 2)]

	def hihat_closed(self):
		return [Note("G#", 2)]

	def hihat_opened(self):
		return [Note("A#", 2)]

	def ride(self):
		return [Note("B", 3)]

	def snare(self):
		return [Note("E", 2)]

	def electric_snare(self):
		return snare

	def acoustic_snare(Self):
		return [Note("D", 2)]

	def lowest_tom(self):
		return Note("F", 2)

	def lower_tom(self):
		return Note("G", 2)

	def low_tom(self):
		return Note("A", 2)

	def middle_tom(self):
		return Note("B", 2)

	def high_tom(self):
		return Note("C", 3)

	def highest_tom(self):
		return Note("D", 3)

	def high_bongo(self):
		return Note("C", 4)

	def low_bongo(self):
		return Note("C#", 4)

	def mute_high_conga(self):
		return Note("D", 4)

	def open_high_conga(self):
		return Note("D#", 4)

	def low_conga(self):
		return Note("E", 4)
