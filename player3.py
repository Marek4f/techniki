import sys
import os
from PyQt4 import QtCore
from PyQt4.phonon import Phonon

app = QtCore.QCoreApplication(sys.argv)
app.setApplicationName("my_player")

volume = 0.5
#~ audioOutput.setVolume(volume)

index = 0
playlist = []
path = "/home/marek/Muzyka"
for file in os.listdir(path):
	if file.endswith(".mp3"):
		playlist.append(Phonon.MediaSource(path+'/'+str(file)))
		print "Dodano plik: " + path+'/'+str(file)

player = Phonon.createPlayer(Phonon.MusicCategory, playlist[index])

audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, player)
#~ Phonon.createPath(audioOutput, player)
print "Odtwarzam plik: " + str(playlist[index])
player.play()

while True:
	s=input("ttttt")
	if s==1:
		player.pause()
	elif s==2:
		player.play()
	elif s==3:
		player.stop()
	elif s==4:
		index = (index + 1) % len(playlist)
		player = Phonon.createPlayer(Phonon.MusicCategory, playlist[index])
		player.play()
	elif s==5:
		volume = volume + 0.1
		audioOutput.setVolume(volume)
		audioOutput.setMuted()
		
app.exec_()
