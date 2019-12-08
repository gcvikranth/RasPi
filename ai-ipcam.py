  
#!/usr/bin/env python
#from darkflow.net.build import TFNet
import cv2
import os
import random
from subprocess import Popen
import time
from PIL import Image,ImageDraw
import numpy as np
import paho.mqtt.client as mqtt
import argparse
#In case Raspberry Pi camera is used instead of RTSP stream
import picamera
usepicamera = False

#RTSP captured frame frame_filename; preferably on RAM drive
#diskutil erasevolume HFS+ 'RAM Disk' `hdiutil attach -nomount ram://20480`
#frame_filename = '/Volumes/RAM Disk/frame'+str(random.randint(1,99999))+'.jpeg'

#Raspberry Pi
#sudo mkdir /tmp/ramdisk; sudo chmod 777 /tmp/ramdisk
#sudo mount -t tmpfs -o size=16M tmpfs /tmp/ramdisk/

frame_filename = '/home/pi/images/frame'+str(random.randint(1,99999))+'.jpeg'

#threshold parameter is below, keeping it too low will result in recognition errors
options = {"model": "cfg/tiny-yolo.cfg", "load": "tiny-yolo.weights",  "threshold": 0.55}

parser=argparse.ArgumentParser()
parser.add_argument(
  "--watch",  # name on the parser - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=str,
  default=['person', 'cat', 'dog', 'bird'],  # default if nothing is provided
)

parser.add_argument(
  "--stream",  # name on the parser - drop the `--` for positional/required parameters
  type=str,
  default= 'rtsp://admin:15081947@192.168.1.6/onvif1', # default if nothing is provided
)

parser.add_argument(
  "--broker",  # name on the parser - drop the `--` for positional/required parameters
  type=str,
  default= '', # default if nothing is provided
)

parser.add_argument(
  "--topic",  # name on the parser - drop the `--` for positional/required parameters
  type=str,
  default= '', # default if nothing is provided
)

parser.add_argument(
  "--showimage",  # name on the parser - drop the `--` for positional/required parameters
  type=str,
  default='no', # default if nothing is provided
)

# parse the command line
args = parser.parse_args()
watch_list=args.watch
rtsp_stream=args.stream
broker_address=args.broker
mqtt_topic=args.topic
showimageflag=args.showimage

print("Watching for: %r" % watch_list)
print("Stream: %r" % rtsp_stream)
print("MQTT broker: %r" % broker_address)
print("MQTT topic: %r" % mqtt_topic)
print("Show image: %r" % showimageflag)

#start a ffmpeg process that captures one frame every 2 seconds
p = Popen(['ffmpeg', '-loglevel', 'panic', '-rtsp_transport', 'udp', '-i', rtsp_stream, '-f' ,'image2' ,'-s', '640x480', '-pix_fmt', 'yuvj420p', '-r', '1/2' ,'-updatefirst', '1', frame_filename])



#tfnet = TFNet(options)
print('frame_filename',frame_filename)
curr_img = Image.open( frame_filename )
curr_img_cv2=cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)
curr_img_cv2 = cv2.resize(curr_img_cv2, (640, 480)) 
cv2.imshow("Security Feed", curr_img_cv2)

p.terminate()
cv2.destroyAllWindows()
