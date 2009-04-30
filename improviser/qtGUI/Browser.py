from PyQt4 import QtCore, QtGui
from qtGUI.UI.browserDialog import Ui_browserDialog
import feedparser
import Options
import urllib

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
			self.set_item)
		self.connect(self.ui.newbutton,
			QtCore.SIGNAL("clicked()"),
			self.new_item)

		self.state = DEFAULT
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)
		if not self.filecollection.loggedin:
			self.ui.update.setEnabled(False)
			
		[self.ui.authors.addItem(x) for x in self.filecollection.get(self.content_type) if x != 'Default']
		map(lambda x: self.ui.authors.item(x).setFont(QtGui.QFont("", -1, 75)), range(3))

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
		p = self.filecollection.get(self.content_type)
		for x in p:
			for y in p[x]:
				self.ui.content.addItem(y + "  [%s]" % (x))
		self.ui.content.setCurrentRow(0)

	def show_defaults(self):
		self.ui.content.clear()
		for x in self.filecollection.get(self.content_type, True):
			self.ui.content.addItem(x)
		self.ui.content.setCurrentRow(0)

	def show_author(self, author):
		p = self.filecollection.get(self.content_type)
		self.ui.content.clear()
		if not p.has_key(author):
			return
		for x in p[author]:
			self.ui.content.addItem(x)
		self.ui.content.setCurrentRow(0)

	def set_state(self):
		i = self.ui.authors.currentRow()
		if i == 0:
			self.state = DEFAULT
		elif i == 1:
			self.state = OWN
		elif i == 2:
			self.state = ALL
		else:
			self.state = OTHER

	def get_item(self, for_show = True):
		i = self.ui.content.currentRow()
		t = str(self.ui.content.item(i).text())
		if self.state == DEFAULT:
			return self.get_default(for_show, t)
		else:
			if self.state == ALL:
				parts = t.split("  [")
				if len(parts) == 1:
					return ""
				name = parts[0]
				owner = parts[1][:-1]
			elif self.state == OWN:
				owner = self.filecollection.credentials["username"]
				name = t
			elif self.state == OTHER:
				owner = self.ui.authors.currentRow()
				if owner == -1:
					return ""
				owner = str(self.ui.authors.item(owner).text())
				name = t
			if for_show:
				try:
					return self.filecollection.get(self.content_type)[owner][name]
				except:
					return ""
			else:
				try:
					return self.filecollection.get(self.content_type, parse_content = False)[owner][name]
				except:
					return ""


		return ""

	def get_default(self, for_show, item):
		defa = self.filecollection.get(self.content_type, True)
		if defa.has_key(item):
			if for_show:
				return defa[item]
			else:
				return "{ " +defa[item] + " }"
		return ""


	def show_item(self):
		self.ui.item.clear()
		for x in self.get_item(",").split():
			if x not in ["{", "}", "", " "]:
				self.ui.item.addItem(x.replace("*", " "))


	def set_item(self):
		i = self.ui.content.currentRow()
		t = str(self.ui.content.item(i).text())
		self.set_state()
		res = self.get_item(False)
		for x in res.split(","):
			if x not in ["", " ", "{}", "{ }"]:
				if self.state == DEFAULT:
					self.add_default_item(t, x)
				else:
					self.listwidget.addItem(x)

		self.reject()

	def add_default_item(self, name, content):
		self.listwidget.addItem("%s %s" % (name, content))


	def check_for_updates(self):
		if str(self.ui.update.text())[:6] == "Update":
			return self.update_database()
		try:
			d = feedparser.parse(Options.UPLOAD_HOME + "updates.php?type=%d&ID=%d" % 
					(self.content_type, self.filecollection.last_ID[self.content_type]))
		except:
			q = QtGui.QMessageBox.warning(self, "Error", "An error occured while trying to update the library.", 1,0)
			return
		if len(d["entries"]) > 0:
			self.ui.update.setText("Update (%d)" % len(d["entries"]))
			self.entries = d["entries"]
		else:
			q = QtGui.QMessageBox.information(self, "Update", "There are currently no updates available. Your collection is up to date.", 1,0)
			self.ui.update.setText("Check for Updates")

	def update_database(self):
		if not self.filecollection.loggedin:
			return 
		progress = QtGui.QProgressDialog("Updating library...", "Abort", 0, len(self.entries), self)
		for i, x in enumerate(self.entries):
			id = int(x.id[len(Options.UPLOAD_HOME):])
			download = "%s (%d.prg)" % (x.title, id)
			progress.setLabelText("Downloading %s..." % download)
			print "Downloading %s..." % download
			progress.setValue(i)
			try:
				f = urllib.urlopen(Options.UPLOAD_HOME + "download.php?ID=%d" % id)
				content = f.read()
				f.close()
				self.filecollection.add(self.content_type, id, x.author, x.title, x.description, content)
			except:
				q = QtGui.QMessageBox.warning(self, "Error", "An error occured while download %s." % (download), 1,0)
				return

			if progress.wasCanceled():
				break
		progress.setValue(len(self.entries))
		self.filecollection.save()
		q = QtGui.QMessageBox.information(self, "Update", "Added %d new item(s). Your collection is up to date." % (i + 1), 1,0)
		self.ui.update.setText("Check for Updates")
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)

	def new_item(self):
		pass
