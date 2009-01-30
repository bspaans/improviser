import os.path as path
import Options
import xml.dom.minidom as minidom
from xml.dom.minidom import Document
import Progressions
import Bands

class FileCollection:

	folder = ""
	credentials = {}
	progressions = []
	instruments = []
	songs = []
	blocks = []
	checkupdates = False
	last_ID = {}


	def __init__(self, folder):
		self.folder = folder
		for x in [Options.UPLOAD_PROGRESSION, Options.UPLOAD_SONG, Options.UPLOAD_INSTRUMENTS, Options.UPLOAD_BLOCKS]:
			self.last_ID[x] = 0
		self.setup()

	def setup(self):
		if not path.exists(self.folder):
			return

		if path.exists(self.folder + "content.xml"):
			self.load()


	def get(self, content_type, only_defaults = False, parse_content = True):
		if content_type == Options.UPLOAD_PROGRESSION:
			return self.get_Progressions(only_defaults, parse_content)
		elif content_type == Options.UPLOAD_INSTRUMENTS:
			return self.get_Instruments(only_defaults, parse_content)

	def get_Progressions(self, only_defaults = False, parse_content = True):
		defaults = {"Empty": ""}

		# Gather default (builtin) progressions.
		for x in Options.get_available_progressions():
			prog = Options.progression_to_string(getattr(Progressions, x))[1:-1]
			if not parse_content:
				defaults[x] = "%s { %s }" % (x, prog)
			else:
				defaults[x] = prog

		if only_defaults:
			return defaults
		res = {}

		for x in self.progressions:
			if not res.has_key(x[2]):
				res[x[2]] = {}

			# Parse progressions in x[5]
			for p in x[5].split(","):
				if not res[x[2]].has_key(x[3]):
					res[x[2]][x[3]] = ""
				if parse_content:
					params = p.split(" ")
					name = params[0]
					params = " ".join(params[1:])[1:-1]
					res[x[2]][x[3]] += params
				else:
					res[x[2]][x[3]] += p + ","

			# Remove comma
			if not parse_content:
				res[x[2]][x[3]] = res[x[2]][x[3]][:-1]



		res['Default'] = defaults
		return res

	def get_Instruments(self, only_defaults = False, parse_content = True):
		defaults = {}

		# Default built in instruments and ensembles
		for x in Options.get_available_bands():
			bands = getattr(Bands, x)
			defaults[x] = ""
			for i in bands:
				if parse_content:
					defaults[x] += i.__class__.__name__ + " "
				else:
					par = ""
					for p in i.params:
						r = str(i.params[p])
						if r == "True":
							r = "1"
						elif r == "False":
							r = "0"
						par += "%s:%s " % (p, r)

					defaults[x] += "%s { %s}," %  (i.__class__.__name__, par)


		if only_defaults:
			return defaults

		res = {}
		for x in self.instruments:
			if not res.has_key(x[2]):
				res[x[2]] = {}

			# Parse instruments in x[5]
			for p in x[5].split(","):
				if not res[x[2]].has_key(x[3]):
					res[x[2]][x[3]] = ""
				if parse_content:
					params = p.split(" ")
					name = params[0]
					params = " ".join(params[1:])[1:-1]

					res[x[2]][x[3]] += name + " "
				else:
					res[x[2]][x[3]] += p + ","

			# Remove comma
			if not parse_content:
				res[x[2]][x[3]] = res[x[2]][x[3]][:-1]

		res['Default'] = defaults
		return res


	def add(self, content_type, id, author, title, description, content):
		if content_type == Options.UPLOAD_PROGRESSION:
			return self.add_Progression(id, author, title, description, content)
		elif content_type == Options.UPLOAD_INSTRUMENTS:
			return self.add_Instrument(id, author, title, description, content)

	def add_Progression(self, id, author, title, description, content):
		for x in self.progressions:
			if x[0] == id:
				return
		self.progressions.append([id, Options.UPLOAD_PROGRESSION, author, title, description, content])

	def add_Instrument(self, id, author, title, description, content):
		for x in self.instruments:
			if x[0] == id:
				return
		self.instruments.append([id, Options.UPLOAD_INSTRUMENTS, author, title, description, content])
	def save(self):
		if not path.exists(self.folder):
			#warning Messagebox
			return False

		doc = Document()
		content = doc.createElement("content")
		doc.appendChild(content)
		for x in self.progressions + self.instruments + self.songs + self.blocks:
			prog = doc.createElement("item")
			prog.setAttribute("id", str(x[0]))
			prog.setAttribute("content_type", str(x[1]))
			content.appendChild(prog)

			author = doc.createElement("author")
			prog.appendChild(author)
			atext = doc.createTextNode(x[2])
			author.appendChild(atext)

			title = doc.createElement("title")
			prog.appendChild(title)
			ttext = doc.createTextNode(x[3])
			title.appendChild(ttext)

			description = doc.createElement("description")
			prog.appendChild(description)
			ttext = doc.createTextNode(x[4])
			description.appendChild(ttext)

			item_content = doc.createElement("item_content")
			prog.appendChild(item_content)
			ttext = doc.createTextNode(x[5])
			item_content.appendChild(ttext)

		result = doc.toxml()
		try:
			f = open(self.folder + "content.xml", "w")
			f.write(result)
			f.close()
		except:
			#warning Messagebox
			return False
		return True


	def load(self):
		self.progressions = []

		p = minidom.parse(self.folder + "content.xml")
		for x in p.getElementsByTagName("item"):
			id = int(x.getAttribute("id"))
			content_type = int(x.getAttribute("content_type"))

			author = x.getElementsByTagName("author")[0].childNodes[0].data
			title = x.getElementsByTagName("title")[0].childNodes[0].data
			description = x.getElementsByTagName("description")[0].childNodes[0].data
			content = x.getElementsByTagName("item_content")[0].childNodes[0].data


			lst = None
			if content_type == Options.UPLOAD_PROGRESSION:
				lst = self.progressions
			elif content_type == Options.UPLOAD_INSTRUMENTS:
				lst = self.instruments
			elif content_type == Options.UPLOAD_SONG:
				lst = self.songs
			elif content_type == Options.UPLOAD_BLOCKS:
				lst = self.blocks
			else:
				#warning throw exception
				break

			if lst is not None:
				lst.append([id, content_type, author, title, description, content])
	
				if id > self.last_ID[content_type]:
					self.last_ID[content_type] = id


