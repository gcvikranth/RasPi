import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)

pwm=GPIO.PWM(07, 100)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
pwm2=GPIO.PWM(12, 100)


pwm.start(0)
pwm2.start(0)
GPIO.output(03, True)
GPIO.output(05, False)
print("#Now, we're going to set the PWM duty to 50%. Write")
pwm.ChangeDutyCycle(100)
print("#then turn on the Enable pin")

GPIO.output(07, True)
print("#then put the code to sleep for 5 seconds so the motor runs")

GPIO.output(8, True)
GPIO.output(10, False)
pwm2.ChangeDutyCycle(100)
GPIO.output(12,True)
sleep(15)
print("#now turn off the Enable pin")



pwm.stop()
pwm2.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
