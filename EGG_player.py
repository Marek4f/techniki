#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.phonon import *
import time



class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(QtGui.QMainWindow, self).__init__()
	
		plik="/home/marek/Wideo/d.avi"
		player=Phonon.VideoPlayer(Phonon.VideoCategory)
		zrodlo=Phonon.MediaSource(plik)
		self.mediaObject = Phonon.MediaObject(self)
		self.videoWidget = Phonon.VideoWidget(self)
		Phonon.createPath(self.mediaObject, self.videoWidget)

		player.play(zrodlo)
		player.setVisible(True)
		

		while True:
			s=input("ttttt")
			if s==1:
				player.pause()
			elif s==2:
				player.play(zrodlo)
			elif s==3:
				player.stop()
			elif s==4:
				if not self.videoWidget.isFullScreen():
					self.videoWidget.enterFullScreen()
					self.videoWidget.showFullScreen()
			else:
				self.videoWidget.exitFullScreen()
				
if __name__ == '__main__':
	while True:
		app = QApplication(sys.argv)
		app.setApplicationName("EGG player")
		egg=MainWindow()
		egg.show()
		if s==4:
			egg.show()
	sys.exit(app.exec_())
