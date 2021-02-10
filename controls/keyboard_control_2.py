from pynput.keyboard import Listener
import sys, tty, termios, time
from pynput.keyboard import Listener
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

leftmotorspeed = 1.0
rightmotorspeed = 1.0

motorforward = (leftmotorspeed , rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, -rightmotorspeed)
motorright = (-leftmotorspeed, rightmotorspeed)
speed = 5
def on_press(key, leftmotorspeed = 1.0, rightmotorspeed = 1.0):
    if hasattr(key, 'char'):
        if key.char == "w":
            robot.value = motorforward
        elif key.char == "s":
            robot.value = motorbackward
        elif key.char == "a":
            robot.value = motorleft
        elif key.char == "d":
            robot.value = motorright
        elif key.char == "1":
            leftmotorspeed = 0.2
            rightmotorspeed = 0.2
        elif key.char == "2":
            leftmotorspeed = 0.4
            rightmotorspeed = 0.4
        elif key.char == "3":
            leftmotorspeed = 0.6
            rightmotorspeed = 0.6
        elif key.char == "4":
            leftmotorspeed = 0.8
            rightmotorspeed = 0.8
        elif key.char == "5":
            leftmotorspeed = 1.0
            rightmotorspeed = 1.0

def on_release(key):
    robot.stop()
    
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()