from PyQt4 import QtCore, QtGui
from qtGUI.progressionBrowser import Ui_progressionBrowser
import Options
import Progressions
import feedparser

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class ProgressionBrowser(QtGui.QDialog):

	def __init__(self, item):
		QtGui.QDialog.__init__(self)
		self.item = item
		self.ui = Ui_progressionBrowser()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):

		self.defaults = {"Empty": ""}

		for x in Options.get_available_progressions():
			prog = Options.progression_to_string(getattr(Progressions, x))[1:-1]
			self.defaults[x] = prog

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
		self.check_for_updates()

	def check_for_updates(self):
		d = feedparser.parse(Options.UPLOAD_HOME + "updates.php?type=%d" % Options.UPLOAD_PROGRESSION)
		if len(d["entries"]) > 0:
			self.ui.update.setText("Update (%d)" % len(d["entries"]))
			self.ui.update.setEnabled(True)
		else:
			self.ui.update.setEnabled(True)


	def show_progressions(self):
		i = self.ui.authors.currentRow()
		t = self.ui.authors.item(i).text()
		if i >= 0:
			self.ui.progressions.clear()
			self.ui.progression.clear()
			if i == 0:
				self.state = DEFAULT
				self.show_defaults()
			if i == 1:
				self.state == OWN
				self.show_own()
			if i == 2:
				self.state == ALL
				self.show_all()

	def show_defaults(self):
		for x in self.defaults:
			self.ui.progressions.addItem(x)
		self.ui.progressions.setCurrentRow(0)

	def show_own(self):
		self.show_author(self.username)

	def show_all(self):
		for x in self.defaults:
			self.ui.progressions.addItem(x + "  [default]")
		self.ui.progressions.setCurrentRow(0)
		

	def show_progression(self):
		self.ui.progression.clear()
		for x in self.get_progression().split(" "):
			if x not in ["{", "}", "", " "]:
				self.ui.progression.addItem(x.replace("*", " "))

	def show_author(self, author):
		pass

	def get_progression(self, for_show = True):
		if self.state == DEFAULT:
			i = self.ui.progressions.currentRow()
			t = str(self.ui.progressions.item(i).text())
			if self.defaults.has_key(t):
				if for_show:
					return self.defaults[t]
				else:
					return "{ " + self.defaults[t] + " }"
		return ""

	def set_progression(self):
		i = self.ui.progressions.currentRow()
		t = str(self.ui.progressions.item(i).text())
		prog = self.get_progression(False)
		self.item.setText("%s %s" % (t, prog))
		self.reject()
		
	
	def update_database(self):
		pass
