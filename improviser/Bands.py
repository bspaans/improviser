from Musicians import *
from random import randrange

"""

	Possible instrument parameters:

		channel		=	MIDI channel
		min_velocity	=	Minimum volume [0-128]
		max_velocity	=	Maximum volume [0-128]
		chance		~= 	Chance to play on tick
		end		 = 	Iteration to end on, default: 0
		start		 = 	Iteration to start on, default: 0
		step 		=	Iterations to wait after end



"""


dummy_parameters = {'channel': 1}

dummy = [
	SlowStridePianist({'max_velocity': 80, 'start': 0, 'step': 2 }),
	FastStridePianist({'max_velocity': 80, 'start': 2, 'step': 2}),
	RockDrum({'start': 0}),
	#JazzDrum({'start': 8, 'end': 12}), 
	BassInstrument({'channel':1, 'start': 1}),
	ChordInstrument({'channel':7, 'chance': 0.15, \
			 'max_velocity': 70, 'start': 2}), 
	SoloInstrument({'channel':1, 'start': 4, 'end': 8, 'chance': 0.2, 
			'step': 4}),
	SoloInstrument({'channel':11, 'start': 8, 'end': 12, 'step':2}),
	SoloInstrument({'channel':12, 'start': 4, 'end': 8, 'step':4}),
	SoloInstrument({'channel':7, 'start': 16, 'end': 20, 'step': 4})
	 ]

swing = [
	ChordInstrument({'channel':7, 'chance': 0.15, 'max_velocity': 70}), 
	SlowStridePianist({'channel': 2, 'max_velocity': 80}),
	RockDrum({'start': 0}),
	SoloInstrument({'channel':11, 'midi_instr': 66, 'start': 0, 'step': 4}),
	SoloInstrument({'channel':12, 'midi_instr': 11, 'start': 4, 'step': 4}),
	BassInstrument({'channel':5, 'midi_instr':36, 'let_ring': True}),
	SimpleChordInstrument({'channel': 1, 'start': 1, 'midi_instr': 49, 'step': 1}), 
	]

weird = [
	SlowStridePianist({'channel': 1, 'start': 4}),
	ChromaticSoloist({'channel': 2, 'midi_instr': 108, 'start': 0, 'step': 4}),
	ChromaticSoloist({'channel': 3, 'midi_instr': 30, 'start': 2, 'end': 8, 'step': 2}),
	BassInstrument({'channel':4, 'midi_instr':36, 'let_ring': True, 'start': 6}),
	SoloInstrument({'channel':5, 'midi_instr':41, 'start': 6, 'end': 8, 'step': 6}),
	ChordInstrument({'channel':6, 'chance': 0.25, 'max_velocity': 70, 'midi_instr': 10, 'start': 0, 'step': 4}), 
	RockDrum({'start': 8, 'step': 8}),
	JazzDrum({'start': 0, 'step': 8}),
	]

soothing = [
	SoloInstrument({'channel': 3, 'midi_instr': 25, 'start': 4, 'end': 8, 'step': 4}),
	WalkingBass({'channel':4, 'start': 0}),
	ChordInstrument({'channel':5, 'chance': 0.25, 'max_velocity': 70, 'midi_instr': 6, 'start': 0, 'step': 4}), 
	ChromaticSoloist({'channel': 6, 'midi_instr': 21, 'start': 8, 'end': 12, 'step': 4}),
	PowerChords({'channel': 7, 'midi_instr': 30, 'start': 8, 'end': 12, 'step': 4}),
	FastStridePianist({'channel': 8, 'midi_instr': 1, 'max_velocity': 80, 'start': 20, 'step': 4}),
	RockDrum({'start': 4}),
	]

none = []

boogie = [
	BoogieWoogieRhythm({'channel': 1, 'midi_instr': randrange(25, 31)}),
	BoogieWoogieRhythm({'channel': 2, 'midi_instr': randrange(1, 10)}),
	RockDrum({}),
	SoloInstrument({'channel':11, 'midi_instr': randrange(25, 90)}),
	BassInstrument({'channel':5, 'midi_instr':36, 'let_ring': True}),
	]

rocknroll= [
	BoogieWoogieRhythm({'channel': 1, 'midi_instr': 29, 'start':2, 'step': 2}),
	BoogieWoogieRhythm({'channel': 3, 'midi_instr': 30, 'start': 4, 'step': 2}),
	BoogieWoogieRhythm({'channel': 2, 'midi_instr': 4, 'start': 0}),
	RockDrum({}),
	SoloInstrument({'channel':11, 'midi_instr': 30}),
	BassInstrument({'channel':5, 'midi_instr':36, 'let_ring': True}),
	Strings({'channel': 6, 'start': 4, 'midi_instr': 49, 'step': 4, 'let_ring': True}), 
	]

