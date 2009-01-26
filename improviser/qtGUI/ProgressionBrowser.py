from PyQt4 import QtGui
from Browser import Browser

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class ProgressionBrowser(Browser):



	def setup(self):
		self.setWindowTitle("Progression Browser")
		self.ui.authors.addItem("Default progressions")
		self.ui.authors.addItem("Own progressions")
		self.ui.authors.addItem("All progressions")
		Browser.setup(self)


		
	
