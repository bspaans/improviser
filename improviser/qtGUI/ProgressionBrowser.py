from PyQt4 import QtCore, QtGui
import Options
import Progressions
import feedparser
import urllib
from Browser import Browser

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class ProgressionBrowser(Browser):



	def setup(self):
		Browser.setup(self)
		[self.ui.authors.addItem(x) for x in self.filecollection.get_Progressions() if x != 'Default']
		map(lambda x: self.ui.authors.item(x).setFont(QtGui.QFont("", -1, 75)), range(3))


	def show_defaults(self):
		self.ui.content.clear()
		for x in self.filecollection.get_Progressions(True):
			self.ui.content.addItem(x)
		self.ui.content.setCurrentRow(0)

	def show_item(self):
		self.ui.item.clear()
		for x in self.get_progression(",").split():
			if x not in ["{", "}", "", " "]:
				self.ui.item.addItem(x.replace("*", " "))

	def show_author(self, author):
		prog = self.filecollection.get_Progressions()
		self.ui.content.clear()
		for x in prog[author]:
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


	def get_progression(self, for_show = True):
		i = self.ui.content.currentRow()
		t = str(self.ui.content.item(i).text())
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
		i = self.ui.content.currentRow()
		t = str(self.ui.content.item(i).text())
		self.set_state()
		res = self.get_progression(False)
		for x in res.split(","):
			if x not in ["", " ", "{}", "{ }"]:
				if self.state == DEFAULT:
					self.listwidget.addItem("%s %s" % (t,x))
				else:
					self.listwidget.addItem(x)

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
		q = QtGui.QMessageBox.information(self, "Update", "Added %d new progression(s). Your progressions are up to date." % (i + 1), 1,0)
		self.ui.update.setText("Check for Updates")
		self.show_defaults()
		self.ui.authors.setCurrentRow(0)
