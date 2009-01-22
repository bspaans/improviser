from Block import Block
from time import sleep
import Arduino

class ArduinoBlock(Block):

	def __init__(self):
		self.arduino = Arduino.Arduino()

	def get_bpm(self, iterations, tick):
		i = self.arduino.get_last()[0]
		self.bpm = i / 4 + 50
		return self.bpm

	def get_wildness(self, iteration, tick):
		i = self.arduino.get_last()[1]
		self.wildness = i / 512.0 * (self.arduino.get_last()[3] / 512.0)
		return self.wildness

	def get_resolution(self, iteration):
		i = self.arduino.get_last()[2]
		if i > 512:
			self.resolution = 8
		else:
			self.resolution = 4
		return self.resolution

	def stop(self):
		self.arduino.buf.stop = True
		sleep(0.1)
