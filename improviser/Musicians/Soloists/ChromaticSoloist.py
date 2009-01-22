from Instrument import Instrument
from mingus.containers.Note import Note
from mingus.core import notes
from random import choice, random

class ChromaticSoloist(Instrument):

	last_note = ''
	note_length = 1
	up = True

	def generate_note(self, state):
		wild = state['wild']

		if self.last_note == '':
			n = choice(state["chord"])
		else:
			if self.up:
				n = notes.augment(self.last_note)
			else:
				n = notes.diminish(self.last_note)
			
		self.last_note = n
		if random() < 0.20:
			self.up = not(self.up)

		if random() < 0.3 * wild:
			self.params["let_ring"] = False
			return [Note(n)]
		elif random() < 0.15 * wild and state["tick"] % 2 == 0:
			self.params["let_ring"] = True
			return [Note(self.last_note)]
		elif random() < 0.1 * wild:
			self.params["let_ring"] = True
			c = choice(state["chord"])
			self.last_note = c
			return [Note(c)]
		else:
			if random() > 0.05:
				self.params['let_ring'] = True
			else:
				self.params['let_ring'] = False
			return None
