def run(statement):
    with open("Modules\\" + statement + ".py", "x") as file:
        file.write(
            """def run():
    pass

# Setup For Custom (This is the only way so far for custom modules without having to say "cat fact run" but I can add some stuff in the future)
from sys import argv


def call_function(function_name):
    try:
        function_to_call = globals()[function_name]
        function_to_call()
    except KeyError:
        print("Unknown function:", function_name)
        pass


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: script2.py run <function>")
    else:
        function_name = argv[2]
        call_function(function_name)"""
        )


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
