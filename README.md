# max2play_knob

<H3>rotaryKnobHID.ino</H3>
This is an arduino sketch that uses a digispark board and a rotary encoder as a volume knob and pause toggle for a max2play squeezelite client. This uses the Adafruit trinket HID library.


<H3>Usbvolumeknob.tar</H3>
A working version of a max2play plugin to use the volume knob above and send command to the server.
<LI>Uses python evdev library to capture events from usb HID device
<LI>Uses requests library to send appropriate http commands to logitec server
<LI>Install script creates a systemd service to run the python script

<H3>Misc</H3>
Dead ends and broken branches.

