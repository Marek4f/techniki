import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

app = QtCore.QCoreApplication(sys.argv)
app.setApplicationName("my_player")

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(QtGui.QMainWindow, self).__init__()
		
		self.playlist = []
		self.setApplicationName("my_player")

		for file in os.listdir("/home/marek/Muzyka"):
			if file.endswith(".mp3"):
				self.playlist.append(Phonon.MediaSource(str(file)))
		self.player = Phonon.createPlayer(Phonon.MusicCategory, playlist[0])
		#~ player.play()
	def play():
		self.player.play()

	def setupUi(self):
		bar = QtGui.QToolBar()

        bar.addAction(self.playAction)
        bar.addAction(self.pauseAction)
        bar.addAction(self.stopAction)

        self.seekSlider = Phonon.SeekSlider(self)
        self.seekSlider.setMediaObject(self.mediaObject)

        self.volumeSlider = Phonon.VolumeSlider(self)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum,
                QtGui.QSizePolicy.Maximum)
  
        volumeLabel = QtGui.QLabel()
        volumeLabel.setPixmap(QtGui.QPixmap('images/volume.png'))

player = MainWindow()

while True:
	s=input("ttttt")
	if s==1:
		player.pause()
	elif s==2:
		player.play()
	elif s==3:
		player.stop()
app.exec_()
