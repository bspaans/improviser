from Block import Block

class IncreasingWildness(Block):

	def get_wildness(self, iteration, tick):
		self.wildness *= 1.005
		return self.wildness
