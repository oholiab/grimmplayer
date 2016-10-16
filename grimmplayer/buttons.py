import RPi.GPIO as GPIO

outputs = []
inputs = [2]

def initialize():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(outputs, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def poll():
    return [GPIO.input(i) for i in inputs]
