import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)

pwm=GPIO.PWM(07, 100)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
pwm2=GPIO.PWM(12, 100)

TRIG = 16
ECHO = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


LEFT_IR_PIN = 13
GPIO.setup(LEFT_IR_PIN, GPIO.IN)

RIGHT_IR_PIN = 15
GPIO.setup(RIGHT_IR_PIN, GPIO.IN)

pwm.start(0)
pwm2.start(0)

##SERVO MOTOR Setup
#SERVO_PIN = 11
#GPIO.setup(SERVO_PIN, GPIO.OUT)
#pwmServo=GPIO.PWM(SERVO_PIN, 50)
#pwmServo.start(0)

pwm.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
#GPIO.output(12,True)
#Setting up Ultrasonic distance measurement
def SetRightMotorBackward():
    print "Setting Right Motor Backward"
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)

def SetRightMotorOff():
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)

def SetLeftMotorOff():
    GPIO.output(03, False)
    GPIO.output(05, False)
    GPIO.output(07, False)

def SetLeftMotorBackward():
    print "Setting Left Motor Backward"
    GPIO.output(03, True)
    GPIO.output(05, False)
    GPIO.output(07, True)

def SetRightMotorForward():
    print "Setting Right Motor Forward"
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, True)

def SetLeftMotorForward():
    print "Setting Left Motor Forward"
    GPIO.output(03, False)
    GPIO.output(05, True)
    GPIO.output(07, True)

def SetServoAngle(angle):
        print "Setting Angle", angle
	duty = angle / 18 + 2
	GPIO.output(SERVO_PIN, True)
	pwmServo.ChangeDutyCycle(duty)
	sleep(0.5)
	GPIO.output(SERVO_PIN, False)
	pwmServo.ChangeDutyCycle(0)

#then turn the enable pin back off

    
def MeasureDistance():
    print "Distance Measurement In Progress"
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    sleep(0.25)
    GPIO.output(TRIG, True)
    sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()      

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance:",distance,"cm"
    return distance
count = 0
p_angle = 0
pwm.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
SetRightMotorOff()
SetLeftMotorOff()
SetRightMotorForward()
SetLeftMotorForward()
sleep(60)

pwm.stop()
pwm2.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
