import requests
from pyttsx3 import speak


def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    if response.status_code == 200:
        fact_data = response.json()
        cat_fact = fact_data.get("fact")
        return cat_fact
    else:
        return "Failed to retrieve cat fact"


def run(statement):
    fact = get_cat_fact()
    print(fact)
    speak(fact)


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
