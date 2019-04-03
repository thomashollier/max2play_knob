# max2play_knob

<H3>rotaryKnobUSB.ino</H3>
Uses a digispark and a rotary encoder as a volume knob for a max2play squeezelite client.

<H3>captureAndInstruct.py</H3>
<LI>Uses adafruit's TrinketKeyboard library for arduino
<LI>Uses pynput library to capture the digispark's key presses
<LI>Uses requests library to send http commands to logitec server

<H3>readEncoder.py</H3>
This doesn't work with digispark because it doesn't provide a serial interface but it should work if you use a micro controller that does.
