import Bands
from improviser.Progressions import *
from mingus.core import progressions

class Block:

	progressions = Contemporary.reincarnatie
	
	bpm = 0
	resolution = 0
	meter = (4,4)
	duration = 0

	swing = 'Default'
	key = 'Default'

	wildness = 0.0

	def get_bpm(self, iterations, tick):
		return self.bpm

	def get_duration(self):
		p = self.progressions
		song_length = p[-1][0] - p[0][0]
		return self.duration * song_length - 1

	def get_key(self, iteration):
		return self.key

	def get_meter(self, iteration, tick):
		return self.meter

	def get_progression(self, iteration):
		p = self.progressions
		iteration -= 1
		res = []
		for i in range(len(p)):
			if i < len(p) - 1:
				if p[i][0] <= iteration and p[i + 1][0] > iteration:
					res= p[i][1]
					break
			else:
				res = p[i][1]
				break
		if res == 'R':
			song_length = p[-1][0] - p[0][0]
			for prog in p:
				p[p.index(prog)] = \
					(prog[0] + song_length, prog[1])
			return self.get_progression(iteration + 1)

		return res


	def get_resolution(self, iteration):
		return self.resolution

	def get_tick_length(self, tick, tick_length):
		if not self.swing:
			return tick_length
		else:
			if tick % 2 == 0:
				return tick_length * 1.33
			else:
				return tick_length * 0.66


	def get_wildness(self, iteration, tick):
		return self.wildness

	def stop(self):
		pass
