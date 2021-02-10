from picamera import picamera
from time import sleep

camera = picamera

camera.start_preview()

count=5
while count!=0:
    sleep(count)
    camera.capture('/home/pi/Desktop/view.jpg')
    count+=1