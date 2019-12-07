#!/usr/bin/python -u

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--serverIP", help="IP address of the server, including port", required=True)
parser.add_argument("-m", "--playerMAC", help="MAC address of the client", required=True)
parser.add_argument("-n", "--usbDevice", help="name of the usb device", required=True)
args = parser.parse_args()


import requests, time


originalPlayerName = "testPlayer"
originalPowerState = True
originalPlayState = True
originalVolume = 50

serverIP = args.serverIP
playerMAC = args.playerMAC
usbDevice = args.usbDevice
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



import evdev, time

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
device = False
while not device:
	try:
		device = [x for x in devices if x.name == usbDevice][0]
	except:
		print("no hid combo found")
		time.sleep(1)

print("Monitoring %s for volume up/down or pause signals" % usbDevice)

evdev.device.KbdInfo(repeat=.3,delay=100100)

for event in device.read_loop():
	if event.type == evdev.ecodes.EV_KEY and event.value == 1:
		if event.code == evdev.ecodes.KEY_VOLUMEDOWN:
        		print("volume down")
        		playerVolume = changeVolume(playerName, playerVolume, -volumeStep)
		elif event.code == evdev.ecodes.KEY_VOLUMEUP:
       		 	print("volume up")
        		playerVolume = changeVolume(playerName, playerVolume, volumeStep)
		elif event.code == evdev.ecodes.KEY_MUTE:
        		print("mute %s" % "on" if playState else "off")
        		playState = togglePlayState(playerName, playState)


