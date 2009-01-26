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


	def show_item(self):
		self.ui.item.clear()
		for x in self.get_progression(",").split():
			if x not in ["{", "}", "", " "]:
				self.ui.item.addItem(x.replace("*", " "))

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

	def set_item(self):
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
		
	