metal = [
	BlastBeat({'max_velocity': 80}),
	PowerChords({'channel': 7, 'midi_instr': 30}),
	ChromaticSoloist({'channel':6, 'midi_instr': 29, 'max_velocity':80, 'start': 0, 'step':4}),
	ChromaticSoloist({'channel':8, 'midi_instr': 28, 'max_velocity':80, 'start': 4, 'step':4}),
	BassInstrument({'channel':5, 'midi_instr':36}),
	Strings({'channel': 1, 'start': 4, 'midi_instr': 49, 'step': 4, 'let_ring': True}), 
	Strings({'channel': 1, 'start': 8, 'midi_instr': 30, 'step': 4, 'let_ring': True}), 
	]

jazz = [
	SimpleChordInstrument({'channel': 1}),
	BassInstrument({'channel': 2, 'start': 0, 'let_ring': True}),
	SlowStridePianist({'channel': 3, 'start':0, 'step': 4, 'max_velocity': 70}),
	ChordInstrument({'channel': 4, 'max_velocity': 70, 'chance': 0.5, 'start': 4, 'midi_instr': 1}),
	FastStridePianist({'channel': 5, 'start':4, 'step': 4}),
	RockDrum({}),
	SoloInstrument({'midi_instr': 11, 'channel': 11, 'start': 0, 'step': 4}),
	SoloInstrument({'midi_instr': 66,'channel': 15, 'start': 4, 'stop': 8, 'step': 4, 'max_velocity': 80}),
	]

jazz2 = [
	SoloInstrument({'channel': 0, 'midi_instr': randrange(20,100), 'step': 6}),
	SoloInstrument({'channel': 1, 'midi_instr': randrange(80,100), 'start': 4, 'step': 4}),
	FastStridePianist({'channel': 5, 'start':0}),
	JazzDrum({'start': 2}),
	WalkingBass({'start': 4, 'channel': 4}),
	]

jazz_quartet = [
	JazzDrum({}),
	WalkingBass({'channel': 8}),
	ChordInstrument({'channel': 10, 'midi_instr': 1}),
	SoloInstrument({'channel': 11, 'midi_instr': 2, 'max_velocity':70, 'step': 1, 'start': 1, 'chance': 0.7}),
	SoloInstrument({'channel':12, 'midi_instr': 66, 'start': 0, 'step': 1, 'chance': 0.7}),
	]

jazz_battle = [
	JazzDrum({}),
	WalkingBass({'channel': 8, 'start': 0}),
	ChordInstrument({'channel': 10, 'midi_instr': 1}),
	SoloInstrument({'channel': 11, 'midi_instr': 2, 'max_velocity':70, 'step': 1, 'start': 1, 'chance': 0.7}),
	SoloInstrument({'channel':12, 'midi_instr': 66, 'start': 0, 'step': 1, 'chance': 0.7}),
	SoloInstrument({'channel':13, 'midi_instr': 11, 'start': 8, 'step': 4, 'chance': 0.7}),
	]

serbitat1 = [
	JazzDrum({}),
	FastStridePianist({'channel': 11}),
	Strings({'channel': 3, 'start': 1, 'step': 1}),
	Strings({'channel': 4, 'start': 0, 'midi_instr': 52}),
	SoloInstrument({'channel': 0, 'midi_instr': 65, 'step': 4, 'start': 4,}),
	SoloInstrument({'channel': 5, 'midi_instr': 40, 'step': 4, 'start': 0, 'max_velocity': 110}),
	]

serbitat2 = [
	JazzDrum({'start': 0}),
	ChordInstrument({'channel': 11, 'midi_instr': 6}),
	Strings({'channel': 3, 'start': 5, 'step': 1}),
	Strings({'channel': 4, 'start': 4, 'midi_instr': 52}),
	SoloInstrument({'channel': 0, 'midi_instr': 65, 'step': 4, 'start': 4,}),
	SoloInstrument({'channel': 5, 'midi_instr': 40, 'step': 4, 'start': 8, 'max_velocity': 110}),
	SoloInstrument({'channel': 6, 'midi_instr': 41, 'start': 1, 'end': 4,  'max_velocity': 110}),
	WalkingBass({'channel': 7, 'midi_instr': 32, 'start': 2})
	]

