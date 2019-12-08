import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

IR_PIN1 = 13
GPIO.setup(IR_PIN1, GPIO.IN)
IR_PIN2 = 15
GPIO.setup(IR_PIN2, GPIO.IN)

count = 1

while True:
  got_something1 = GPIO.input(IR_PIN1)
  print got_something1
  if got_something1:
    print("{:>3} Got something at 1".format(count))
  else:
    print("{:>3} Nothing detected at 1".format(count))

  got_something2 = GPIO.input(IR_PIN2)
  print got_something2
  if got_something2:
    print("{:>3} Got something at 2".format(count))
  else:
    print("{:>3} Nothing detected at 2".format(count))
  
  count += 1
  time.sleep(0.2)
