from Block import Block

class IncreasingBPM(Block):

	def get_bpm(self, iteration, tick):
		self.bpm *= 1.005
		return self.bpm
