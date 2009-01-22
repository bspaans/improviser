class Movement:
	"""The default Movement. Moves sequentially through the blocks and progressions."""

	blocks = []
	progressions = []
	instruments = []
	b_counter = 0
	p_counter = 0

	loop = 0
	default_bpm = 120
	default_wildness = 0.5
	default_key = 'C'
	default_resolution = 8
	swing = False

	def __init__(self):
		pass

	def add_block(self, block):
		self.blocks.append(block)

	def add_progression(self, progression):
		self.progressions.append(progression)

	def set_default_bpm(self, bpm):
		self.default_bpm = bpm
	
	def set_default_wildness(self, wildness):
		self.default_wildness = wildness

	def set_default_key(self, key):
		self.default_key = key
	
	def get_instruments(self):
		return self.instruments

	def get_next_block(self):
		"""Prepares and returns the next block in the movement.\
Returns None if there is no next block."""
		if len(self.blocks) > 0:
			if self.loop >= 0:
				r = self.get_block()
				r.progressions = self.get_progression()
				self.b_counter += 1
				if self.b_counter == len(self.blocks):
					self.b_counter = 0
					self.loop -= 1
				return r
		return None

	def get_block(self):
		return self.blocks[self.b_counter]

	def get_progression(self):
		if len(self.progressions) > 0:
			p = self.get_prog()
			self.p_counter += 1
			if self.p_counter == len(self.progressions):
				self.p_counter = 0

			res = []
			for x in p:
				res.append((x[0], x[1]))
			return res

		return None

	def get_prog(self):
		return self.progressions[self.p_counter]

