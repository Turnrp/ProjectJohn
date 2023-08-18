from pyttsx3 import speak


def plus(math):
    Sum = int(math[0]) + int(math[1])
    Final = "The sum of " + math[0] + " plus " + math[1] + " is " + str(Sum)
    print(Final)
    speak(Final)


def minus(math):
    Sum = int(math[0]) - int(math[1])
    Final = "The difference of " + math[0] + " minus " + math[1] + " is " + str(Sum)
    print(Final)
    speak(Final)


def multipliedby(math):
    Sum = int(math[0]) * int(math[1])
    Final = (
        "The product of " + math[0] + " multiplied by " + math[1] + " is " + str(Sum)
    )
    print(Final)
    speak(Final)


def dividedby(math):
    Sum = int(math[0]) / int(math[1])
    Final = "The quotion of " + math[0] + " divided by " + math[1] + " is " + str(Sum)
    print(Final)
    speak(Final)


# Setup For Custom (This is the only way so far for custom modules without having to say "cat fact run" but I can add some stuff in the future)
from sys import argv


def call_function(function_name, math):
    try:
        function_to_call = globals()[function_name]
        function_to_call(math)
    except KeyError:
        print("Unknown function:", function_name)
        pass


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: script2.py run <function> <num> <math> <num>")
    else:
        argv_split = argv[2].split(" ")
        if len(argv_split) > 3:
            function_name = argv_split[1] + argv_split[2]
            math = [argv_split[0], argv_split[3]]
        else:
            function_name = argv_split[1]
            math = [argv_split[0], argv_split[2]]
        call_function(function_name, math)
