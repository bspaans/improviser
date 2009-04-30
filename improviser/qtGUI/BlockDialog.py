from PyQt4 import QtCore, QtGui
from qtGUI.UI.blockDialog import Ui_blockDialog
from mingus.core import diatonic
import Options

class BlockDialog(QtGui.QDialog):

	def __init__(self, item):
		QtGui.QDialog.__init__(self)
		self.item = item
		self.ui = Ui_blockDialog()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):
		for x in ["From movement", 1, 2, 4, 8, 16, 32, 64, 128]:
			self.ui.resolution.addItem(str(x))
		for x in ["From movement"] + diatonic.basic_keys:
			self.ui.key.addItem(x)
		for x in Options.get_available_blocks():
			self.ui.blockcombo.addItem(x)

		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			lambda: self.save_block())

	def load_block(self, block_str):

		p = block_str.split(" ")
		self.ui.blockcombo.setCurrentIndex(combo_index_by_text(self.ui.blockcombo, p[0]))

		if len(p) == 1:
			return 

		params = Options.parse_block_params(p[1:])
		if 'duration' in params:
			self.ui.duration.setValue(params['duration'])
		if 'bpm' in params:
			self.ui.bpm.setValue(params["bpm"])
		if 'wild' in params:
			self.ui.wildness.setValue(params["wild"])
		if 'swing' in params:
			if params["swing"]:
				self.ui.swing.setCurrentIndex(2)
			else:
				self.ui.swing.setCurrentIndex(1)
		if 'key' in params:
			self.ui.key.setCurrentIndex(combo_index_by_text(self.ui.key, params["key"]))
		if 'resolution' in params:
			self.ui.resolution.setCurrentIndex(combo_index_by_text(self.ui.resolution, str(params["resolution"])))



	def save_block(self):
	
		block = self.ui.blockcombo.currentText()
		res = str(block) + " { "

		bpm = self.ui.bpm.value()
		resolution = str(self.ui.resolution.currentText())
		key = str(self.ui.key.currentText())
		wild = self.ui.wildness.value()
		duration = self.ui.duration.value()
		swing = self.ui.swing.currentIndex()

		if bpm != 0:
			res += "bpm:%d " % bpm
		if wild != 0.0:
			res += "wild:%f " % wild
		if duration != 0:
			res += "duration:%d " % duration
		
		if swing > 0:
			res += "swing:%d " % (swing - 1)
		if resolution != "From movement":
			res += "resolution:%s " % resolution
		if key != "From movement":
			res += "key:%s " % key

		
		
		res += "}"
		if res == str(block) + " { }":
			res = str(block)
		self.item.setText(res)

def combo_index_by_text(combo, text):
	for x in range(combo.count()):
		if combo.itemText(x) == text:
			return x
	return -1
