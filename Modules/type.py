from pynput.keyboard import Controller, KeyCode
from time import sleep

keyboard = Controller()


def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        return sentence[: -len(old)] + new
    return sentence


def run(statement: str):
    statement = replace_ending(statement, " entered", "\n")
    statement = replace_ending(statement, " enter", "\n")
    keyboard.type(statement)


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
