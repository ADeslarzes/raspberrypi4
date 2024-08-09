import subprocess
import time
import os
from random import seed
from random import randint

from subprocess import call
 
print("Starting the program...")


while True:
 
    cmd = "yes | gphoto2 --filename '/home/pi/PHOTO_FULLPROCESS/set_11/pic_" + str(randint(0,100000))+".%C' --capture-image-and-download"
    subprocess.call(cmd, shell=True)
    
    time.sleep(4)
    
