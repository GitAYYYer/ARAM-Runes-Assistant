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
    # Define all necessary variables to place into URL.
    championName = raw_input("Enter your champion name: ")
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

    for i in range (1, sheet.nrows):
        # i refers to row number, the second value refers to the column.
        # Columns are in the same order as variables above.
        # 0 = Champion Name, 1 = Primary Tree, etc.
        if (sheet.cell_value(i, 0).lower() == championName.lower()):
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