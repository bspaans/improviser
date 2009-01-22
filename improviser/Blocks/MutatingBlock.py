from Block import Block
from improviser.Progressions import *
from mingus.core import progressions
from random import random, choice

class MutatingBlock(Block):

	def get_progression(self, iteration):
		res = Block.get_progression(self, iteration)
		# Mutate
		if random() < 0.5 * self.wildness:
			change = choice(range(len(res)))
			if self.wildness > 0.5:
				depth = 1
			else:
				depth = 0
			r =progressions.substitute(res, change, depth)
			if r != []:
				res[change] = choice(r)
				p = self.progressions
				for i in range(len(p)):
					if i < len(p) - 1:
						if p[i][0] <= iteration and p[i + 1][0] > iteration:
							p[i] = (p[i][0], res)
				print res

		return res
