#!/usr/bin/env python
import Options


if __name__ == '__main__':
	try:
		sequencer = Options.get_sequencer_from_cli()
	except Options.OptionError, str:
		print str
	else:
		sequencer.play()
