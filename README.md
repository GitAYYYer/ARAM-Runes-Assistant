# ARAM-Runes-Assistant
A very basic runes assistant that references to Mobafire's interactive runes page, for League of Legends :)
Currently this application is run using the python command rather than having a .exe, as creating a .exe for every change I make is annoying (and also out of my scope).

## Setup
In 'ARAM-Runes-Assistant.py', there are two variables which might require changing to work. You change these in the config.json file.
- 'fileName' is the path to your .xlsx file which holds all champions and their runes.  
- 'chromePath' is the path to your chrome.exe. NOTE: When changing this to a different path, make sure to always append a space and '%s' to the end of the path.  

## Functionality
When you run 'python ARAM-Runes-Assistant.py', you will be prompted to enter a champion name, or 'exit' to exit the program.  
After entering a name, the program will search through the .xlsx file for the champion name inputted (case-insensitive) for a match.  
If it matches, a mobafire link will be opened to the runes for that champion.  
If there is no match, then there are likely multiple builds for that champion (and the program will tell you the closest matches).  
If there are no close matches, then you will be prompted again to try typing just the champion name.  