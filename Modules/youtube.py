from pytube import Search
from webbrowser import open_new
from pyttsx3 import speak


def run(statement):
    video = Search(statement).results[0]
    open_new("https://www.youtube.com/watch?v=" + str(video.video_id))
    speak("Opening " + statement)


# Setup
from sys import argv


def call_function(function_name, variable_received):
    try:
        function_to_call = globals()[function_name]
        function_to_call(variable_received)
    except KeyError:
        print("Unknown function:", function_name)


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: script2.py <function> <variable>")
    else:
        function_name = argv[1]
        variable_received = argv[2]
        call_function(function_name, variable_received)