serbitat3 = [
	BlastBeat({'start': 0}),
	PowerChords({'channel': 5, 'midi_instr': 30, 'start': 0}),
	SimpleChordInstrument({'channel': 11, 'midi_instr': 6}),
	BassInstrument({'channel': 6, 'midi_instr': 33}),

	SoloInstrument({'channel': 7, 'midi_instr': 27, 'step': 4, 'start': 8, 'max_velocity': 110}),
	SoloInstrument({'channel': 8, 'midi_instr': 29, 'start': 4, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 10, 'midi_instr': 61, 'start': 0, 'max_velocity': 127, 'min_velocity': 100})


	]

serbitat4 = [
	ChromaticSoloist({'channel': 10, 'midi_instr': 60, 'start': 0, 'max_velocity': 127, 'min_velocity': 100}),
	ChordInstrument({'channel': 11, 'midi_instr': 1, 'chance':0.4}),
	JazzDrum({'start': 0}),
	Strings({'channel': 4, 'start': 0, 'midi_instr': 52}),
	SoloInstrument({'channel': 7, 'midi_instr': 46, 'step': 6, 'start': 4, 'max_velocity': 110}),
	SoloInstrument({'channel': 8, 'midi_instr': 45, 'start': 4, 'step': 4,  'max_velocity': 110}),
	BoogieWoogieRhythm({'channel': 2, 'midi_instr': 4, 'start': 0}),
	SlowSoloist({'channel': 12, 'midi_instr': 61}),
	BassInstrument({'channel': 6, 'midi_instr': 33}),

	]

serbitat5 = [
	RandomSoloist({'channel': 1, 'midi_instr': 11}),
	RandomSoloist({'channel': 2, 'midi_instr': 1}),
	RandomSoloist({'channel': 3, 'midi_instr': 6}),
	RandomSoloist({'channel': 4, 'midi_instr': 7}),
	RandomSoloist({'channel': 5, 'midi_instr': 8}),
	RandomSoloist({'channel': 6, 'midi_instr': 9}),
	RandomSoloist({'channel': 7, 'midi_instr': 12}),
	RandomSoloist({'channel': 8, 'midi_instr': 15}),
	BlastBeat({'start': 0}),
	RandomSoloist({'channel': 10, 'midi_instr': 17}),
	RandomSoloist({'channel': 11, 'midi_instr': 72}),
	]

serbitat6 = [
	Snare({'start': 0, 'end': 4}),
	RandomSoloist({'channel': 10, 'midi_instr': 30, 'end': 4}),
	JazzDrum({'start': 4}),
	PowerChords({'channel': 5, 'midi_instr': 30, 'start': 4}),
	ChordInstrument({'channel': 11, 'midi_instr': 1, 'chance':0.4}),
	Strings({'channel': 4, 'start': 4, 'midi_instr': 52}),
	SoloInstrument({'channel': 6, 'start': 8, 'midi_instr': 29}),
	SoloInstrument({'channel': 7, 'start': 12, 'midi_instr': 25}),
	BassInstrument({'channel': 8, 'midi_instr': 33}),
	]

serbitat7 = [
	BlastBeat({'start': 0, 'step': 2}),
	JazzDrum({'start': 2, 'step': 2}),
	SoloInstrument({'channel': 0,  'midi_instr': 105}),
	ChordInstrument({'channel': 1, 'midi_instr': 110, 'start': 0}),
	BassInstrument({'channel': 2, 'midi_instr': 47, 'start': 0}),
	SlowStridePianist({'channel': 3, 'midi_instr': 1, 'start': 0}),
	Strings({'channel': 4, 'start': 0, 'midi_instr': 52}),
	SimpleSoloInstrument({'channel': 5, 'start': 0, 'midi_instr':60}),
	Strings({'channel': 6, 'start': 0, 'midi_instr': 60}),
	SimpleSoloInstrument({'channel': 10, 'start': 0, 'midi_instr': 61}),

	SimpleSoloInstrument({'channel': 7, 'start': 0, 'midi_instr': 64}),
	SoloInstrument({'channel': 8, 'midi_instr': 65, 'start': 4, 'step': 4,  'max_velocity': 110}),
	WalkingBass({'channel': 11, 'midi_instr': 35}),
	SoloInstrument({'channel': 12, 'midi_instr': 75, 'start': 8, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 13, 'midi_instr': 11, 'start': 0, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 14, 'midi_instr': 9, 'start': 4, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 15, 'midi_instr': 117, 'start': 0}),

	]

