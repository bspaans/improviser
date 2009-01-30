from instrumentDialog import Ui_instrumentDialog
from mingus.containers.Instrument import MidiInstrument
from PyQt4 import QtCore, QtGui
import Options
import Musicians

class InstrumentDialog(QtGui.QDialog):

	def __init__(self, item):
		QtGui.QDialog.__init__(self)
		self.item = item
		self.ui = Ui_instrumentDialog()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):
		for x in Options.get_available_instruments():
			self.ui.algorithm.addItem(x)

		m = MidiInstrument()
		d = 1
		for x in m.names:
			self.ui.midi.addItem("%d. %s" % (d, x))
			d += 1

		self.connect(self.ui.algorithm, 
			QtCore.SIGNAL("activated(int)"),
			lambda x: self.load_instrument(self.ui.algorithm.currentText()))

		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			lambda: self.save_instrument())

	def save_instrument(self):
		chan = self.ui.channel.value()
		drum = False
		if chan == 9:
			drum = True


		res = ""
		res += self.ui.algorithm.currentText() + " { "
		res += "channel:%d " % (self.ui.channel.value())
		if not drum:
			res += "midi_instr:%d " % (self.ui.midi.currentIndex())
		res += "start:%d " % self.ui.stepstart.value()
		res += "chance:%f " % (self.ui.chance.value())
		if self.ui.step.value() != 0:
			res += "step:%d " % self.ui.step.value()
		if self.ui.stepend.value() != -1:
			res += "end:%d " % self.ui.stepend.value()
		res += "max_velocity:%d min_velocity:%d " % (self.ui.maxvelocity.value(),
				self.ui.minvelocity.value())
		res += "note_length:%d " % self.ui.noteduration.value()
		res += "max_notes:%d " % self.ui.maxnotes.value()
		res += "}"
		self.item.setText(res)

	def load_instrument(self, instr_str):
		instr_str = str(instr_str)
		parts = instr_str.split(" ")

		index = combo_index_by_text(self.ui.algorithm, parts[0])
		if index > 0:
			self.ui.algorithm.setCurrentIndex(index)

		params = Options.parse_instrument_params(parts[1:])
		i = getattr(Musicians, parts[0])(params)
		self.ui.stepstart.setValue(i.start)
		self.ui.stepend.setValue(i.end)
		self.ui.step.setValue(i.step)
		if 'max_velocity' in i.params:
			self.ui.maxvelocity.setValue(i.params["max_velocity"])
		else:
			self.ui.maxvelocity.setValue(100)
		if 'min_velocity' in i.params:
			self.ui.minvelocity.setValue(i.params["min_velocity"])
		else:
			self.ui.minvelocity.setValue(50)

		if 'chance' in i.params:
			self.ui.chance.setValue(i.params['chance'])

		self.ui.channel.setEnabled(True)
		if 'channel' in i.params:
			self.ui.channel.setValue(i.params["channel"])
			if i.params["channel"] == 9:
				self.ui.channel.setEnabled(False)
		else:
			self.ui.channel.setValue(0)

		if 'note_length' in i.params:
			self.ui.noteduration.setValue(i.params["note_length"])
		else:
			self.ui.noteduration.setValue(2)

		if 'midi_instr' in i.params:
			self.ui.midi.setCurrentIndex(i.params['midi_instr'])
		else:
			self.ui.midi.setCurrentIndex(0)

		if 'max_notes' in i.params:
			self.ui.maxnotes.setValue(i.params['max_notes'])
		else:
			self.ui.maxnotes.setValue(-1)


def combo_index_by_text(combo, text):
	for x in range(combo.count()):
		if combo.itemText(x) == text:
			return x
	return -1
