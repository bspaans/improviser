from mingus.core import progressions, diatonic
from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.Composition import Composition
from time import sleep, time
from random import random
from mingus.core import chords
from mingus.midi import MidiFileOut
from os import sys

class Sequencer:

	instruments = []
	progression = []
	state = {}
	iterations = 0
	paint_function = None
	tick_function = None
	update_function = None
	verbose = False
	bar = -1
	chord_index = -1

	def __init__(self, movement):
		self.movement = movement
		if not self.get_next_block():
			sys.exit(0)

	def get_next_block(self):
		b = self.movement.get_next_block()
		if b != None:
			self.block = b
			self.play_iterations = self.block.get_duration()
			return True
		return False


	def block_iteration(self):
		"""Queries the block class for information """
		"""each time a progression has played."""

		b = self.block
		self.meter = b.get_meter(self.iterations, 0)
		self.key = b.get_key(self.iterations)
		self.progression = b.get_progression(self.iterations)
		self.resolution = b.get_resolution(self.iterations)
		self.instruments = self.movement.get_instruments()
		self.set_bpm(b.get_bpm(self.iterations, 0))
		self.wild = b.get_wildness(self.iterations, 0)
		self.reset_state()
	
	def block_tick(self):
		"""Queries the block class on every tick."""

		self.sync()
		b = self.block
		self.set_bpm(b.get_bpm(self.iterations, self.tick))
		self.meter = b.get_meter(self.iterations, self.tick)
		self.wild = b.get_wildness(self.iterations, self.tick)

	def bar_tick(self):

		if self.verbose:
			if self.no_fluidsynth:
				print "|"
			else:
				print "-" * 80
		self.bar += 1

	def change_scale(self):
		
		if self.chord != self.state["chord"]:
			if self.verbose:
				if self.no_fluidsynth:
					sys.stdout.write("|");
			self.state["scale"] = \
				diatonic.get_notes(self.key)
			for n in self.chord:
				if n not in self.state["scale"]:
					self.replace_scale_note(n)

	def change_state(self, tick):

		self.change_scale()
		self.tick = tick % self.ticks
		self.state["chord"] = self.chord
		self.state["progression_index"] = tick / self.resolution
		self.state["tick"] = self.tick
		self.state["ticks"] = self.ticks
		self.state["iteration_tick"] = tick
		self.state["iterations"] = self.iterations
		self.state["wild"] = self.wild
		self.state["paint_function"] = self.paint_function
		self.state["bpm"] = self.bpm
		self.state["bar"] = self.bar


	def iteration(self):
		"""Gets called each iteration -- when self.progression """
		"""changes or gets repeated."""
		self.iterations += 1
		self.play_iterations -= 1
		self.block_iteration()
		self.chords = progressions.to_chords( \
				self.progression, self.key)
		self.state["chords"] = self.chords
		self.ticks = int(round(self.resolution / \
				float(self.meter[1]) * self.meter[0]))


	def play_instruments(self):
		"""Plays all the instruments in self.instruments if """
		"""they are currently enabled."""
		if self.no_fluidsynth:
			sys.stdout.write(".")
		it = self.bar
		for i in self.instruments:
			if it in i.must_play:
				i.play(self.state)
			elif (it >= i.global_end and i.global_end != -1) or it in i.must_not_play:
				i.stop_playing_notes()
				i.add_rest(self.state)
			elif it >= i.start and (it < i.end or i.end == -1):
				i.play(self.state)
			elif it == i.end and i.step != 0:
				i.stop_playing_notes()
				diff = i.end - i.start
				i.start = i.end + i.step
				i.end = i.start + diff
				i.add_rest(self.state)
			else:
				i.stop_playing_notes()
				i.add_rest(self.state)


	def play(self):
		"""Loops until self.play_iterations iterations """
		"""have been played."""

		while self.play_iterations >= 0:
			i = 0
			self.tick_start = time()
			self.iteration()
			while i < len(self.chords) * self.ticks:

				if i != 0:
					self.tick_start = time()
				if i / self.ticks != self.chord_index:
					self.chord_index = i / self.ticks
					self.bar_tick()
				self.chord = self.chords[ self.chord_index ]

				
				self.change_state(i)
				if self.tick_function != None:
					self.tick_function(self.state)
				self.play_instruments()

				if self.update_function != None:
					self.update_function()

				self.block_tick()
				i += 1
		self.block.stop()
		if not self.get_next_block():
			for i in self.instruments:
				i.stop()
			self.output_midi()
		else:
			self.play()

	def output_midi(self):
		c = Composition()
		print 
		print "Writing MIDI file %s..." % self.output_file
		for s in self.instruments:
			if hasattr(s, 'bar'):
				s.track + s.bar
			c.add_track(s.track)
		
		MidiFileOut.write_Composition(self.output_file, c, self.bpm , 0)


	def replace_scale_note(self, note):
		s = self.state["scale"]
		for n in s:
			if n[0] == note[0]:
				s[ s.index(n) ] = note
				return
		s.append(note)

	def reset_state(self):
		self.state = {
			'chord': [],
			'chords': [], 
			'progression': self.progression, 
			'progression_index': 0, 
			'iteration_tick': 0,
			'bpm': self.bpm, 
			'tick': 0, 
			'meter': self.meter, 
			'resolution': self.resolution, 
			'key': self.key,
			'scale': diatonic.get_notes(self.key), 
			'wild': self.block.get_wildness(0,0),
			'tick_function': self.tick_function,
			'paint_function': self.paint_function,
			'update_function': self.update_function,
			'swing': self.block.swing,
			}


	def set_bpm(self, bpm):
		self.bpm = bpm
		self.tick_length = (60.0 / bpm) / (self.resolution / \
				float(self.meter[1]))


	def set_progression(self, progression):
		self.progression = progression

	def sync(self):
		# Execution time of current tick
		if self.no_fluidsynth:
			return
		exec_time = time() - self.tick_start

		tick_length = self.block.get_tick_length(self.tick, \
				self.tick_length)
		if exec_time > tick_length:
			if self.verbose:
				print "Tick Overflow!"
			# Should tick be skipped?
		else:
			tick_length -= exec_time
		try:
			sleep(tick_length)
		except KeyboardInterrupt:
			self.block.stop()
			self.output_midi()
			sys.exit(0)

	def stop(self):
		for instr in self.instruments:
			instr.stop()
