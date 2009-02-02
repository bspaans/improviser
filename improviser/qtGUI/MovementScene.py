from PyQt4 import QtCore, QtGui
from mingus.containers.Instrument import MidiInstrument
import Options
import math


class MovementScene(QtGui.QGraphicsScene):

	IOFFSETX = 250
	IOFFSETY = 50
	BOXSIZE = 25

	# Memoizatio
	last_prog_block = ()
	last_prog_block_index = ()
	last_progressions = ()
	last_instr = ""
	last_instr_names = []
	bars = {}
	bar_texts = []
	last_text = None
	last_sel = -1
	last_sel_item = None
	last_blocks = []
	last_end = -1
	last_bar = -2
	last_bar_selector = []

	def __init__(self, main):
		QtGui.QGraphicsScene.__init__(self)
		self.main = main
		self.ui = main.ui
		self.midi_instr = MidiInstrument()

		# Brushes and pens
		self.brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
		self.brush_dont_play = QtGui.QBrush(QtCore.Qt.white, QtCore.Qt.NoBrush)
		self.brush_play = QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern)
		self.brush_must_play = QtGui.QBrush(QtGui.QColor(255, 0, 0).light(60), QtCore.Qt.SolidPattern)
		self.brush_must_not_play = QtGui.QBrush(QtGui.QColor(250,250,250), QtCore.Qt.SolidPattern)
		self.brush_percussion = QtGui.QBrush(QtGui.QColor(255,255,0), QtCore.Qt.SolidPattern)
		self.brush_must_play_percussion = QtGui.QBrush(QtGui.QColor(255, 255, 0).light(80), QtCore.Qt.SolidPattern)
		self.brush_selection = QtGui.QBrush(QtGui.QColor(0, 0, 255).light(186), QtCore.Qt.SolidPattern)
		self.brush_bar = QtGui.QBrush(QtGui.QColor(0,255,0), QtCore.Qt.SolidPattern)
		self.box_pen = QtGui.QPen(self.brush, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
		self.select_pen = QtGui.QPen(self.brush, 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
		self.bar_pen = QtGui.QPen(self.brush_bar, 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
		self.ui.graphicsView.setScene(self)

		

	def mousePressEvent(self, ev):
		self.pressed = ev.scenePos()

	def mouseReleaseEvent(self, ev):
		if self.pressed == ev.scenePos():
			x, y = self.get_box_coords(ev)
			if self.ui.instruments.count() == 0 or self.ui.progressions.count() == 0:
				return
			if x >= 0 and y >= 0:
				self.ui.instruments.setCurrentRow(y)
				instrument = self.ui.instruments.item(y)
				instr = str(instrument.text()).split()
				params = Options.parse_instrument_params(instr[1:])

				play, stop = [], []
				if 'must_not_play' in params:
					stop = [ int(z) for z in params['must_not_play'].split("-") ]

				if 'must_play' in params:
					play = [ int(z) for z in params['must_play'].split("-")]


				if x in play:
					play.remove(x)
					if x not in stop and not self.plays(params, x, True):
						stop.append(x)
				elif x in stop:
					stop.remove(x)
					if x not in play:
						play.append(x)
				else:
					if not self.plays(params, x, True):
						play.append(x)
					else:
						stop.append(x)

				stop = [ str(x) for x in stop ]
				play = [ str(x) for x in play ]

				if play != []:
					play.sort()
					params['must_play'] = "-".join(play)
				else:
					if params.has_key('must_play'):
						del params['must_play']
				if stop != []:
					stop.sort()
					params['must_not_play'] = "-".join(stop)
				else:
					if params.has_key('must_not_play'):
						del params['must_not_play']
				
				instrument.setText("%s { %s }" % (instr[0], " ".join([ "%s:%s" % (str(x), str(params[x])) for x in params ]) ))
				self.update()
			elif y >= 0:
				self.ui.instruments.setCurrentRow(y)
				self.update()

	def get_box_coords(self, ev):
		x, y = self.pressed.x(), self.pressed.y()
		x = x - self.IOFFSETX
		y = y - self.IOFFSETY
		boxx = x / self.BOXSIZE
		boxy = y / self.BOXSIZE
		x = -1
		y = -1
		if boxy - math.floor(boxy) < 0.8:
			y = int(math.floor(boxy))
		if boxx - math.floor(boxx) < 0.8:
			x = int(math.floor(boxx))
		return (x, y)

	def mouseDoubleClickEvent(self, ev):
		if self.pressed == ev.scenePos():
			x, y = self.get_box_coords(ev)
			if y >= 0 and x < 0:
				self.ui.editinstrument.click()
		
		self.pressed = []

	def plays(self, params, n, ignore_arbitrary_bars = False):
		start, end, step, global_end = -1, -1, -1, -1
		must_play, must_not_play = [], []
		if 'start' in params:
			start = params['start']
		if 'step' in params:
			step = params['step']
		if 'end' in params:
			end = params['end']
		if 'global_end' in params:
			global_end = params['global_end']
		if 'must_play' in params:
			must_play = [ int(x) for x in params['must_play'].split("-") ]
		if 'must_not_play' in params:
			must_not_play = [ int(x) for x in params['must_not_play'].split("-") ]

		if not ignore_arbitrary_bars:
			if n in must_play:
				return 2

			if n in must_not_play:
				return -1

		if global_end != -1 and n >= global_end:
			return 0

		if start == -1:
			return 1
		if n < start:
			return 0

		if end == -1 and step == -1:
			return 1

		if step == -1:
			if n >= start and n < end:
				return 1
			return 0

		if end == -1:
			n = (n - start) % (step * 2)
			if n < step:
				return 1
			return 0

		n = (n - start) % (end - start + step)
		if n < end - start:
			return 1
		return 0

	def get_progressions(self):
		changed = 1
		try:
			p = self.main.get_progressions().split(",")
			if self.last_progressions == p:
				changed = 0
			self.last_progressions = p
			prog = [Options.parse_progression(x) for x in p]
			prog_text = [ x.split()[0] for x in p]
			return (changed, prog, prog_text)
		except:
			return (1, [], [])

	def get_prog_block_index(self, prog):
		duration = int(self.ui.duration.value())
		prog_block_index, prog_index, offset = [], 0, 0
		if len(prog) != 0:
			if self.ui.blocks.count() == 0:
				search_space = ["Block"]
			else:
				search_space = self.main.get_blocks().split(",")

			if self.last_prog_block == (prog, search_space):
				return self.last_prog_block_index

			self.last_prog_block = (prog, search_space)
			for x in search_space:
				parts = x.split()
				params = Options.parse_block_params(parts[1:])
				dur = params['duration'] if 'duration' in params else duration
				for i in range(dur):
					prog_block_index.append((offset, parts[0], prog_index))
					prog_offset = 0
					for itk, tk in enumerate(prog[prog_index]):
						if itk != 0:
							offset += (tk[0] - prog_offset) * len(prog[prog_index][itk - 1][1])
						prog_offset = tk[0]
				prog_index += 1 
				if prog_index >= len(prog):
					prog_index =0

		self.last_prog_block_index = (0, offset, prog_block_index)
		return (1, offset, prog_block_index)

	def paint_prog_block_index(self):
		progchanged, prog, prog_text = self.get_progressions()
		indexchanged, end, prog_block_index = self.get_prog_block_index(prog)
		IOFFSETY = self.IOFFSETY
		BOXSIZE = self.BOXSIZE
		self.progchanged = progchanged

		if self.main.get_instruments() is None:
			return end

		if len(prog) <= 0:
			self.center_text("No progressions have been added.")
			return None

		if not progchanged and not indexchanged and self.ui.instruments.count() == len(self.last_instr_names):
			return end

		for x in self.last_blocks:
			self.removeItem(x)

		self.last_blocks = []
		for i, x in enumerate(prog_block_index):
			offset, name, prog_index = x
			blockend = end
			if i != len(prog_block_index) - 1:
				blockend = prog_block_index[i + 1][0]
			if name != 'R':
				# Block lines
				x1 = self.IOFFSETX + offset * BOXSIZE
				y1 = IOFFSETY - 10
				y2 = self.IOFFSETY + 3 + self.ui.instruments.count() * BOXSIZE
				width = (blockend - offset) * BOXSIZE - 5
				height = 4

				# Paint upper block lines
				r1 = self.addRect(QtCore.QRectF(x1, y1, width, 4), self.select_pen)

				# Paint lower block lines
				r2 = self.addRect(QtCore.QRectF(x1, y2, width, 4), self.select_pen)

				self.last_blocks += [r1, r2]

				# Block text
				t = self.addText(name[:int((blockend-offset) * 2.5)], 
					QtGui.QFont("", 12, 80))
				t.setToolTip(name)
				t.translate(self.IOFFSETX + BOXSIZE * offset, 3)
				self.last_blocks.append(t)

				# Progression text
				t = self.addText(prog_text[prog_index][:int((blockend - offset) * 3)], QtGui.QFont("", 8, 40, True))
				t.setToolTip(prog_text[prog_index])
				t.translate(self.IOFFSETX + BOXSIZE * offset, IOFFSETY - 25)
				self.last_blocks.append(t)
		return end

	def paint_selector(self):
		IOFFSETY = self.IOFFSETY
		BOXSIZE = self.BOXSIZE

		sel = self.ui.instruments.currentRow()
		if sel != self.last_sel:
			self.last_sel = sel
			if self.last_sel_item is not None:
				self.removeItem(self.last_sel_item)

			if sel != -1:
				r = self.addRect(QtCore.QRectF(-1, sel * BOXSIZE + IOFFSETY - 1, self.width(), BOXSIZE - BOXSIZE / 5 + 1), self.select_pen, self.brush_selection)
				r.setZValue(-50)
				self.last_sel_item = r
			else:
				self.last_sel_item = None

	def paint_bar(self, bar_number):

		if self.ui.instruments.count() != len(self.last_instr_names):
			for i, x in enumerate(self.last_bar_selector):
				if (i + 1) % 2 != 0:
					diff = self.ui.instruments.count() - len(self.last_instr_names)
					x.translate(0, diff * self.BOXSIZE)

		if self.last_bar == bar_number:
			return 

		if self.ui.instruments.count() == 0 or self.ui.progressions.count() == 0:
			for x in self.last_bar_selector:
				self.removeItem(x)
			self.last_bar_selector = []
			return

		delta = bar_number - self.last_bar
		if delta not in [0, 1]:
			for x in self.last_bar_selector:
				self.removeItem(x)
			self.last_bar_selector = []
		self.last_bar = bar_number

		dx = 0
		progchanged, prog, prog_text = self.get_progressions()
		for i,x in enumerate(self.last_prog_block_index[2]):
			offset, name, prog_index = x
			if bar_number == offset - 1:
				dx = -5
		
		if bar_number == self.last_end - 1:
			dx = -5

		if bar_number >= self.last_end:
			return

		x = bar_number * self.BOXSIZE + self.IOFFSETX
		y1 = self.IOFFSETY + 3 + self.ui.instruments.count() * self.BOXSIZE
		y2 = self.IOFFSETY - 10
		pen = self.bar_pen
		brush = self.brush_bar

		l = self.addRect(QtCore.QRectF(x, y1, self.BOXSIZE + dx, 3), pen, brush)
		l.setZValue(-50)
		self.last_bar_selector.append(l)

		l = self.addRect(QtCore.QRectF(x, y2, self.BOXSIZE + dx, 3), pen, brush)
		l.setZValue(-50)
		self.last_bar_selector.append(l)

	def paint_bar_selector(self):
		self.paint_bar(self.last_bar)


	def update(self):
		"""Gets called everytime something might have changed."""
		
		# Remove status text if there is any
		if self.last_text is not None:
			self.removeItem(self.last_text)
			self.last_text = None

		self.paint_instruments()

	def paint_instruments(self):

		IOFFSETY = self.IOFFSETY
		BOXSIZE = self.BOXSIZE

		# Paint the blocks and progressions
		# end represents the last bar
		end = self.paint_prog_block_index()
		if end is None:
			return

		# Paint selector and the current bar.
		self.paint_selector()
		self.paint_bar_selector()

		# Check if instruments need to be repainted
		instr = self.main.get_instruments()
		if self.last_instr == instr and end == self.last_end and not self.progchanged:
			return
		self.last_instr = instr


		if instr is not None:
			old_bars = self.bars
			bars = {}
			instr_lst = instr.split(",")
			instr_parts = [ x.split() for x in instr_lst ]
			instr_name = [ x[0] for x in instr_parts]

			for x in self.bar_texts:
				self.removeItem(x)
			self.bar_texts = []
			for i in range(0, end, 4):
				t = self.addText(str(i), QtGui.QFont("", 8, 40, True))
				t.translate(self.IOFFSETX + i * BOXSIZE, self.IOFFSETY + 9 + len(instr_lst) * self.BOXSIZE)
				self.bar_texts.append(t)

			for i, x in enumerate(instr_lst):
				parts = instr_parts[i]

				if not old_bars.has_key(x) or end != self.last_end or self.last_instr_names != instr_name:

					bars[x] = []

					# Get instrument name and parameters
					name = instr_name[i]
					params = Options.parse_instrument_params(parts[1:])

					# Add instrument and midi instrument tooltip
					s = self.addText(name)
					if 'midi_instr' in params:
						s.setToolTip(self.midi_instr.names[params['midi_instr']])
					s.translate(0, i * BOXSIZE + IOFFSETY)
					bars[x].append(s)

					
					for n in range(end):
						plays = self.plays(params, n)
						if plays > 0:
							if plays == 1:
								b = self.brush_play
							elif plays == 2:
								b = self.brush_must_play

							if 'channel' in params and params['channel'] == 9:
								b = self.brush_percussion if plays == 1	else self.brush_must_play_percussion
						else:
							if plays == 0:
								b = self.brush_dont_play
							else:
								b = self.brush_must_not_play
						a = self.addRect(QtCore.QRectF(self.IOFFSETX + n * BOXSIZE, i * BOXSIZE + IOFFSETY, BOXSIZE - BOXSIZE / 5, BOXSIZE - BOXSIZE / 5 ), self.box_pen,b)
						bars[x].append(a)
				else:
					bars[x] = old_bars[x]
					del old_bars[x]
			for x in old_bars:
				for y in old_bars[x]:
					self.removeItem(y)
			self.bars = bars
			self.last_instr_names = instr_name

		else:
			self.center_text("No instruments have been added.")

		self.last_end = end

	def clean(self):
		"""Removes all the buffered scene items."""
		for x in self.bars:
			for y in self.bars[x]:
				self.removeItem(y)
		for x in self.last_blocks + self.last_bar_selector + self.bar_texts:
			self.removeItem(x)
		if self.last_sel_item is not None:
			self.removeItem(self.last_sel_item)
		self.last_bar_selector = []
		self.bar_texts = []
		self.last_bar = -2
		self.last_sel = -1
		self.last_sel_item = None
		self.bars = {}
		self.last_blocks = []
		self.last_progressions = ()

		if self.last_text is not None:
			self.removeItem(self.last_text)
			self.last_text = None

	def center_text(self,txt):
		self.clean()
		t = self.addText(txt)
		t.setTextWidth(250)
		t.translate(self.main.size().width() / 2 - (t.textWidth() / 2), self.IOFFSETY)
		self.last_text = t


