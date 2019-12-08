import RPi.GPIO as GPIO
from time import sleep
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

count=0
ServoAngle=0
while True and count<10000:
   SetAngle(ServoAngle)
   ServoAngle=ServoAngle+30
   if ServoAngle == 180:
        while ServoAngle!=0 :
         SetAngle(ServoAngle)
         ServoAngle = ServoAngle-30
         
   count=count+1
   
pwm.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
