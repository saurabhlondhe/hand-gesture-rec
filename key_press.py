from pynput.keyboard import Key, Controller
keyboard = Controller()
def pressRightArrow():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def pressLeftArrow():
    keyboard.press(Key.left)
    keyboard.release(Key.left)