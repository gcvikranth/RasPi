import cv2
import rtsp
import os
import random
from subprocess import Popen
import time

client = rtsp.Client(rtsp_server_uri = 'rtsp://admin:15081947@192.168.1.6/onvif1')

p = Popen(['ffmpeg', '-loglevel', 'panic', '-rtsp_transport', 'udp', '-i', 'rtsp://admin:15081947@192.168.1.6/onvif1', '-f' ,'image2' ,'-s', '640x480', '-pix_fmt', 'yuvj420p', '-r', '1/2' ,'-updatefirst', '1', '/tmp'])


client.read().show()
client.close()
