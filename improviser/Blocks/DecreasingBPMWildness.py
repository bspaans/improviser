from DecreasingWildness import DecreasingWildness
from DecreasingBPM import DecreasingBPM

class DecreasingBPMWildness(DecreasingWildness, DecreasingBPM):
	
	def get_bpm(self, it, ti):
		return DecreasingBPM.get_bpm(self, it, ti)
