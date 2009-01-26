from PyQt4 import QtCore, QtGui
from qtGUI.browserDialog import Ui_browserDialog

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class Browser(QtGui.QDialog):

	def __init__(self, listwidget, filecollection, content_type):
		QtGui.QDialog.__init__(self)
		self.listwidget = listwidget
		self.content_type = content_type
		self.filecollection = filecollection
		self.ui = Ui_browserDialog()
		self.ui.setupUi(self)
		self.setup()


	def setup(self):

		self.connect(self.ui.update,
			QtCore.SIGNAL("clicked()"),
			self.check_for_updates)
		self.connect(self.ui.authors,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_content)
		self.connect(self.ui.content,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_item)
		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			self.set_progression)

		self.state = DEFAULT
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)
		if not self.filecollection.loggedin:
			self.ui.update.setEnabled(False)

	def show_authors(self):
		pass


	def show_content(self):
		self.set_state()
		i = self.ui.authors.currentRow()
		t = str(self.ui.authors.item(i).text())
		if i >= 0:
			if i == 0:
				self.show_defaults()
			elif i == 1:
				self.show_own()
			elif i == 2:
				self.show_all()
			else:
				self.show_author(t)

	def show_own(self):
		self.ui.content.clear()
		self.show_author(self.filecollection.credentials["username"])

	def show_all(self):
		self.ui.content.clear()
		prog = self.filecollection.get(self.content_type)
		for x in prog:
			for y in prog[x]:
				self.ui.content.addItem(y + "  [%s]" % (x))
		self.ui.content.setCurrentRow(0)

	def show_defaults(self):
		pass

	def check_for_updates(self):
		if str(self.ui.update.text())[:6] == "Update":
			return self.update_database()
		try:
			d = feedparser.parse(Options.UPLOAD_HOME + "updates.php?type=%d&ID=%d" % 
					(self.content_type, self.filecollection.last_ID[Options.UPLOAD_PROGRESSION]))
		except:
			return
		if len(d["entries"]) > 0:
			self.ui.update.setText("Update (%d)" % len(d["entries"]))
			self.entries = d["entries"]
		else:
			q = QtGui.QMessageBox.information(self, "Update", "There are currently no updates available. Your collection is up to date.", 1,0)
			self.ui.update.setText("Check for Updates")
