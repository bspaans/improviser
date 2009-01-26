#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from qtGUI.MainWindow import ImproviserMainWindow
from qtGUI.PreferencesDialog import PreferencesDialog
from FileCollection import FileCollection
from sys import argv

def show_main(params):
	i = ImproviserMainWindow()
	i.loggedin = params["login"]
	i.default_folder = params["default_folder"]

	i.credentials = {"username": params["username"], 
			 "password": params["password"]}
	fc = FileCollection(i.default_folder)
	fc.credentials = i.credentials
	fc.loggedin = i.loggedin
	fc.checkupdates = params["checkupdates"]
	i.filecollection = fc

	if 'soundfont' not in params:
		i.no_fluidsynth = True
		i.soundfont = ''
		i.driver = ''
	else:
		i.no_fluidsynth = False
		i.soundfont = params["soundfont"]
		i.driver = params["driver"]
	i.connect_widgets()
	i.showMaximized()

app = QtGui.QApplication(argv)
p = PreferencesDialog(show_main)
p.show()
app.exec_()


