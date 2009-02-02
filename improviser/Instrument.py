from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer
from random import randrange
from mingus.containers.Track import Track
from mingus.containers.Bar import Bar
from mingus.containers.Instrument import MidiInstrument

class Instrument:

	history = []
	params = {}

	
	playing = []
	last_played = []
	last_chan= 0
	last_bpm = 0

	start = 0
	end = -1
	step = 0
	global_end = -1
	must_play = []
	must_not_play = []

	midi_set = False
	last_tick = (-1, -1) # iteration,tick
	no_fluidsynth = True
	
	def __init__(self, parameters):
		self.params = parameters
		self.track = Track()
		i = MidiInstrument()
		self.track.instrument = i
		if 'start' in parameters:
			self.start = self.params["start"]
			if 'end' not in parameters:
				if 'step' in parameters:
					self.end = self.start + parameters["step"]
		if 'end' in parameters:
			self.end= self.params["end"]
			if 'start' not in parameters:
				self.start = 0

		if 'step' in parameters:
			self.step = parameters["step"]
			if 'start' not in parameters:
				self.start = 0
			if 'end' not in parameters:
				self.end = self.start + self.step
		if 'global_end' in parameters:
			self.global_end = parameters['global_end']

		self.must_play = []
		self.must_not_play = []
		if 'must_play' in parameters:
			self.must_play = [ int(x) for x in parameters['must_play'].split("-") ]

		if 'must_not_play' in parameters:
			self.must_not_play = [ int(x) for x in parameters['must_not_play'].split("-") ] 

	def reset(self):
		self.track = Track()
		self.track.instrument = MidiInstrument()
		self.midi_set = False
		if hasattr(self, "bar"):
			del self.bar

	def import_fluidsynth(self):
		global fluidsynth
		from mingus.midi import fluidsynth
		self.no_fluidsynth = False

	def add_rest(self, state):
		if state["tick"] == 0:
			self.record_new_bar(state)

		dur = state["resolution"]
		if state["swing"]:
			if state["tick"] % 2 == 0:
				dur = 1.0 / (1.0 / dur * (2.0 / 3.0))
			else:
				dur = 1.0 / (1.0 / dur * (4.0 / 3.0))
		self.record_rest(dur)
		self.last_tick = (state["iterations"], state["tick"])


	def get_note_length(self, state):
		"""The number of ticks that should be played."""
		if 'let_ring' not in self.params:
			return 1
	
		if not self.params['let_ring']:
			return 1
		if 'note_length' in self.params:
			maxnl = self.params['note_length']
			if 'min_note_length' in self.params:
				minnl = self.params['min_note_length']
				if minnl != maxnl + 1:
					return randrange(min(minnl, maxnl + 1), max(minnl, maxnl + 1))
				return maxnl
			return maxnl

		if 'min_note_length' in self.params:
			return self.params['min_note_length']

		return state["ticks"] / state["meter"][1] 

	def get_max_simultaneous_notes(self, state):

		if 'max_notes' not in self.params:
			return -1
		else:
			return self.params['max_notes']

	def get_range(self, state):
		minr = 0
		maxr = 115
		if 'max_note' in self.params:
			maxr = self.params['max_note']
		if 'min_note' in self.params:
			minr = self.params['min_note']
		
		if minr > maxr:
			return maxr + 12, minr + 12
		return minr + 12, maxr + 12
	
	def len_current_notes_playing(self):
		res = 0
		for x in self.playing:
			res += len(x[0])
		return res
	
	def set_instrument(self):
		if not(self.midi_set) and 'midi_instr' in self.params:
			if not self.no_fluidsynth:
				fluidsynth.set_instrument(self.params["channel"], self.params["midi_instr"])
			self.midi_set = True
			self.track.instrument.instrument_nr = self.params["midi_instr"]

	def play(self, state):


		if not(self.midi_set):
			self.set_instrument()

		if state["tick"] == 0:
			self.record_new_bar(state)

		self.stop_playing_notes()

		note_length = self.get_note_length(state)
		max_notes = self.get_max_simultaneous_notes(state)
		range_min, range_max = self.get_range(state)

				

		dur = state["resolution"]
		if state["swing"]:
			if state["tick"] % 2 == 0:
				dur = 1.0 / (1.0 / dur * (2.0 / 3.0))
			else:
				dur = 1.0 / (1.0 / dur * (4.0 / 3.0))

		n = self.generate_note(state)
		if n is None:
			n = []
		v = int(self.generate_velocity(state))
		c = self.params["channel"]


		if max_notes != -1 and n != []:
			curn = self.len_current_notes_playing()
			if curn >= max_notes:
				n = []
			elif curn + len(n) > max_notes:
				n = n[:max_notes - curn]

		newn = []
		for note in n:
			if int(note) >= range_min and int(note) <= range_max:
				note.velocity = v
				note.channel = c
				newn.append(note)

		n = newn

		if n != [] and max_notes != 0:
					
			
			#if self.last_bpm != state["bpm"]:
			#	self.last_bpm = state["bpm"]
			#	n = NoteContainer(n)
			#	n.bpm = state["bpm"]

			self.record_notes(state, n, dur)

			if not self.no_fluidsynth:
				fluidsynth.play_NoteContainer(n, c, v)

			self.playing.append([n, note_length])
			self.last_chan = c
			self.last_played = n
			if state["paint_function"] != None:
				state["paint_function"](n, c)
		else:
			self.record_rest(dur)

		self.last_tick = (state["iterations"], state["tick"])

	def record_new_bar(self, state):
		if hasattr(self, "bar"):
			self.track + self.bar
		b = Bar()
		b.set_meter(state["meter"])
		b.length = 0.0
		b.key = state["key"]
		self.bar = b


	def record_notes(self, state, notes, duration):
		"""Adds notes to the track."""
		if self.last_tick != (state["iterations"], state["tick"]):
			self.bar.place_notes(notes, duration)	
		else:
			self.bar.bar[-1][2].add_notes(notes)

	def record_rest(self, duration):
		"""Adds a rest to the track, or adds a tick to the last\
NoteContainer if there are notes playing."""
		dur = duration
		if len(self.bar) > 0:
			if self.bar[-1][2] is None or len(self.playing) > 0:
				i = 1.0 / (1.0 / dur + 1.0 / self.bar[-1][1])
				self.bar[-1][1] = i
				self.bar.current_beat += 1.0 / dur
			else:
				self.bar.place_notes(None, dur)
		else:
			self.bar.place_notes(None, dur)

	def generate_note(self, state):
		return None

	def generate_velocity(self, state):
		wild, minv, maxv = 1.0, 50, 100
		if 'max_velocity' in self.params:
			maxv = self.params['max_velocity']
		if 'min_velocity' in self.params:
			minv = self.params['min_velocity']
		if 'wild' in state:
			wild = state['wild']

		if state["tick"] % (state["resolution"] / float(state["meter"][1])) == 0:
			velocity = randrange(maxv - 10, maxv)
		else:
			velocity = randrange(minv, maxv)

		wildness = (minv - maxv) / 2 * wild
		return max(min(velocity - wildness, 127), 0)


	def stop_playing_notes(self):
		playing = []
		for x in self.playing:
			if x[1] <= 1:
				if not self.no_fluidsynth:
					fluidsynth.stop_NoteContainer(x[0], self.last_chan)
			else:
				playing.append([x[0], x[1] - 1])

		self.playing = playing

	def stop(self):
		if not self.no_fluidsynth:
			for x in range(128):
				fluidsynth.stop_Note(x, self.last_chan)
