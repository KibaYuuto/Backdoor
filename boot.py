import board
import digitalio
import storage
import supervisor

safe_pin = digitalio.DigitalInOut(board.GP0)
safe_pin.direction = digitalio.Direction.INPUT
safe_pin.pull = digitalio.Pull.UP

if safe_pin.value:
    # Pin 1 nicht mit GND verbunden → Normalbetrieb, Massenspeicher deaktivieren
    storage.disable_usb_drive()
else:
    # Pin 1 mit GND verbunden → Safe-Mode, Laufwerk anzeigen, damit Code geändert werden kann
    supervisor.disable_autoreload()
    # storage.remount("/", False)  # Optional: Schreibschutz für Dateien aufheben
