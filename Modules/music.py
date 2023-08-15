import pynput.keyboard as kb

keyboard = kb.Controller()


def play():
    keyboard.press(kb.Key.media_play_pause)
    keyboard.release(kb.Key.media_play_pause)


def pause():
    keyboard.press(kb.Key.media_play_pause)
    keyboard.release(kb.Key.media_play_pause)


def volumeup():
    keyboard.press(kb.Key.media_volume_up)
    keyboard.release(kb.Key.media_volume_up)


def volumedown():
    keyboard.press(kb.Key.media_volume_down)
    keyboard.release(kb.Key.media_volume_down)


def next():
    keyboard.press(kb.Key.media_next)
    keyboard.release(kb.Key.media_next)


def back():
    keyboard.press(kb.Key.media_previous)
    keyboard.release(kb.Key.media_previous)


# Setup For Custom (This is the only way so far for custom modules without having to say "cat fact run" but I can add some stuff in the future)
from sys import argv


def call_function(function_name):
    try:
        function_to_call = globals()[function_name.replace(" ", "")]
        function_to_call()
    except KeyError:
        print("Unknown function:", function_name)
        pass


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: script2.py run <function>")
    else:
        function_name = argv[2]
        call_function(function_name)
