from gpiozero import Robot, Button
from gpiozero.pins.pigpio import PiGGPIOFactory

factory = PiGGPIOFactory(host="192.168.1.79")
robot = Robot(left = (factory.pin(7), factory.pin(8)), right = (factory.pin(9),factory.pin(10)))

accelerate = Button(4)
reverse = Button(17)
right = Button(13)
left = Button(21)

accelerate.when_pressed = robot.forward
accelerate.when_released = robot.stop

reverse.when_pressed = robot.reverse
reverse.when_released = robot.stop

right.when_pressed = robot.right
right.when_released = robot.stop

left.when_pressed = robot.left
left.when_released = robot.stop
