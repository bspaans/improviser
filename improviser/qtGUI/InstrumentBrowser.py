
from PyQt4 import QtGui
from Browser import Browser

DEFAULT = 1
OWN = 2
ALL = 3
OTHER = 10

class InstrumentBrowser(Browser):



	def setup(self):
		self.setWindowTitle("Instrument Browser")
		self.ui.authors.addItem("Default instruments")
		self.ui.authors.addItem("Own instruments")
		self.ui.authors.addItem("All instruments")
		Browser.setup(self)

	def get_default(self, for_show, item):
		if not self.filecollection.get(self.content_type)["Default"].has_key(item):
			return ""
		if for_show:
			return self.filecollection.get(self.content_type)["Default"][item]
		else:
			return self.filecollection.get(self.content_type, parse_content = False)["Default"][item]

	def add_default_item(self, name, content):
		self.listwidget.addItem("%s" % content)


		
	
