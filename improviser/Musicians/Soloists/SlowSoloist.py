from SimpleSoloInstrument import SimpleSoloInstrument


class SlowSoloist(SimpleSoloInstrument):


	def generate_note(self, state):
		if state["tick"] == 0:
			return SimpleSoloInstrument.generate_note(self, state)
