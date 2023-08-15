from requests import get
from pyttsx3 import speak
import datetime

BASEURL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "f277a9d4df9e110004d77b7988bd14d7"


def kelv_to_cel_fahrentheit(kelvin):
    celsius = kelvin - 273.15
    fahrentheit = celsius * (9 / 5) + 32
    return int(celsius), int(fahrentheit)


def run(statement):
    for i in ["in", "at"]:  # Remove every directing word
        statement = statement.replace(i, "", 1)
    statement = statement.split(" ")

    CITY = statement[0] and statement[0] or "Virginia"
    url = BASEURL + "appid=" + API_KEY + "&q=" + CITY

    response = get(url).json()
    kelvin = int(response["main"]["temp"])
    celsius, fahrenheit = kelv_to_cel_fahrentheit(kelvin)
    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelv_to_cel_fahrentheit(
        feels_like_kelvin
    )
    wind_speed = response["wind"]["speed"]
    humidity = response["main"]["humidity"]
    description = response["weather"][0]["description"]
    sunrise = str(
        datetime.datetime.utcfromtimestamp(
            response["sys"]["sunrise"] + response["timezone"]
        )
    ).split(" ")[1]
    sunrise = sunrise[: sunrise.rfind(":")].split(":")
    sunrise[0] = str(int(sunrise[0]) < 12 and sunrise[0] or int(sunrise[0]) - 12)
    sunrise = ":".join(sunrise) + " AM"

    sunset = str(
        datetime.datetime.utcfromtimestamp(
            response["sys"]["sunset"] + response["timezone"]
        )
    ).split(" ")[1]
    sunset = sunset[: sunset.rfind(":")].split(":")
    sunset[0] = str(int(sunset[0]) < 12 and sunset[0] or int(sunset[0]) - 12)
    sunset = ":".join(sunset) + " PM"

    full = f"The Temperature in {CITY} is {fahrenheit:.2f} fahrenheit but feels like {feels_like_fahrenheit:.2f} fahrenheit. The Humidity is {humidity} precent and the wind speed is {wind_speed} meters a second. The General Weather in {CITY} is {description}. The sunrises in {CITY} is at {sunrise} and falls at {sunset}."
    print(full)
    speak(full)


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
