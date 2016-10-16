from grimmplayer import buttons
from grimmplayer import control

def main():
    buttons.initialize()
    lastButtonState = buttons.poll()
    while True:
        buttonState = buttons.poll()
        for i in range(0, len(buttons.inputs)):
            # lt as pull-down
            if buttonState[i] < lastButtonState[i]:
                control.togglePlay()
                print("PUSHY BUTTON")
        lastButtonState = buttonState


if __name__ == "__main__":
    main()
