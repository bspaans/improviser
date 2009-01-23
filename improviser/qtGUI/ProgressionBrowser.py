from PyQt4 import QtCore, QtGui
from qtGUI.progressionBrowser import Ui_progressionBrowser
import Options

DEFAULT = 1
OWN = 2
OTHER = 10

class ProgressionBrowser(QtGui.QDialog):

	def __init__(self, item):
		QtGui.QDialog.__init__(self)
		self.item = item
		self.ui = Ui_progressionBrowser()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):

		self.defaults = {"Empty": "",
				 "Pop": "1*I-IV-V-I",
				 "Simple": "1*I-V"}

		self.connect(self.ui.update,
			QtCore.SIGNAL("clicked()"),
			self.update_database)
		self.connect(self.ui.authors,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_progressions)
		self.connect(self.ui.progressions,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_progression)
		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			self.set_progression)

		self.state = DEFAULT
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)

	def show_progressions(self):
		i = self.ui.authors.currentRow()
		t = self.ui.authors.item(i).text()
		if i >= 0:
			self.ui.progressions.clear()
			self.ui.progression.clear()
			if i == 0:
				self.state = DEFAULT
				self.show_defaults()

	def show_defaults(self):
		for x in self.defaults:
			self.ui.progressions.addItem(x)
		self.ui.progressions.setCurrentRow(0)

	def show_progression(self):
		self.ui.progression.clear()
		for x in self.get_progression().split(" "):
			self.ui.progression.addItem(x)

	def get_progression(self, for_show = True):
		if self.state == DEFAULT:
			i = self.ui.progressions.currentRow()
			t = str(self.ui.progressions.item(i).text())
			if for_show:
				prog = self.defaults[t]
				prog = prog.replace("*", " ")
				return prog
			else:
				return "{ " + self.defaults[t] + " }"
		return []

	def set_progression(self):
		i = self.ui.progressions.currentRow()
		t = str(self.ui.progressions.item(i).text())
		prog = self.get_progression(False)
		self.item.setText("%s %s" % (t, prog))
		
	
	def update_database(self):
		pass
