from genericpath import samestat
from os import stat
import numpy as np
from pyttsx3 import speak
import speech_recognition as sr
import math

Alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

Outposts = [
    ("Sanctuary Outpost", (6, 7)),
    ("New Golden Sands Outpost", (4, 10)),
    ("Plunder Outpost", (10, 18)),
    ("Ancient Spire Outpost", (17, 17)),
    ("Galleon's Grave Outpost", (18, 8)),
    ("Dagger Tooth Outpost", (13, 8)),
    ("Morrow's Peak Outpost", (22, 17)),
    ("Reaper's Hideout", (9, 11)),
]
Seaposts = [
    ("The Spoils of Plenty Store", (2, 7)),
    ("The North Star Seapost", (8, 10)),
    ("The Finest Trading Post", (6, 17)),
    ("Stephen's Spoils", (12, 15)),
    ("Three Paces East Seapost", (19, 10)),
    ("The Wild Treasures Store", (15, 4)),
    ("Brian's Bazaar", (25, 12)),
    ("Roaring Traders", (21, 20)),
]
Fortresses = [
    ("Keel Haul Fort", (3, 6)),
    ("Hidden Spring Keep", (9, 8)),
    ("Sailor's Knot Stronghold", (5, 14)),
    ("Lost Gold Fort", (8, 17)),
    ("Fort of the Damned", (12, 14)),
    ("The Crow's Nest Fortress", (15, 17)),
    ("Skull Keep", (16, 9)),
    ("Kraken Watchtower", (12, 6)),
    ("Shark Fin Camp", (16, 5)),
    ("Molten Sands Fortress", (26, 11)),
]
SunkenKingdom = [
    ("Shrine of the Coral Tomb", (8, 5)),
    ("Shrine of Ocean's Fortune", (4, 14)),
    ("Shrine of Ancient Tears", (14, 20)),
    ("Shrine of Tribute", (7, 18)),
    ("Shrine of Hungering", (17, 5)),
    ("Shrine of Flooded Embrace", (14, 12)),
    ("Treasury of Sunken Shores", (4, 3)),
    ("Treasury of the Lost Ancients", (8, 13)),
    ("Treasury of the Secret Wilds", (12, 3)),
]

