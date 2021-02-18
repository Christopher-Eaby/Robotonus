from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
metaldet = 36
GPIO.setup(metaldet,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(metaldet)==0:
        print("metal found")
        sleep(1)
