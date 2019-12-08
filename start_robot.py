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

pwm.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
#GPIO.output(12,True)
#Setting up Ultrasonic distance measurement
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

while True and count<10:
   print "Count =", count
   
   #SetServoAngle(p_angle)
   p_angle=90
   count=count+1
   got_something_left = GPIO.input(LEFT_IR_PIN)
   got_something_right = GPIO.input(RIGHT_IR_PIN)
   distanceFromObstacle=MeasureDistance()
   pwm.ChangeDutyCycle(80)
   pwm2.ChangeDutyCycle(80)
   SetRightMotorBackward()
   SetLeftMotorBackward()
    
##   if got_something_left == 0:
##         print "Seeing obstacle at left"  
##         SetRightMotorForward()
##         SetLeftMotorBackward()
##         sleep(0.5)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##   elif got_something_right == 0:
##         print "Seeing obstacle at right"  
##         SetRightMotorBackward()
##         SetLeftMotorForward()
##         sleep(0.5)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##   elif distanceFromObstacle < 40 and p_angle==90:
##         print "Reversing @ distance",  distanceFromObstacle,"angle", p_angle
##         SetRightMotorBackward()
##         SetLeftMotorBackward()
##         sleep(2)        
##         SetRightMotorBackward()
##         SetLeftMotorForward()
##         sleep(0.5)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##         sleep(1)
##   elif got_something_left == 0 and got_something_right==0:
##         print "Reversing Stuck really bad"  
##         SetRightMotorBackward()
##         SetLeftMotorBackward()
##         sleep(3)        
##         SetRightMotorBackward()
##         SetLeftMotorForward()
##         sleep(0.5)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##         sleep(1)
##   elif distanceFromObstacle < 50 and p_angle==45:
##         print "Reversing @ distance",  distanceFromObstacle,"angle", p_angle
##         SetRightMotorBackward()
##         SetLeftMotorBackward()
##         sleep(1)        
##         SetRightMotorForward()
##         SetLeftMotorBackward()
##         sleep(0.75)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##         sleep(1)
##   elif distanceFromObstacle < 50 and p_angle==135:
##         print "Reversing @ distance",  distanceFromObstacle,"angle", p_angle
##         SetRightMotorBackward()
##         SetLeftMotorBackward()
##         sleep(1)        
##         SetRightMotorBackward()
##         SetLeftMotorForward()
##         sleep(0.75)
##         SetRightMotorForward()
##         SetLeftMotorForward()
##   else:
##         print "No Obstacles marching forward" ,got_something_right,got_something_left 
##         SetRightMotorForward()
##         SetLeftMotorForward()
##   p_angle=p_angle+45
##   if p_angle >180:
##       p_angle=0
      
   sleep(2)
    ##distanceFromObstacle=MeasureDistance()
    #if distanceFromObstacle > 40:
    #  SetRightMotorForward()
    #  SetLeftMotorForward()
    #  sleep(1)
    #elif distanceFromObstacle < 40 and distanceFromObstacle > 20:
    #  print "## Turning now",distanceFromObstacle
    #  SetRightMotorForward()
    #  SetLeftMotorBackward()
    #  sleep(2)
    #else:
    #  print "## Stopping now",distanceFromObstacle
    #  SetRightMotorBackward()
    #  SetLeftMotorBackward()
    #  sleep(2)
    
       
      
pwm.stop()
pwm2.stop()
#and cleanup all of the GPIO channels.

GPIO.cleanup()
