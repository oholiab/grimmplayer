from grimmplayer import buttons

def main():
    buttons.initialize()
    lastButtonState = buttons.poll()
    while True:
        buttonState = buttons.poll()
        print(buttonState)
        if buttonState != lastButtonState:
            print("PUSHY BUTTON")
        lastButtonState = buttonState


if __name__ == "__main__":
    main()
