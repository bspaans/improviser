from PyQt4 import QtCore, QtGui
from qtGUI.UI.uploadDialog import Ui_uploadDialog
import urllib
import md5
import Options

class UploadDialog(QtGui.QDialog):

	def __init__(self, content_type, content, credentials):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_uploadDialog()
		self.ui.setupUi(self)
		self.setup()
		self.params = {
			"name": credentials['username'],
			"pass": md5.new(credentials['password']).hexdigest(),
			"content": content,
			"content_type": content_type}
		self.content = content
		self.content_type = content_type

	def setup(self):
		self.connect(self.ui.buttonBox,
			QtCore.SIGNAL("accepted()"),
			self.try_upload)

	def try_upload(self):
		name = str(self.ui.uploadname.text())
		description = str(self.ui.uploaddescription.toPlainText())
		self.params['content_name'] = name
		self.params['content_description'] = description

		params = urllib.urlencode(self.params)
		try:
			f = urllib.urlopen(Options.UPLOAD_HOME + "upload.php?%s" % params)
		except:
			q = QtGui.QMessageBox.critical(self, "Error", "Could not connect to server '%s'" % Options.UPLOAD_HOME, 1, 0)
			return

		res = f.read()
		f.close()

		if res == "":
			q = QtGui.QMessageBox.critical(self, "Error", "Empty response from server '%s'." % Options.UPLOAD_HOME, 1, 0)
			return False


		keyword = res.split()[0]
		msg = " ".join(res.split()[1:])

		if keyword == "OK":
			msg = "Upload succesful!\n" + msg if msg != "" else "Upload succesful!"
			q = QtGui.QMessageBox.information(self, "Success", msg, 1, 0)
			self.reject()
			return
		elif keyword == "INVALID":
			q = QtGui.QMessageBox.warning(self, "Error", str(msg), 1, 0)
		elif keyword == "ERROR":
			q = QtGui.QMessageBox.critical(self, "Error", str(msg), 1, 0)
		else:
			q = QtGui.QMessageBox.critical(self, "Error", "Invalid response from server '%s'." % Options.UPLOAD_HOME, 1, 0)




