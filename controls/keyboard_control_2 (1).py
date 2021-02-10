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

def on_release(key):
    robot.stop()
    
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
