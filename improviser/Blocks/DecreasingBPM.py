from Block import Block

class DecreasingBPM(Block):

	def get_bpm(self, iteration, tick):
		if self.bpm > 1:
			self.bpm *= 0.995
			return self.bpm
		else:
			return 1