Treasures = {
    "chest of legends": ("athenas fortune", "4000-7000~"),
    "ashen chest of legends": ("athenas fortune", "7000-10,000~"),
    "chalice of ancient fortune": ("athenas fortune", "500-800~"),
    "crate of legendary voyages": ("athenas fortune", "500-700~"),
    "gilded relic of ancient fortune": ("athenas fortune", "1200-1600~"),
    "keg of ancient black powder": ("athenas fortune", "2500-4000~"),
    "skull of ancient fortune": ("athenas fortune", "500-700~"),
    "villainous skull of ancient fortune": ("athenas fortune", "1200-1700~"),
    "ritual skull": ("bilge rats", "10 doubloons"),
    "rag and bone crates": ("bilge rats", "5 doubloons"),
    "ashen tome": (
        "bilge rats",
        "10 doubloons each (there are four types of tomes and five tome ranks for each of those four tome types)",
    ),
    "ashen chest": (
        "bilge rats",
        "10 doubloons (plus whatever you earn from selling the tomes found inside the chest) or sold for 100 gold to 2500 gold depending on the type",
    ),
    "ashen key": (
        "bilge rats",
        "5 doubloons (plus the 10 doubloons earned from selling the chest they open)",
    ),
    "captains chest": ("gold hoarders", "500-1500~"),
    "castaways chest": ("gold hoarders", "50-150~"),
    "marauders chest": ("gold hoarders", "250-550~"),
    "seafarers chest": ("gold hoarders", "100-300~"),
    "chest of rage": ("gold hoarders", "2500-4000~"),
    "chest of sorrow": ("gold hoarders", "2500-4500~"),
    "chest of a thousand grogs": ("gold hoarders", "2000-3000~"),
    "chest of ancient tributes": ("gold hoarders", "3000-4000~"),
    "chest of the damned": ("gold hoarders", "1000-2000~"),
    "skeleton captains chest": ("gold hoarders", "1000-1500~"),
    "stronghold chest": ("gold hoarders", "1000-3000~"),
    "bronze artifacts": ("gold hoarders", "50-150~"),
    "silver artifacts": ("gold hoarders", "150-300~"),
    "gold artifacts": ("gold hoarders", "300-500~"),
    "bejeweled (literally) artifacts": ("gold hoarders", "500-1000~"),
    "devils roar artifacts": ("gold hoarders", "100-2000~ depending on the artifact"),
    "gold treasure vault key": ("gold hoarders", "3000-4000~"),
    "silver treasure vault key": ("gold hoarders", "2000-2500~"),
    "stone treasure vault keys": ("gold hoarders", "1000-1500~"),
    "animal meat": ("the hunters call", "45 if cooked properly"),
    "kraken/megalodon meat": ("the hunters call", "450 if cooked properly"),
    "fish": (
        "the hunters call",
        "the most common cooked fish will get you about 100 gold, while some of the more rare cooked fish could net you nearly 2000 gold",
    ),
    "treacherous plunder": ("the hunters call", "10"),
    "disgraced bounty skull": ("order of souls", "200~"),
    "foul bounty skull": ("order of souls", "100~"),
    "hateful bounty skull": ("order of souls", "500~"),
    "villainous bounty skull": ("order of souls", "500-1500~"),
    "ashen skulls": (
        "order of souls",
        "see the above skull rewards - you'll earn slightly more for each ashen skull.",
    ),
    "captain skull of the damned": ("order of souls", "1500-2000~"),
    "skull of the damned": ("order of souls", "1000-1500~"),
    "ashen winds skull": (
        "order of souls",
        "5000~ (but its also basically a flamethrower, which could be more useful than gold to be honest)",
    ),
    "gold hoarders skull": ("order of souls", "10,000"),
    "skeleton captains skull": ("order of souls", "500-2500~"),
    "stronghold skull": ("order of souls", "1500-5000~"),
    "chicken": (
        "merchant alliance (but they must first be captured in an animal crate)",
        "10-200~, depending on the type of chicken",
    ),
    "pig": (
        "merchant alliance (but they must first be captured in an animal crate)",
        "10-200~, depending on the type of pig",
    ),
    "snake": (
        "merchant alliance (but they must first be captured in an animal crate)",
        "10-200~, depending on the type of snake",
    ),
    "gunpowder barrel": ("merchant alliance", "50-250~"),
    "stronghold gunpowder barrel": ("merchant alliance", "2500-7500~"),
    "fruit crate": ("merchant alliance", "500-1000~"),
    "cannonball crate": ("merchant alliance", "500-1000~"),
    "wood crate": ("merchant alliance", "500-1000~"),
    "cannonball crate of the damned": ("merchant alliance", "1000~"),
    "storage crate of the damned": ("merchant alliance", "1000~"),
    "ammo crate": ("merchant alliance", "250~"),
    "firebomb crate": ("merchant alliance", "1000-2000~"),
    "storage crate": ("n/a", "can't be sold"),
    "ashes of the damned": ("merchant alliance", "1000-1500~"),
    "crate of ancient bone dust": ("merchant alliance", "2000-5000~"),
    "crate of exotic silks": ("merchant alliance", "500~"),
    "crate of exquisite spices": ("merchant alliance", "1000~"),
    "crate of extraordinary minerals": ("merchant alliance", "1500~"),
    "crate of fine ore": ("merchant alliance", "750~"),
    "crate of fine sugar": ("merchant alliance", "150~"),
    "crate of precious gemstones": ("merchant alliance", "3000~"),
    "crate of rare tea": ("merchant alliance", "300~"),
    "crate of volcanic stone": ("merchant alliance", "1500~"),
    "crate of plants": ("merchant alliance", "700~"),
    "create of devils plants": ("merchant alliance", "1400~"),
    "crate of cloth": ("merchant alliance", "700~"),
    "crate of devils cloth": ("merchant alliance", "1400~"),
    "crate of rum": ("merchant alliance", "700~"),
    "crate of devils rum": ("merchant alliance", "1400~"),
    "assorted gemstones": ("merchant alliance", "4000~, when in demand"),
    "broken stone": ("merchant alliance", "2500~, when in demand"),
    "raw sugar": ("merchant alliance", "2000~, when in demand"),
    "unfiltered minerals": ("merchant alliance", "4000~, when in demand"),
    "unprocessed tea": ("merchant alliance", "2500~, when in demand"),
    "unrefined spices": ("merchant alliance", "3500~, when in demand"),
    "unsorted silks": ("merchant alliance", "3000~, when in demand"),
    "emerald mermaid gem": ("gold hoarders", "1000"),
    "ruby mermaid gem": ("gold hoarders", "2000"),
    "sapphire mermaid gem": ("gold hoarders", "1000"),
    "reapers chest": ("reapers bones", "25 doubloons"),
    "broken emissary flag": (
        "reapers bones",
        "anywhere from 1000 to 10,000, depending on the emissary rank of the player ",
    ),
}

LocationDictionary = {
    "sanctuaryoutpost": (6, 7),
    "newgoldensandsoutpost": (4, 10),
    "plunderoutpost": (10, 18),
    "ancientspireoutpost": (17, 17),
    "galleonsgraveoutpost": (18, 8),
    "daggertoothoutpost": (13, 8),
    "morrowspeakoutpost": (22, 17),
    "reapershideout": (9, 11),
    "thespoilsofplentystore": (2, 7),
    "thenorthstarseapost": (8, 10),
    "thefinesttradingpost": (6, 17),
    "stephensspoils": (12, 15),
    "threepaceseastseapost": (19, 10),
    "thewildtreasuresstore": (15, 4),
    "briansbazaar": (25, 12),
    "roaringtraders": (21, 20),
    "keelhaulfort": (3, 6),
    "hiddenspringkeep": (9, 8),
    "sailorsknotstronghold": (5, 14),
    "lostgoldfort": (8, 17),
    "fortofthedamned": (12, 14),
    "thecrowsnestfortress": (15, 17),
    "skullkeep": (16, 9),
    "krakenwatchtower": (12, 6),
    "sharkfincamp": (16, 5),
    "moltensandsfortress": (26, 11),
    "shrineofthecoraltomb": (8, 5),
    "shrineofoceansfortune": (4, 14),
    "shrineofancienttears": (14, 20),
    "shrineoftribute": (7, 18),
    "shrineofhungering": (17, 5),
    "shrineoffloodedembrace": (14, 12),
    "treasuryofsunkenshores": (4, 3),
    "treasuryofthelostancients": (8, 13),
    "treasuryofthesecretwilds": (12, 3),
}


