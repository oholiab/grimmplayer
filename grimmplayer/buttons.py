import RPi.GPIO as GPIO

BIG = 26
RIGHT = 16
LEFT = 5
UP = 6
DOWN = 13

outputs = []
inputs = [BIG, RIGHT, LEFT, UP, DOWN]

def initialize():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(outputs, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def poll():
    return [GPIO.input(i) for i in inputs]
