import time
from gpiozero import CamJamKitRobot

pinLineFollower = 25

robot = CamJamKitRobot()
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (-leftmotorspeed, rightmotorspeed)
motorright = (leftmotorspeed, -rightmotorspeed)

robot.value = motorright
time.sleep(0.5)
robot.stop()
