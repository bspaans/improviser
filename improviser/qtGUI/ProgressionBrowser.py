from PyQt4 import QtCore, QtGui
from qtGUI.progressionBrowser import Ui_progressionBrowser
import Options
import Progressions
import feedparser
import urllib

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class ProgressionBrowser(QtGui.QDialog):


	def __init__(self, proglist, filecollection):
		QtGui.QDialog.__init__(self)
		self.progression_list = proglist
		self.filecollection = filecollection
		self.ui = Ui_progressionBrowser()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):


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

		for x in self.filecollection.get_Progressions():
			if x != 'Default':
				self.ui.authors.addItem(x)


		self.state = DEFAULT
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)
		self.check_for_updates()

	def check_for_updates(self):
		if not self.filecollection.loggedin:
			self.ui.update.setEnabled(False)
			return
		try:
			d = feedparser.parse(Options.UPLOAD_HOME + "updates.php?type=%d&ID=%d" % 
					(Options.UPLOAD_PROGRESSION, self.filecollection.last_progression))
		except:
			return
		if len(d["entries"]) > 0:
			self.ui.update.setText("Update (%d)" % len(d["entries"]))
			self.ui.update.setEnabled(True)
			self.entries = d["entries"]
		else:
			self.ui.update.setEnabled(False)


	def show_progressions(self):
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

	def show_defaults(self):
		self.ui.progressions.clear()
		for x in self.filecollection.get_Progressions(True):
			self.ui.progressions.addItem(x)
		self.ui.progressions.setCurrentRow(0)

	def show_own(self):
		self.ui.progressions.clear()
		self.show_author(self.filecollection.credentials["username"])

	def show_all(self):
		self.ui.progressions.clear()
		prog = self.filecollection.get_Progressions()
		for x in prog:
			for y in prog[x]:
				self.ui.progressions.addItem(y + "  [%s]" % (x))
		self.ui.progressions.setCurrentRow(0)
		

	def show_progression(self):
		self.ui.progression.clear()
		for x in self.get_progression(",").split():
			if x not in ["{", "}", "", " "]:
				self.ui.progression.addItem(x.replace("*", " "))

	def show_author(self, author):
		prog = self.filecollection.get_Progressions()
		self.ui.progressions.clear()
		for x in prog[author]:
			self.ui.progressions.addItem(x)
		self.ui.progressions.setCurrentRow(0)


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


	def get_progression(self, for_show = True):
		i = self.ui.progressions.currentRow()
		t = str(self.ui.progressions.item(i).text())
		if self.state == DEFAULT:
			defa = self.filecollection.get_Progressions(True)
			if defa.has_key(t):
				if for_show:
					return defa[t]
				else:
					return "{ " +defa[t] + " }"
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
					return self.filecollection.get_Progressions()[owner][name]
				except:
					return ""
			else:
				try:
					return self.filecollection.get_Progressions(parse_content = False)[owner][name]
				except:
					return ""


		return ""

	def set_progression(self):
		i = self.ui.progressions.currentRow()
		t = str(self.ui.progressions.item(i).text())
		self.set_state()
		res = self.get_progression(False)
		for x in res.split(","):
			if x not in ["", " ", "{}", "{ }"]:
				print x, self.state
				if self.state == DEFAULT:
					self.progression_list.addItem("%s %s" % (t,x))
				else:
					self.progression_list.addItem(x)

		self.reject()
		
	
	def update_database(self):
		if not self.filecollection.loggedin:
			return 
		progress = QtGui.QProgressDialog("Downloading progressions...", "Abort", 0, len(self.entries), self)
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
				self.filecollection.add_Progression(id, x.author, x.title, x.description, content)
			except:
				pass

			if progress.wasCanceled():
				break
		progress.setValue(len(self.entries))
		self.filecollection.save()
		self.ui.update.setEnabled(False)