# (North, South, East, West)
DirectionDictionary = {
    "1, 0, 0, 0": "North",
    "0, 1, 0, 0": "South",
    "0, 0, 1, 0": "East",
    "0, 0, 0, 1": "West",
    "1, 0, 1, 0": "North-East",
    "0, 1, 1, 0": "South-East",
    "0, 1, 0, 1": "South-West",
    "1, 0, 0, 1": "North-West",
}


def FindClosestPOI(x, y, POIS):
    print(x, y)
    distances = []
    for location_name, location_coords in POIS:
        distance = math.sqrt(
            (location_coords[0] - x) ** 2 + (location_coords[1] - y) ** 2
        )
        distances.append((location_name, location_coords, distance))

    distances.sort(key=lambda x: x[2])

    return distances[0]


def GetDirection(coords, destination):
    direction = (coords[0] - destination[0], coords[1] - destination[1])
    directionGCD = np.gcd(direction[0], direction[1])
    direction = (direction[0] / directionGCD, direction[1] / directionGCD)

    isNorth = int(direction[1] > 0)
    isSouth = int(direction[1] < 0)
    isEast = int(direction[0] < 0)
    isWest = int(direction[0] > 0)

    key = str(isNorth) + ", " + str(isSouth) + ", " + str(isEast) + ", " + str(isWest)
    return DirectionDictionary[key]


def run(statement):
    response = "Null"
    if "direction from" in statement:
        statement = statement.replace("direction from ", "")
        statement = statement.replace("-", "").replace(" ", "").split("to")
        for i in statement:
            statement[statement.index(i)] = statement[statement.index(i)].replace(
                "be ", "b"
            )

        # print(statement[0], list(LocationDictionary.keys()))
        if statement[0] in list(LocationDictionary.keys()):
            coords = LocationDictionary[statement[0]]
        else:
            coords = statement[0][:1] + " " + statement[0][1:]
            coords = coords.split(" ")
            coords = (Alphabet.index(coords[0]), int(coords[1]))

        if statement[1] in list(LocationDictionary.keys()):
            destination = LocationDictionary[statement[1]]
        else:
            destination = statement[1][:1] + " " + statement[1][1:]
            destination = destination.split(" ")
            destination = (Alphabet.index(destination[0]), int(destination[1]))

        response = GetDirection(coords, destination)
    elif "find" in statement and "nearest" in statement and "from" in statement:
        playerLocation = statement.split("from")[1].replace(" ", "")

        if playerLocation in list(LocationDictionary):
            coords = LocationDictionary[playerLocation]
        else:
            playerLocation = playerLocation[0] + " " + playerLocation[1:]
            playerLocation = playerLocation.split(" ")
            playerLocation[0] = Alphabet.index(playerLocation[0]) + 1
        POIS = []

        if "outpost" in statement:
            POIS = Outposts
        elif "seapost" in statement:
            POIS = Seaposts
        elif "fortress" in statement:
            POIS = Fortresses
        elif "sunken kingdom" in statement:
            POIS = SunkenKingdom
        elif "dad" in statement:
            response = "This is an impossible statement your dad is gone."

        if (
            "outpost" in statement
            or "seapost" in statement
            or "fortress" in statement
            or "sunken kingdom" in statement
        ):
            response = FindClosestPOI(
                int(playerLocation[0]), int(playerLocation[1]), POIS
            )
            response = (
                str(response[0])
                + " at "
                + Alphabet[response[1][0] - 1]
                + str(response[1][1])
                + ", Head "
                + GetDirection(
                    (int(playerLocation[0]), int(playerLocation[1])),
                    (response[1][0], int(response[1][1])),
                )
            )
    elif "what" in statement:
        if "value" in statement and "of the" in statement:
            TreasureName = statement[statement.index("of the ") + 7 :]
            if TreasureName in Treasures.keys():
                Treasure = Treasures[TreasureName]
                response = (
                    "The best emissary to turn this into would be "
                    + Treasure[0].replace("N/A", "None")
                    + " and the average gold you would get is "
                    + Treasure[1].replace("~", "").replace("-", " to ").replace(",", "")
                )
            else:
                response = (
                    "I'm sorry it does not seem like "
                    + TreasureName
                    + " is in my database."
                )
    print("Billy:", response)
    speak(response)


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
