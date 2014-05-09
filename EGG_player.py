#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.phonon import *
import time

app = QApplication(sys.argv)
app.setApplicationName("EGG player")

plik="/home/marek/Wideo/d.avi"
zrodlo=Phonon.MediaSource(plik)
mediaObject = Phonon.MediaObject()
videoWidget = Phonon.VideoWidget()
Phonon.createPath(mediaObject, videoWidget)
mediaObject.setQueue(zrodlo)

mediaObject.play()
mediaObject.setVisible(True)


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
		
#if __name__ == '__main__':
	


	sys.exit(app.exec_())
