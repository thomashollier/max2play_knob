# max2play_knob

Uses a digispark and a rotary encoder as a volume knob for a max2play squeezelite client.

Uses adafruit's TrinketKeyboard library for arduino
Uses pynput library to capture the digispark's key presses
Uses requests library to send http commands to logitec server

The readEncoder.py script doesn't work with digispark because it doesn't provide a serial interface but it should work if you use a micro controller that does.
