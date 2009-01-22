import Movement

class FluentMovement(Movement.Movement):
	"""Preserves the bpm and wildness between blocks."""
	
	last_bpm = 0
	last_wildness = 0
	last_block = None

	def __init__(self):
		Movement.Movement.__init__(self)

	def get_block(self):
		if self.last_block is None:
			self.last_block = self.blocks[self.b_counter]
			return self.last_block

		self.last_bpm = self.last_block.bpm
		self.last_wildness = self.last_block.wildness
		self.last_block = self.blocks[self.b_counter]

		next_block = self.blocks[self.b_counter]
		next_block.bpm = self.last_bpm
		next_block.wildness = self.last_wildness
		return next_block


