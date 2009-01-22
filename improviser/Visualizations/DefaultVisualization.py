from Visualization import Visualization

class DefaultVisualization(Visualization):

	notes = []

	def paint_screen(self, notes, channel):
		self.notes.append(notes)

	def update_screen(self):
		if self.notes == []:
			print
		for n in self.notes:
			print "%25s" % n, 
		print
		self.notes = []

