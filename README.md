# ProjectJohn
This is a modular voice assistant. Updates Soon!

If you wanna create your module I made two modules that create basic or custom modules a basic module just runs a function named run and custom modules will execute other function names

To use The Hey John Module you will need an Open AI API Key and it will cost money unless you still have the free trial.

## Instructions
1. Make sure you have Python and at least 1 module installed
2. Make sure the modules are in the folder "Modules"
3. Make sure you have all of the requirements installed
4. To use a module you have to use its name in a sentence the use the syntax after

## How To Install Pip
Go to this <a href="https://bootstrap.pypa.io/get-pip.py">site</a> and press CTRL + S and save it somewhere you will remember then in Command Prompt run the below command in the same directory as the file 
```
python get-pip.py
```
Then run the below command after you installed and restarted your pc in the same directory of requirements.txt
```
pip install -r requirements.txt
```

## Examples
Say "Calculate 1 plus 1" <br />
Response: "The sum of 1 plus 1 is 2"

## Create Basic Modules
Say "new basic module <NAME>" <br />
Open the file <NAME>.py in an IDE of your choice <br />
Under the run, function add whatever you want this module todo <br />
See <a href="https://github.com/Turnrp/ProjectJohn/blob/main/Modules/translate.py">translate.py</a>

## Create Custom Modules
Say "new custom module <NAME>" <br />
Open the file <NAME>.py in an IDE of your choice <br />
Under any function name, add whatever you want under it <br />
See <a href="https://github.com/Turnrp/ProjectJohn/blob/main/Modules/music.py">music.py</a>
