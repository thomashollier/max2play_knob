# max2play_knob

<H3>rotaryKnobUSB.ino</H3>
Uses a digispark and a rotary encoder as a volume knob for a max2play squeezelite client. This uses Adafruit TrinketKeyboard arduino library.

<H3>rotaryKnobHID.ino</H3>
Uses a digispark and a rotary encoder as a volume knob for a max2play squeezelite client. This uses the Adafruit trinket HID library and is the one I ended up using.


<H3>captureAndInstruct.py</H3>
<LI>Uses pynput library to capture the digispark's key press messages
<LI>Uses requests library to send appropriate http commands to logitec server

<H3>readEncoder.py</H3>
This doesn't work with digispark because it doesn't provide a serial interface but it should work if you use a micro controller that does.
