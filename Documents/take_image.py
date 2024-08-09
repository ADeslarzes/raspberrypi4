import os
import time

nb_pics = 10

os.system("raspivid -t 3000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o pivideo.h264")
os.system("MP4Box -add pivideo.h264 pivideo.mp4")
os.system("rm pivideo.h264")
