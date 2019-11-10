# Program to get a champion name, then construct a reference URL to send to Mobafire and retrieve runes.
# Example URL:
# https://www.mobafire.com/league-of-legends/rune-page-planner#&rune=Precision:1:16:19:22::Inspiration:52:56:::Shards:1:1:4
import xlrd
import webbrowser

# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Give the file path of the file you want to read from:
fileName = "Champion-Runes.xlsx"
# Give the file path of your Chrome:
# If you're using windows, make sure to use forward slashes '/' and to append ' %s' at the end of your path.
chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# To open Excel Workbook 
workbook = xlrd.open_workbook(fileName) 
sheet = workbook.sheet_by_name("Champion Runes") 

if __name__ == "__main__":
    while True:
        # Define all necessary variables to place into URL.
        championNameInput = raw_input("Enter your champion name: ").lower()
        primaryTree = ""
        keyStone = ""
        topRune = ""
        midRune = ""
        bottomRune = ""
        secondaryTree = ""
        secondaryR1 = ""
        secondaryR2 = ""
        stat1 = ""
        stat2 = ""
        stat3 = ""

        # If the input matches a value in the spreadsheet, set to true. If still false after going through spreadsheet,
        # then find the closest matches and print them to user.
        championFound = False
        closestMatches = []

        for i in range (1, sheet.nrows):
            championNameSpreadsheet = sheet.cell_value(i, 0).lower()

            # if the input is a substring of the spreadsheet champion name, then check if the values are equal (in which case, you give the runes for that champion).
            if (championNameInput in championNameSpreadsheet):
                # i refers to row number, the second value refers to the column.
                # Columns are in the same order as variables above.
                # 0 = Champion Name, 1 = Primary Tree, etc.
                if (championNameSpreadsheet == championNameInput):
                    championFound = True
                    primaryTree = sheet.cell_value(i, 1)
                    keyStone = int(sheet.cell_value(i, 2))
                    topRune = int(sheet.cell_value(i, 3))
                    midRune = int(sheet.cell_value(i, 4))
                    bottomRune = int(sheet.cell_value(i, 5))
                    secondaryTree = sheet.cell_value(i, 6)
                    secondaryR1 = int(sheet.cell_value(i, 7))
                    secondaryR2 = int(sheet.cell_value(i, 8))
                    stat1 = int(sheet.cell_value(i, 9))
                    stat2 = int(sheet.cell_value(i, 10))
                    stat3 = int(sheet.cell_value(i, 11))

                    baseURL = 'https://www.mobafire.com/league-of-legends/rune-page-planner#&rune={}:{}:{}:{}:{}::{}:{}:{}:::Shards:{}:{}:{}'
                    newURL = baseURL.format(primaryTree, keyStone, topRune, midRune, bottomRune, secondaryTree, secondaryR1, secondaryR2, stat1, stat2, stat3)
                    webbrowser.get(chromePath).open(newURL)
                # else, the input was a substring but not a full match, meaning there are multiple rune builds that can be returned.
                else:
                    closestMatches.append(championNameSpreadsheet)
            
        # Print the closest matches.
        if (championFound == False):
            print("Couldn't find a match.")
            if (len(closestMatches) > 0):
                print("Closest matches:")
                for build in closestMatches:
                    print(build)
                print("")
            else:
                print("No close match could be found. Try typing just the champion name.")