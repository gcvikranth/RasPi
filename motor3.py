import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)
pwm=GPIO.PWM(07, 50)
pwm.start(0)

GPIO.output(03, True)
GPIO.output(05, False)

pwm.ChangeDutyCycle(100)

GPIO.output(07, True)


print("Sleeping for 10 seconds for motor to run")
sleep(10)
#now turn off the Enable pin

GPIO.output(07, False)
#then reverse the inputs to set it to reverse
pwm.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
