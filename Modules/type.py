from pynput.keyboard import Controller, KeyCode
from time import sleep

keyboard = Controller()


def run(statement: str):
    enter = False
    if statement.endswith(" enter"):
        statement = statement[:-6]
        enter = True
    keyboard.type(statement)
    if enter:
        keyboard.type("\n")


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
