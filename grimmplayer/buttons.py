import RPi.GPIO as GPIO

BIG_PIN = 26
RIGHT_PIN = 16
LEFT_PIN = 5
UP_PIN = 6
DOWN_PIN = 13

# Map the buttons to named indexes for use everywhere else
BIG = 0
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

outputs = []
inputs = [BIG_PIN, RIGHT_PIN, LEFT_PIN, UP_PIN, DOWN_PIN]

def initialize():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(outputs, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def poll():
    return [GPIO.input(i) for i in inputs]
