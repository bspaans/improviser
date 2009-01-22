from BassInstrument import BassInstrument
from mingus.containers.Note import Note
from mingus.core import notes
from random import choice, random, randrange

class WalkingBass(BassInstrument):

	last = Note('C', -1)
	first = Note('C', -1)
	chord = []
	octave = 1

	def __init__(self, params):
		if 'midi_instr' not in params:
			params["midi_instr"] = 27
		BassInstrument.__init__(self, params)

	def generate_note(self, state):

		wild = 1.0
		if 'wild' in state:
			wild = state['wild']

		if state["tick"] % (state["resolution"] / 4.0) == 0:
			p = state["tick"] / (state["resolution"] \
				/ 4.0)
			if self.last == Note('C', -1):
				n = Note(choice(state["chord"]), self.octave)
				if n != self.first:
					self.last = n
					self.first = n
				else:
					n = Note(choice(state["chord"].remove(n.name)), self.octave)
			else:
				if p == 0:
					i = notes.augment(self.last.name)
					if i in state["chord"]:
						self.augment()
						self.first = Note(self.last.name, self.octave)
					else:
						self.last = Note(choice(state["chord"]), self.octave)
						self.first = Note(self.last.name, self.octave)
				elif p == 1:
					if random() > 0.5:
						self.augment()
					elif random() > 0.5:
						self.diminish()
					else:
						self.last = Note(choice(state["chord"]), self.octave)

				elif p == 2:
					i= notes.augment(self.last.name)
					j= notes.diminish(self.last.name)
					ni = Note(i, self.octave)
					nj = Note(j, self.octave)

					if i in state["chord"] and random() > 0.6 and ni != self.first:
						self.augment()
					elif j in state["chord"] and random() > 0.6 and nj != self.first:
						self.diminish()
					else:
						if random() > 0.9 and ni != self.first:
							self.augment()
						elif random() > 0.35 and nj != self.first:
							self.diminish()
						else:
							self.last = Note(choice(state["chord"]), self.octave)
				elif p == 3:
					try:
						next = state["chords"][state["progression_index"] + 1]
					except:
						next = state["chord"]
					if random() > 0.8:
						self.last = Note(choice(next), self.octave)
						self.diminish()
					if random() > 0.9:
						self.augment()
					else:
						self.diminish()
						if random() > 0.9:
							self.diminish()
			if random() < wild * 1.5:
				return [self.last]

					
						
	def diminish(self):
		self.last.name = notes.diminish(self.last.name)

	def augment(self):
		self.last.name = notes.augment(self.last.name)

				
