import requests
from datetime import datetime
from pyttsx3 import speak


def GetMonth(month: int):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[month - 1]


class roAPI:
    def GetID(Username: str) -> int:
        requestPayload = {
            "usernames": [Username],
            "excludeBannedUsers": True,  # Whether to include banned users within the request, change this as you wish
        }

        responseData = requests.post(
            "https://users.roblox.com/v1/usernames/users", json=requestPayload
        )
        if responseData.status_code != 200:
            return 0

        userId = responseData.json()["data"][0]["id"]
        return userId

    def GetAge(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            CreationDate = response.json()["created"]
            CreationDate = CreationDate.split("T")
            CreationDate = CreationDate[0].split("-")
            CreationDate = datetime.date(
                int(CreationDate[0]), int(CreationDate[1]), int(CreationDate[2])
            )
            Days = (datetime.date.today()) - (CreationDate)
            Days = str(Days).split(" ")
            return Days[0]
        except:
            return "https://users.roblox.com/v1/users/" + str(UserID)

    def GetLimiteds(UserID: int) -> tuple:
        """
        Returns the total list of a users limiteds

        Please be aware this function can take some time to run depending on internet speed and how many limiteds a user owns
        """
        Limiteds = []
        IDs = []
        Cursor = ""
        Done = False
        while Done == False:
            try:
                response = requests.get(
                    "https://inventory.roblox.com/v1/users/"
                    + f"/{UserID}/assets/collectibles?sortOrder=Asc&limit=100&cursor={Cursor}"
                )
                Items = response.json()
                if (response.json()["nextPageCursor"] == "null") or response.json()[
                    "nextPageCursor"
                ] == None:
                    Done = True
                else:
                    Done = False
                    Cursor = response.json()["nextPageCursor"]
                for Item in Items["data"]:
                    try:
                        Limited = Item["name"]
                        ID = Item["assetId"]
                        Limiteds.append(Limited)
                        IDs.append(ID)
                    except:
                        Limiteds = Limiteds
                        IDs = IDs
                if response.json()["nextPageCursor"] == "None":
                    Done = True

            except Exception as ex:
                Done = True
        return (Limiteds, IDs)

    def CreationDate(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            CreationDate = response.json()["created"]
            CreationDate = CreationDate.split("T")
            CreationDate = CreationDate[0].split("-")

            return (
                str(CreationDate[1])
                + "/"
                + str(CreationDate[2])
                + "/"
                + str(CreationDate[0])
            )  # DD/MM/YYYY -- The Correct Format
        except:
            return response.json()["errors"][0]["message"]

    def GetDescription(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            return response.json()["description"]
        except:
            return "User not found"

    def UsernameHistory(UserID: int) -> list[list, str]:
        Cursor = ""
        Done = False
        PastNames = []
        while Done == False:
            response = requests.get(
                "https://users.roblox.com/v1/users/"
                + f"{UserID}/username-history?limit=100&sortOrder=Asc&cursor={Cursor}"
            )
            Names = response.json()["data"]
            if (response.json()["nextPageCursor"] == "null") or response.json()[
                "nextPageCursor"
            ] == None:
                Done = True
            else:
                Done = False
                Cursor = response.json()["nextPageCursor"]
            for Name in Names:
                PastNames.append(Name["name"])
            if response.json()["nextPageCursor"] == "None":
                Done = True
        return PastNames


def run(statement):
    Username = statement.replace(" ", "")
    try:
        UserID = roAPI.GetID(Username)
        Description = "Description: " + roAPI.GetDescription(UserID)
        CreationDate = roAPI.CreationDate(UserID)
        CreationMonth = "Creation Month: " + GetMonth(int(CreationDate[:2]))
        CreationDate = "Creation Date: " + CreationDate
        # AccountAge = "Account Age: " + str(roAPI.GetAge(UserID)) + " Days"
        UserHistory = "Username History: " + str(roAPI.UsernameHistory(UserID)).replace(
            '"', ""
        ).replace("[", "").replace("]", "")
        Limiteds = roAPI.GetLimiteds(UserID)
        LimitedStr = "Limiteds: \n"
        for i in Limiteds[0]:
            ID = Limiteds[1][Limiteds[0].index(i)]
            LimitedStr += i + ": " + str(ID) + "\n"
        # Change Log Box
        new_text = (
            "UserID: "
            + str(UserID)
            + "\n"
            + Description
            + "\n"
            + CreationDate
            + "\n"
            + CreationMonth
            + "\n"
            # + AccountAge
            # + "\n"
            + UserHistory
            + "\n"
            + LimitedStr
        )
    except Exception as e:
        new_text = f"Invalid User {Username} (Make sure your using their @ not display) or there was an error {e}"
    print(new_text)
    speak(new_text)


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
