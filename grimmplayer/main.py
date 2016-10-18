from grimmplayer import buttons
from grimmplayer import control
import time

def main():
    buttons.initialize()
    lastButtonState = buttons.poll()
    heldfor = 0
    pressStart = None
    debounceStart = None
    debounceCounter = 0
    while True:
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
                control.togglePlay()
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
