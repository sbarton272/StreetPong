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
x = 0
state = 'on'
## loop
while 1:
  if( x == 1000 ):
    if ( state == 'on' ):
      file = open(led_pin, 'r+')
      file.write(LOW)
      file.close()
      state = 'off'
    else:
      file = open(led_pin,'r+')
      file.write(HIGH)
      file.close()
      state = 'on'
    x = 0
  else:
    x = x+1
#  temp = ['']
 # file = open(button_pin, 'r')
  #temp[0] = file.read()
  #file.close()
#  if( '0' in temp[0]):
 #   file = open(led_pin, 'r+')
  #  file.write(HIGH)
   # file.close()
 # else:
  #  file = open(led_pin,'r+')
   # file.write(LOW)
    #file.close()
