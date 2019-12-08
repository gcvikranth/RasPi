import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

IR_PIN = 13
GPIO.setup(IR_PIN, GPIO.IN)
count = 1

while True:
  got_something = GPIO.input(IR_PIN)
  print got_something
  if got_something:
    print("{:>3} Got something".format(count), got_something)
  else:
    print("{:>3} Nothing detected".format(count),got_something)
  count += 1
  time.sleep(0.2)