serbitat8 = [
	BlastBeat({'start': 0, 'step': 2}),
	JazzDrum({'start': 2, 'step': 2}),
	SoloInstrument({'channel': 0,  'midi_instr': 105}),
	ChordInstrument({'channel': 1, 'midi_instr': 110, 'start': 0}),
	BassInstrument({'channel': 2, 'midi_instr': 47, 'start': 0}),
	SlowStridePianist({'channel': 3, 'midi_instr': 1, 'start': 0}),
	Strings({'channel': 4, 'start': 0, 'midi_instr': 52}),
	SoloInstrument({'channel': 5, 'start': 0, 'midi_instr':60}),
	Strings({'channel': 6, 'start': 0, 'midi_instr': 60}),
	ChromaticSoloist({'channel': 10, 'start': 0, 'midi_instr': 61}),

	ChromaticSoloist({'channel': 7, 'start': 0, 'midi_instr': 64}),
	SoloInstrument({'channel': 8, 'midi_instr': 65, 'start': 4, 'step': 4,  'max_velocity': 110}),
	WalkingBass({'channel': 11, 'midi_instr': 35}),
	SoloInstrument({'channel': 12, 'midi_instr': 75, 'start': 8, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 13, 'midi_instr': 11, 'start': 0, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 14, 'midi_instr': 9, 'start': 4, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 15, 'midi_instr': 117, 'start': 0}),

	]

serbitat9 = [

	BlastBeat({'start': 0, 'step': 2}),
	JazzDrum({'start': 2, 'end': 4,  'step': 6}),
	RockDrum({'start': 6, 'end': 8, 'step': 6}),
	ChromaticSoloist({'channel': 7, 'start': 0, 'midi_instr': 64}),
	SoloInstrument({'channel': 8, 'midi_instr': 65, 'start': 4, 'step': 4,  'max_velocity': 110}),
	WalkingBass({'channel': 11, 'midi_instr': 35}),
	SoloInstrument({'channel': 12, 'midi_instr': 75, 'start': 8, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 13, 'midi_instr': 11, 'start': 0, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 14, 'midi_instr': 9, 'start': 4, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 15, 'midi_instr': 117, 'start': 0}),


	]

serbitat10 = [

	Strings({'channel': 4, 'start': 4, 'midi_instr': 52}),
	FastStridePianist({'channel': 8, 'midi_instr': 1, 'max_velocity': 80, 'start': 20, 'step': 4}),
	RandomSoloist({'channel': 10, 'midi_instr': 17}),
	ChordInstrument({'channel': 1, 'midi_instr': 105, 'start': 0}),
	ChordInstrument({'channel': 3, 'midi_instr': 110, 'start': 0}),
	BassInstrument({'channel': 2, 'midi_instr': 47, 'start': 0}),
	WalkingBass({'channel': 11, 'midi_instr': 34}),
	SoloInstrument({'channel': 14, 'midi_instr': 72, 'start': 0, 'step': 4,  'max_velocity': 110}),
	SoloInstrument({'channel': 13, 'midi_instr': 73, 'start': 0, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 15, 'midi_instr': 117, 'start': 0}),
	SimpleSoloInstrument({'channel': 7, 'start': 0, 'midi_instr': 64}),
	]

serbitat11 = [

	BlastBeat({'start': 0, 'step': 0}),
	Strings({'channel': 4, 'start': 4, 'midi_instr': 40}),
	FastStridePianist({'channel': 8, 'midi_instr': 6, 'max_velocity': 80, 'start': 20, 'step': 4}),
	SoloInstrument({'channel': 10, 'midi_instr': 41}),
	ChordInstrument({'channel': 1, 'midi_instr': 14, 'start': 0}),
	BoogieWoogieRhythm({'channel': 3, 'midi_instr': 42, 'start': 0}),
	BassInstrument({'channel': 2, 'midi_instr': 107, 'start': 0}),
	WalkingBass({'channel': 11, 'midi_instr': 7}),
	SoloInstrument({'channel': 14, 'midi_instr': 69, 'start': 2, 'step': 3,  'max_velocity': 110}),
	SoloInstrument({'channel': 13, 'midi_instr': 72, 'start': 1, 'step': 4,  'max_velocity': 110}),
	ChromaticSoloist({'channel': 15, 'midi_instr': 73, 'start': 3, 'step': 2}),
	SoloInstrument({'channel': 7, 'start': 4, 'step': 1, 'midi_instr': 64}),
	BoogieWoogieRhythm({'channel': 12, 'midi_instr': 66, 'start': 0}),
	SoloInstrument({'channel': 6, 'start': 4, 'step': 1, 'midi_instr': 67}),
	]

midi_test = [
	RockDrum({'start': 0, 'step': 1}),
	SimpleChordInstrument({'start':1, 'midi_inst': 1, 'channel': 1}),

	]
