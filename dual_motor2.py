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
SERVO_PIN = 11
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwmServo=GPIO.PWM(SERVO_PIN, 50)
pwmServo.start(0)

#GPIO.output(03, True)
#GPIO.output(05, False)
#print("#Now, we're going to set the PWM duty to 50%. Write")
pwm.ChangeDutyCycle(100)
#print("#then turn on the Enable pin")

#GPIO.output(07, True)

#GPIO.output(8, True)
#GPIO.output(10, False)
pwm2.ChangeDutyCycle(100)
#GPIO.output(12,True)
#Setting up Ultrasonic distance measurement

def SetServoAngle(angle):
        print "Setting Angle", angle
	duty = angle / 18 + 2
	GPIO.output(SERVO_PIN, True)
	pwmServo.ChangeDutyCycle(duty)
	sleep(0.5)
	GPIO.output(SERVO_PIN, False)
	pwmServo.ChangeDutyCycle(0)

#then turn the enable pin back off



def TurnClockwise(time):
    print "Turning Clockwise for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, True)
    GPIO.output(07, True)
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)
    sleep(time)

def TurnCounterClockwise(time):
    print "Turning CounterClockwise for ",time,"seconds"
    GPIO.output(03, True)
    GPIO.output(05, False)
    GPIO.output(07, True)
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, True)
    sleep(time)

def GoForward(time):
    print "Going Forward for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, True)
    GPIO.output(07, True)
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, True)
    sleep(time)

def GoBackward(time):
    print "Going Backward for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, True)
    GPIO.output(07, True)
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)
    sleep(time)

def SpinningRightMotorBackward(time):
    print "Spinning Right Motor Backward for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, False)
    GPIO.output(07, False)
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)
    sleep(time)

def SetRightMotorBackward():
    print "Setting Right Motor Backward"
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)
    

def SpinningRightMotorForward(time):
    print "Spinning Right Motor Forward for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, False)
    GPIO.output(07, False)
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, True)
    sleep(time)

def SpinningLeftMotorBackward(time):
    print "Spinning Left Motor Backward for ",time,"seconds"
    GPIO.output(03, True)
    GPIO.output(05, False)
    GPIO.output(07, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)
    sleep(time)

def SpinningLeftMotorForward(time):
    print "Spinning Left Motor Forward for ",time,"seconds"
    GPIO.output(03, False)
    GPIO.output(05, True)
    GPIO.output(07, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)
    sleep(time)

def SetRightMotorBackward():
    print "Setting Right Motor Backward"
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(12, True)

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

def StopLeftMotor():
    print "Stopping Left Motor"
    GPIO.output(03, False)
    GPIO.output(05, False)
    GPIO.output(07, False)

def StopRightMotor():
    print "Stopping Right Motor"
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)
    
def MeasureDistance():
    print "Distance Measurement In Progress"
    GPIO.output(TRIG, False)

    print "Waiting For Sensor To Settle"

    sleep(1)
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


#TurnCounterClockwise(5)
#TurnClockwise(5)
#GoForward(5)
#GoBackward(5)
#TurnCounterClockwise(5)
#TurnClockwise(5)
#SpinningLeftMotorBackward(5)
#SpinningLeftMotorForward(5)

    
#TurnCounterClockwise(5)
#TurnClockwise(5)
#StopLeftMotor()
#StopRightMotor()
#SetRightMotorBackward()
#SetLeftMotorBackward()
#sleep(5)
#SetRightMotorForward()
#StopLeftMotor()
#sleep(0.75)
#SetLeftMotorForward()
#StopRightMotor()
#sleep(1)
#SetRightMotorBackward()
#SetLeftMotorBackward()
#SetRightMotorForward()
#SetLeftMotorForward()

count = 0
left=97
pwm.ChangeDutyCycle(63) #left
pwm2.ChangeDutyCycle(91) #right

SetRightMotorForward()
SetLeftMotorForward()
sleep(10)

SetRightMotorBackward()
SetLeftMotorBackward()
sleep(10)
      
pwm.stop()
pwm2.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
