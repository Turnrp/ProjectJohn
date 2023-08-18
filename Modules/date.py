from datetime import datetime
from pyttsx3 import speak


def run(statement):
    now = datetime.now()
    hour_formatted = (
        now.hour > 12 and now.hour - 12 or (now.hour == 0 and 12 or now.hour)
    )
    time_formatted = (
        str(now.month)
        + "/"
        + str(now.day)
        + "/"
        + str(now.year)
        + " "
        + str(hour_formatted)
        + ":"
        + str(now.minute)
    )
    print(time_formatted)
    speak(time_formatted)


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
