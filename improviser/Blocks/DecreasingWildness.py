from Block import Block

class DecreasingWildness(Block):

	def get_wildness(self, iteration, tick):
		if self.wildness > 0:
			self.wildness *= 0.995
			return self.wildness
		return 0.0
