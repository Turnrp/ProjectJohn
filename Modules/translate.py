from googletrans import Translator, constants
from pyttsx3 import speak

language_list = [item for sublist in constants.LANGUAGES.items() for item in sublist]


def run(statement):
    translator = Translator()
    language = "english"
    # print(language_list)
    if statement.split(" ")[0] in language_list:
        language = statement.split(" ")[0]
        statement = statement.replace(language, "", 1)
    # textLanguage = translator.detect(statement)
    translated = translator.translate(statement, dest=language)
    print(statement, "->", translated.text)
    speak(translated.text)


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
