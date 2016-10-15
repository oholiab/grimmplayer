import RPi.GPIO as GPIO

#outputs = [3, 37]
inputs = [7, 11, 13, 37]

def initialize():
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(outputs, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def poll():
    return [GPIO.input(i) for i in inputs]
