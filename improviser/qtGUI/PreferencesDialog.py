from PyQt4 import QtCore, QtGui
from qtGUI.UI.preferencesDialog import Ui_preferencesDialog
from os import environ, path
import urllib
import md5
import Options

class PreferencesDialog(QtGui.QDialog):

	def __init__(self, show_main):
		QtGui.QDialog.__init__(self)
		self.show_main = show_main
		self.ui = Ui_preferencesDialog()
		self.ui.setupUi(self)
		self.setup()
		self.try_load_from_file()

	def setup(self):
		h = "/home"
		for x in ['HOMEPATH', 'HOME']:
			if x in environ:
				self.default_folder = environ[x]


		for x in ['default', 'alsa', 'oss', 'jack', 'portaudio', 'coreaudio', 
				'sndmgr', 'Direct Sound']:
			self.ui.driver.addItem(x)

		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			self.open_window)

		self.connect(self.ui.browsebutton,
			QtCore.SIGNAL("clicked()"),
			self.load_dialog)

		self.connect(self.ui.browsefolder,
			QtCore.SIGNAL("clicked()"),
			self.load_folder_dialog)

		self.connect(self.ui.no_fluidsynth,
			QtCore.SIGNAL("stateChanged(int)"),
			lambda x: self.ui.browsebutton.setEnabled(not(x)) or \
					self.ui.driver.setEnabled(not(x)))

		self.connect(self.ui.nologin,
			QtCore.SIGNAL("stateChanged(int)"),
			lambda x: self.ui.username.setEnabled(not(x)) or \
					self.ui.password.setEnabled(not(x)))

	def try_load_from_file(self):
		if "HOME" in environ:
			f = path.join(environ["HOME"], ".improviser")
			if path.exists(f):
				try:
					fp = open(f, "r")
					for x in fp.readlines():
						option = x[:-1]
						parts = option.split(":")
						key = parts[0]
						if key == "soundfont":
							self.ui.soundfont.setText(":".join(parts[1:]))
						elif key == "driver":
							i = combo_index_by_text(self.ui.driver, "".join(parts[1:]))
							self.ui.driver.setCurrentIndex(int(i))
						elif key == "no_fluidsynth":
							if parts[1] == "1":
								self.ui.browsebutton.setEnabled(False)
								self.ui.driver.setEnabled(False)
								self.ui.no_fluidsynth.setChecked(True)
						elif key == "nologin":
							if parts[1] == "1":
								self.ui.username.setEnabled(False)
								self.ui.password.setEnabled(False)
								self.ui.nologin.setChecked(True)
						elif key == "checkupdates":
							if parts[1] == "1":
								self.ui.checkupdates.setChecked(True)
						elif key == "folder":
							self.ui.folder.setText(":".join(parts[1:]))
							self.default_folder = ":".join(parts[1:])
						elif key == "user":
							self.ui.username.setText(":".join(parts[1:]))
						elif key == "pass":
							self.ui.password.setText(":".join(parts[1:]))
					fp.close()
				except:
					pass

	def try_save_file(self):
		if "HOME" in environ:
			f = path.join(environ["HOME"], ".improviser")
			try:
				fp = open(f, "w")
				fp.write("soundfont:%s\n" % self.ui.soundfont.text())
				fp.write("driver:%s\n" % self.ui.driver.currentText())
				fp.write("no_fluidsynth:%d\n" % self.ui.no_fluidsynth.isChecked())
				fp.write("user:%s\n" % self.ui.username.text())
				fp.write("pass:%s\n" % self.ui.password.text())
				fp.write("nologin:%d\n" % self.ui.nologin.isChecked())
				fp.write("folder:%s\n" % self.ui.folder.text())
				fp.write("checkupdates:%d\n" % self.ui.checkupdates.isChecked())
				fp.close()
			except:
				pass


	def login(self):

		if self.ui.nologin.isChecked():
			return False
		if str(self.ui.username.text()) == "" or str(self.ui.password.text()) == "":
			q = QtGui.QMessageBox.warning(self, "Error", "Empty username and/or password", 1, 0)
			return False

		params = urllib.urlencode({"name": str(self.ui.username.text()),
			"pass": md5.new(str(self.ui.password.text())).hexdigest()})

		

		try:
			f = urllib.urlopen(Options.UPLOAD_HOME + "login.php?%s" % params)
		except:
			q = QtGui.QMessageBox.critical(self, "Error", "Could not connect to the site.", 1, 0)
			return False
		res = f.read()
		f.close()

		if res == "":
			q = QtGui.QMessageBox.critical(self, "Error", "Empty response from server.", 1, 0)
			return False


		keyword = res.split()[0]
		msg = " ".join(res.split()[1:])

		if keyword == "OK":
			return True
		elif keyword == "NEW":
			q = QtGui.QMessageBox.information(self, "Success", "Created new account '%s'" % str(self.ui.username.text()), 1, 0)
			return True
		elif keyword == "INVALID":
			q = QtGui.QMessageBox.warning(self, "Error", str(msg), 1, 0)
			return False
		elif keyword == "ERROR":
			q = QtGui.QMessageBox.critical(self, "Error", str(msg), 1, 0)
			return False
		
		q = QtGui.QMessageBox.critical(self, "Error", "Invalid response from server.", 1, 0)
		return False


	def toggle_enabled(self):
		if self.ui.no_fluidsynth.isChecked():
			self.ui.browsebutton.enabled()
		else:
			self.ui.browsebutton.enabled()



	def open_window(self):
		soundfont = str(self.ui.soundfont.text())
		driver = str(self.ui.driver.currentText())
		no_fluidsynth = int(self.ui.no_fluidsynth.isChecked())
		self.try_save_file()

		params = { "default_folder": self.default_folder,
			   "checkupdates": self.ui.checkupdates.isChecked(),
			   "username": str(self.ui.username.text()),
			   "password": str(self.ui.password.text()),
			   "login": self.login() }

		if not params['login']:
			if not self.ui.nologin.isChecked():
				return

		if no_fluidsynth:
			self.show_main(params)
			self.reject()
		else:
			if soundfont != "":
				params["soundfont"] = soundfont
				params["driver"] = driver
				self.show_main(params)
				self.reject()

	def load_dialog(self):
		f = QtGui.QFileDialog()
		s = f.getOpenFileName(self, "Load soundfont.",
				self.default_folder, "Soundfont (*.sf2)")
		if s != "":
			self.ui.soundfont.setText(s)

	def load_folder_dialog(self):
		f = QtGui.QFileDialog()
		f.setFileMode(QtGui.QFileDialog.DirectoryOnly)
		s = f.getExistingDirectory(self, "Select folder.", self.default_folder)

		if s != "":
			self.ui.folder.setText(s)
			self.default_folder = s



def combo_index_by_text(combo, text):
	for x in range(combo.count()):
		if combo.itemText(x) == text:
			return x
	return -1
