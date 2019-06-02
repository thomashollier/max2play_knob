#!/anaconda3/bin/python
import serial, requests

#
# For testing
# Created two communicating serial ports like this:
# socat -d -d pty,raw,echo=0,crnl pty,raw,echo=0,crnl
# Created temp values, will come from pinging LMS
#

originalPlayerName = "testPlayer"
originalPowerState = True
originalPlayState = True
originalVolume = 50


blah blas

serverIP = "192.168.11.3:9000"
playerMAC = "b8:27:eb:17:25:b1"
port = "/dev/ttys002"
ser = serial.Serial(port)
volumeStep = 5

def getPlayerName():
	return originalPlayerName 

def getPowerState(playerName):
	return originalPowerState

def getPlayState(playerName):
	return originalPlayState

def getVolume(playerName):
	return originalVolume 

def togglePlayState(playerName, playState):
	url = "http://%s/status.html" % serverIP
	params = {"p0":"pause", "player":playerMAC}
	r = requests.get(url, params)
	print(r.request.url)
	if playState:
		return False
	else:
		return True

def changeVolume(playerName, playerVolume, v):
	url = "http://%s/status.html" % serverIP
	params = {"p0":"mixer", "p1":"volume", "p2":"%s%s"%("+" if v>0 else "",v), "player":playerMAC}
	r = requests.get(url, params)
	print(r.request.url)
	return playerVolume + v



playerName = getPlayerName()
powerState = getPowerState(playerName)
playState = getPlayState(playerName)

if powerState:
	playerVolume = getVolume(playerName)
	print("Player %s is %s paused and volume is set to %s\n" % (playerName, "" if playState else "not", playerVolume))
	while (1):
		message = ser.readline().rstrip()
		if message == b"Pressed":
			playState = togglePlayState(playerName, playState)
		elif message == b"Up":
			playerVolume = changeVolume(playerName, playerVolume, volumeStep)
		elif message == b"Down":
			playerVolume = changeVolume(playerName, playerVolume, -volumeStep)
		else:
			print("Unrecognized message")
		print("Player %s is %s paused and volume is set to %s\n" % (playerName, "" if playState else "not", playerVolume))


