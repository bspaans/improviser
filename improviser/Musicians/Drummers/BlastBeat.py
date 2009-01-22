from Drum import Drum
from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.Note import Note
from random import choice, random

class BlastBeat(Drum):


	def __init__(self, params):
		self.last_tom = Note("C", 10)
		self.play_toms = True
		Drum.__init__(self, params)

	def generate_note(self, state):

		n = []
		if state["tick"] % 2 == 0:
			n += self.bass()
			if state["iteration_tick"] == 0:
				n += self.crash()
			else:
				n += self.hihat_closed()
		else:
			n = self.snare()

		if state["iteration_tick"] / float(state["ticks"] * \
			len(state["chords"])) > 0.75:
			if random() > 0.5:
				self.play_toms = True
			elif random() > 0.8:
				self.play_toms = False
		else:
			self.play_toms= False

		if self.play_toms:
			t = Note("C", -1)
			if Note("C", -1) == self.last_tom:
				t = choice([self.highest_tom(), self.high_tom()])
			elif self.last_tom == Note("D", 3):
				t = choice([self.highest_tom(), self.high_tom()])
			elif self.last_tom == Note("C", 3):
				t = choice([self.middle_tom(), self.high_tom(), self.highest_tom(), self.high_tom()])
			elif self.last_tom == Note("B", 2):
				t = choice([self.middle_tom(), self.low_tom(), self.lower_tom(), self.high_tom()])
			elif self.last_tom == Note("A", 2):
				t = choice([self.middle_tom(), self.low_tom(), self.lower_tom()])
			elif self.last_tom == Note("G", 2):
				t = choice([self.lower_tom(), self.low_tom(), self.lowest_tom()])
			elif self.last_tom == Note("F", 2):
				t = choice([self.lower_tom(), self.lowest_tom()])


			
			n += [t]
			self.last_tom = t
				
		else:
			self.last_tom = Note('C', -1)
		return NoteContainer(n)

