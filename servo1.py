import RPi.GPIO as GPIO
from time import sleep
import sys
from espeak import espeak
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm.start(0)

def SetAngle(angle):
        print "Setting Angle", angle
	duty = angle / 18 + 2
	GPIO.output(11, True)
	pwm.ChangeDutyCycle(duty)
	sleep(0.5)
	GPIO.output(11, False)
	pwm.ChangeDutyCycle(0)

#then turn the enable pin back off
ServoAngle = int(sys.argv[1])
print "ServoAngle=", ServoAngle
espeak.synth (" Turning The Head "+sys.argv[1])
SetAngle(ServoAngle)

pwm.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
