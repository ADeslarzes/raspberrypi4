import os
import time

nb_pics = 10

os.system("raspivid -t 30000 -w 1000 -h 1000 -fps 25 -b 1200000 -p 0,0,640,480 -o satvideo.h264")
os.system("MP4Box -add satvideo.h264 satvideo.mp4")
os.system("rm satvideo.h264")

print("video enregistree")

os.system("python3 long_exposure/src/long_exposure.py local-video /home/pi/Documents/code_final/satvideo.mp4 /home/pi/Documents/code_final/long_exp.png -s 5")

print("long exposure exported!")

