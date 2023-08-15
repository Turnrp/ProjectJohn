import speech_recognition as sr
from subprocess import run
from os import listdir

Modules = listdir("Modules")
ModulesNames = [item.split(".")[0] for item in Modules]
# print(Modules, ModulesNames)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            statement = r.recognize_google(audio, language="en-in")
            print(f"user said:{statement}\n")
        except Exception as e:
            return "none"
        return statement


if __name__ == "__main__":
    while True:
        statement = input().lower()
        # statement = takeCommand().lower()
        if statement == "0":
            continue

        if statement == "load":
            Modules = listdir("Modules")
            ModulesNames = [item.split(".")[0] for item in Modules]
            continue

        module_name = None
        for name in ModulesNames:
            if name in statement:
                module_name = name
                break

        if module_name:
            module_args = (
                statement.replace(statement.split(module_name)[0], "", 1)
                .replace(module_name, "", 1)
                .strip()
            )
            # print(module_args)
            for module in Modules:
                if module_name in module:
                    Module = module
                    break
            try:
                RunProcess = run(["python", "Modules\\" + Module, "run", module_args])
                # print(RunProcess)
            except:
                print("Error")
