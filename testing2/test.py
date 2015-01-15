import time, os

GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME = "gpio"

HIGH = "1"
LOW = "0"
INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"

led_pin_mode = os.path.join(GPIO_MODE_PATH, 'gpio'+str(7))
button_pin_mode = os.path.join(GPIO_MODE_PATH, 'gpio'+str(12))

led_pin = os.path.join(GPIO_PIN_PATH, 'gpio'+str(7))
button_pin = os.path.join(GPIO_PIN_PATH, 'gpio'+str(12))

## Setting pin modes
file = open(led_pin_mode, 'r+')
file.write(OUTPUT)
file.close()

file = open(button_pin_mode, 'r+')
file.write(INPUT_PU)
file.close()

## set LED to low at start
file = open(led_pin, 'r+')
file.write(LOW)
file.close()
