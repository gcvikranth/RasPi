import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
#GPIO.setup(07, GPIO.OUT)
#pwm=GPIO.PWM(07, 100)

#pwm.start(0)
GPIO.output(03, True)
GPIO.output(05, False)
print("#Now, we're going to set the PWM duty to 50%. Write")
#pwm.ChangeDutyCycle(50)
print("#then turn on the Enable pin")

#GPIO.output(07, True)
print("#then put the code to sleep for 2 seconds so the motor runs")

sleep(5)
print("#now turn off the Enable pin")

GPIO.output(03, False)

print("#then reverse the inputs to set it to reverse")

print("Going faster")
#pwm.ChangeDutyCycle(100)
#GPIO.output(07, True)
#sleep(10)
#GPIO.output(07, False)

print("Going Slower")
#pwm.ChangeDutyCycle(25)
#GPIO.output(07, True)
#sleep(10)
#GPIO.output(07, False)

print("Reversing....")

#GPIO.output(03, False)
#GPIO.output(05, True)
#Then change the PWM duty to 75%

#pwm.ChangeDutyCycle(75)
#then turn the enable back on


#GPIO.output(07, True)
#put the code to sleep for 3 seconds

#sleep(3)
#then turn the enable pin back off

#GPIO.output(07, False)
#stop the Pulse

print("Going slower In reverse")
#pwm.ChangeDutyCycle(50)
#GPIO.output(07, True)
#sleep(10)
#GPIO.output(07, False)

print("Going Faster In reverse")
#pwm.ChangeDutyCycle(100)
#GPIO.output(07, True)
#sleep(10)
#GPIO.output(07, False)

print("Changing direction")
#GPIO.output(03, True)
#GPIO.output(05, False)

#pwm.ChangeDutyCycle(100)
#GPIO.output(07, True)
#sleep(10)
#GPIO.output(07, False)

#pwm.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
