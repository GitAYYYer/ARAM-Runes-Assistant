# ARAM-Runes-Assistant
A quick and easy-to-use GUI to be your assistant for deciding what runes you should take on a champion, for the ARAM gamemode in League of Legends :) 

This was designed to help my friends play League of Legends better, and is all made with personal preference in mind.

## Setup
There isn't really setup involved, other than having the excel spreadsheet in the same directory as the ARAM-Runes-Assistant.exe file. 
The spreadsheet is currently in an old excel format, and I will look to update this in the future.

## Functionality
When you run the 'ARAM-Runes-Assistant.exe', a GUI window will pop up, with all the champions on the left hand side of the window.
The top left has a search bar, where you can search for a champion and the window will filter out champions based on your search. 
Pressing enter with a valid champion name will change the bottom right area of the window to show the runes I'd recommend taking on the entered champion.
You can also click on each champion portrait to bring up the recommended runes as well.

When inputting a champion to get runes for, the program will search for the champion's name in the spreadsheet and return the corresponding runes.

## Future Functionality
### Easy
- Provide each champion with a general description to how they play (e.g. Leona is a Warden who engages for her teammates).
- A general item-build or set of items for each champion.

### Medium
- Give tips or easy combos for each champion (this helps especially for champions like Riven who are reliant on combos)
- Recommend items for different situations, e.g. Zhonyas becomes very important for a mage when the enemy team has an AD Assassin.
    - This is different from recommending items in real-time; These are static and do not consider the strength of the item specific to the game, e.g. Zhonyas is not as important if the AD Assassin is 0/10.

### Hard
- Look at active game using League of Legends API and give info depending on enemy champions or ally champions
    - For example, as an enchanter support, you would value Ardent Censer a lot when your team has auto-attacking champions, but not so much when your team is heavily AP-stacked.
- Give specific champion vs champion knowledge 
    - This one seems much more complicated and honestly would take a very long time to collate since it's so specific, but would still be very helpful.

## Credit
Credit goes to 'Brent Vollebregt' at PyTutorials for making an application to convert Python files to .exe very easily. Video can be found at https://www.youtube.com/watch?v=OZSZHmWSOeM&list=PLRFfcI5ac25sL4zRlO3VpkSIbM021qRIa&index=15. 

Thanks to Eddy for some ideas and Adam for photoshopping some of the icons.

## Remember
This is my personal preference, and is tailored for my friends :)