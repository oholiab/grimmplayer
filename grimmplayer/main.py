from grimmplayer import buttons
from grimmplayer import control
import time

def noop():
    pass

def control_map(button):
    switcher = {
            buttons.BIG: control.togglePlay,
            buttons.LEFT: control.previous,
            buttons.RIGHT: control.skip,
            buttons.UP: control.vol_up,
            buttons.DOWN: control.vol_down,
            }
    return switcher[button]()

def main():
    buttons.initialize()
    lastButtonState = buttons.poll()
    heldfor = 0
    pressStart = None
    debounceStart = None
    debounceCounter = 0
    while True:
        time.sleep(0.05)
        buttonState = buttons.poll()
        for i in range(0, len(buttons.inputs)):
            # lt as pull-down
            if debounceStart is not None:
                debounceCounter = time.time() - debounceStart
                if debounceCounter < 0.3:
                    continue
                else:
                    debounceStart = None
                    debounceCounter = 0
            if buttonState[i] < lastButtonState[i]:
                pressStart = time.time()
                debounceStart = time.time()
                control_map(i)
                print("PUSHY BUTTON")
            elif buttonState[i] > lastButtonState[i]:
                pressStart = None
            elif buttonState[i] == lastButtonState[i] == 0 and pressStart is not None:
                heldfor = time.time() - pressStart

            if heldfor > 1:
                heldfor = 0
                pressStart = None
                control.skip()
        lastButtonState = buttonState

if __name__ == "__main__":
    main()
