from Instrument import Instrument
from mingus.containers.Note import Note
from random import choice, random, randrange

class SoloInstrument(Instrument):

	def __init__(self, params):
		Instrument.__init__(self, params)

	def generate_note(self, state):
		chance = 0.8
		wild = 1.0

		if 'chance' in self.params:
			chance = self.params['chance']

		if 'wild' in state:
			wild = state['wild']


		if state["tick"] % 2 == 0 and random() < chance * wild:
			return [Note(choice(state["chord"]))]
		elif state["tick"] % 2 == 1 and random() < chance * wild:
			for x in self.last_played:
				if x.name in state["scale"]:

					i = state["scale"].index(x.name)
					diff = randrange(1, 7, 2)
					if random() > 0.5:
						i += diff
					else:
						i -= diff
					if i >= len(state["scale"]):
						i = 0
					if i < 0:
						i = len(state["scale"]) - 1
					new = state["scale"][i]

					return [Note(state["scale"][i])]

		return None

