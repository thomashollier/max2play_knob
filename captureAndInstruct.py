#!/anaconda3/bin/python


import serial, requests, time

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

serverIP = "192.168.11.3:9000"
playerMAC = "b8:27:eb:17:25:b1"
port = "/dev/ttys002"
#ser = serial.Serial(port)
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
playerVolume = getVolume(playerName)

from pynput.keyboard import Key, Listener

def on_press(key):
    if str(key) == "'D'":
        print("down")
        changeVolume(playerName, playerVolume, -volumeStep)
    elif str(key) == "'U'":
        print("up")
        changeVolume(playerName, playerVolume, volumeStep)
    elif str(key) == "'P'":
        print("mute")
        togglePlayState(playerName, playState)

def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    playerName = getPlayerName()
    powerState = getPowerState(playerName)
    playState = getPlayState(playerName)
    playerVolume = getVolume(playerName)
    listener.join()
