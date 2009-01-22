from DoubleTimeBlock import DoubleTimeBlock
from MutatingBlock import MutatingBlock

class MutatingDoubleTimeBlock(MutatingBlock, DoubleTimeBlock):
	
	def get_resolution(self, iteration):
		return DoubleTimeBlock.get_resolution(self, iteration)

