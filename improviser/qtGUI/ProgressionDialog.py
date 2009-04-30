from qtGUI.UI.progressionDialog import Ui_progressionDialog
from PyQt4 import QtCore, QtGui
import Options
from mingus.core import chords
from mingus.core import progressions as mingus_progressions

class ProgressionDialog(QtGui.QDialog):

	def __init__(self, item):
		QtGui.QDialog.__init__(self)
		self.item = item
		self.ui = Ui_progressionDialog()
		self.ui.setupUi(self)
		self.setup()

	def setup(self):
		self.ui.accidentals.addItem("")
		for x in range(1, 3):
			self.ui.accidentals.addItem("b" * x)
		for x in range(1, 3):
			self.ui.accidentals.addItem("#" * x)

		for x in ["I", "II", "III", "IV", "V", "VI", "VII"]:
			self.ui.romannumeral.addItem(x)

		for x in chords.chord_shorthand.keys():
			self.ui.chordsuffix.addItem(x)

		for x in ["0.25", "0.5", "0.75", "1", "2", "3", "4"]:
			self.ui.bars.addItem(x)
		self.ui.bars.setCurrentIndex(3)

		self.connect(self.ui.addchord,
			QtCore.SIGNAL("clicked()"),
			self.add_chord)

		self.connect(self.ui.addprogression,
			QtCore.SIGNAL("clicked()"),
			self.add_progression)

		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			lambda: self.save_progression())

		self.connect(self.ui.clearsequence, 
			QtCore.SIGNAL("clicked()"),
			lambda: self.ui.progressionsequence.clear() or self.ui.progression.clear())

		self.connect(self.ui.removesequence,
			QtCore.SIGNAL("clicked()"),
			self.remove_sequence)

		self.connect(self.ui.upsequence,
			QtCore.SIGNAL("clicked()"),
			lambda: self.swap_list_item(self.ui.progressionsequence))

		self.connect(self.ui.downsequence,
			QtCore.SIGNAL("clicked()"),
			lambda: self.swap_list_item(self.ui.progressionsequence, False))

		self.connect(self.ui.progressionsequence,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_progression)

		self.connect(self.ui.clearprogression, 
			QtCore.SIGNAL("clicked()"),
			self.ui.progression.clear)

		self.connect(self.ui.removeprogression,
			QtCore.SIGNAL("clicked()"),
			self.remove_progression)

		self.connect(self.ui.upprogression,
			QtCore.SIGNAL("clicked()"),
			lambda: self.swap_list_item(self.ui.progression))

		self.connect(self.ui.downprogression,
			QtCore.SIGNAL("clicked()"),
			lambda: self.swap_list_item(self.ui.progression, False))

		self.connect(self.ui.progression,
			QtCore.SIGNAL("itemSelectionChanged()"),
			self.show_chord)

		self.connect(self.ui.accidentals,
			QtCore.SIGNAL("activated(int)"),
			lambda x: self.add_chord(True))

		self.connect(self.ui.romannumeral,
			QtCore.SIGNAL("activated(int)"),
			lambda x: self.add_chord(True))

		self.connect(self.ui.chordsuffix,
			QtCore.SIGNAL("activated(int)"),
			lambda x: self.add_chord(True))

		self.connect(self.ui.repeat,
			QtCore.SIGNAL("valueChanged(int)"),
			lambda x: self.add_progression(True))
			

	def add_chord(self, update = False):
		if update:
			i = self.ui.progression.currentRow()
			if i == -1:
				return self.add_chord()

		chord = str(self.ui.accidentals.currentText())
		chord += str(self.ui.romannumeral.currentText())
		chord += str(self.ui.chordsuffix.currentText())
		duration = str(self.ui.bars.currentText())
		r=  "%s %s" % (duration, chord)
		if not update:
			self.ui.progression.addItem(r)
			self.ui.progression.setCurrentRow(self.ui.progression.count() - 1)
		else:
			self.ui.progression.item(i).setText(r)
		if self.ui.progressionsequence.currentRow() != -1:
			self.add_progression(True)
		else:
			self.add_progression(True)

	def add_progression(self, update = False):
		res=""

		if update:
			i = self.ui.progressionsequence.currentRow()
			if i == -1:
				return self.add_progression()

		for x in range(self.ui.progression.count()):
			t = self.ui.progression.item(x).text()
			parts = t.split(" ")
			if parts[0] == "1":
				text = parts[1]
			else:
				text = "%s%s" % (parts[0], parts[1])
			res += "%s-" % text

		if res != "":
			r = str(self.ui.repeat.value() + 1) + " " + res[:-1]
			if not update:
				self.ui.progressionsequence.addItem(r)
				self.ui.progressionsequence.setCurrentRow(self.ui.progressionsequence.count() - 1)
			else:
				self.ui.progressionsequence.item(i).setText(r)

	def load_progression(self, prog_str):
		p = str(prog_str)
		parts = p.split(" ")
		if len(parts) == 0:
			return 

		if len(parts) == 1 and p in Options.get_available_progressions():
			x = Options.progression_to_string(getattr(Progressions, p))
			return self.load_progression("%s %s" % (p, x))

		self.ui.progressionname.setText(parts[0])
		if len(parts) > 3:
			params = parts[2:-1]
			for x in params:
				r = x.split("*")
				if len(r) == 2:
					self.ui.progressionsequence.addItem("%d %s" % (int(r[0]), r[1]))
				if len(r) == 1 and x != "":
					self.ui.progressionsequence.addItem("0 %s" % r[0])

	def save_progression(self):
		res = ""
		name = str(self.ui.progressionname.text()).replace(" ", "_")
		if name == "":
			return
		
		res += name + " { "
		for x in range(self.ui.progressionsequence.count()):
			t = self.ui.progressionsequence.item(x).text()
			parts = t.split(" ")
			res += "%d*%s " % (int(parts[0]), parts[1])
		res += " }"

		self.item.setText(res)


	def swap_list_item(self, lst, up = True):
		index = lst.currentRow()
		if index < 0:
			return
		c = lst.count()
		cur = lst.item(index)
		i1 = cur.text()
		if up:
			if index > 0:
				i2 = lst.item(index - 1)
				lst.setCurrentRow(index - 1)
			else:
				return 

		else:
			if index < c - 1:
				i2 = lst.item(index + 1)
				lst.setCurrentRow(index + 1)
			else:
				return
		t = i2.text()
		i2.setText(i1)
		cur.setText(t)

	def remove_sequence(self):
		i = self.ui.progressionsequence.currentRow()
		if i >= 0:
			self.ui.progression.clear()
			self.ui.progressionsequence.takeItem(i)
		

	def remove_progression(self):
		i = self.ui.progression.currentRow()
		if i >= 0:
			self.ui.progression.takeItem(i)
			self.add_chord(True)

	def show_progression(self):
		i = self.ui.progressionsequence.currentRow()
		if i >= 0:
			self.ui.progression.clear()
			prog = self.ui.progressionsequence.item(i).text()
			p = prog.split(" ")
			self.ui.repeat.setValue(int(p[0]) - 1)
			chords = p[1].split("-")
			for c in chords:
				if type(c[0]) != int:
					self.ui.progression.addItem("1 %s" % c)
				else:
					print "Can't parse bar length"
			self.ui.progression.setCurrentRow(0)
			self.show_chord()

	def show_chord(self):
		i = self.ui.progression.currentRow()
		if i >= 0:
			parts = str(self.ui.progression.item(i).text()).split(" ")
			self.ui.bars.setCurrentIndex(combo_index_by_text(
				self.ui.bars, parts[0]))
			chord =mingus_progressions.parse_string(parts[1])
			self.ui.romannumeral.setCurrentIndex(combo_index_by_text(
				self.ui.romannumeral, chord[0]))
			self.ui.chordsuffix.setCurrentIndex(combo_index_by_text(
				self.ui.chordsuffix, chord[2]))

			acc = chord[1]
			r = ''
			while acc > 0:
				r += '#'
				acc -= 1
			while acc < 0:
				r += 'b'
				acc += 1
			self.ui.accidentals.setCurrentIndex(combo_index_by_text(
				self.ui.accidentals, r))


def combo_index_by_text(combo, text):
	for x in range(combo.count()):
		if combo.itemText(x) == text:
			return x
	return -1

