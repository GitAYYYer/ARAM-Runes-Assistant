# Program to get a champion name, then construct a reference URL to send to Mobafire and retrieve runes.
# Example URL:
# https://www.mobafire.com/league-of-legends/rune-page-planner#&rune=Precision:1:16:19:22::Inspiration:52:56:::Shards:1:1:4
import xlrd
import webbrowser
import win32gui
import win32con
import sys
from difflib import SequenceMatcher
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_Window import Ui_MainWindow

# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Give the file path of the file you want to read from:
fileName = "Champion-Runes-Old-Format.xls"
# Give the file path of your Chrome:
# If you're using windows, make sure to use forward slashes '/' and to append ' %s' at the end of your path.
chromePath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

# To open Excel Workbook 
workbook = xlrd.open_workbook(fileName) 
sheet = workbook.sheet_by_name("Champion Runes")

# Lists of champions, to use when searching for champion in line edit box
allChampions = []
filteredChampions = []

# Helper function to get similarity of two texts, not used currently.
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Used to open chrome.
def getWindowText(hwnd):
    buf_size = 1 + win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
    buf = win32gui.PyMakeBuffer(buf_size)
    win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, buf_size, buf)
    return str(buf)

# Called once at the start to load all champions into a list to filter on later.
def loadChampions():
    for i in range(1, sheet.nrows):
        allChampions.append(sheet.cell_value(i, 0))

# Called every time input is changed; will look through each champion and see if user input is similar to champion name
def filterChampions(input):
    filteredChampions.clear()

    for champion in allChampions:
        # If input is empty, there is no filter, return all champions.
        if not input:
            return allChampions
        elif input.lower() in champion.lower():
            filteredChampions.append(champion)

    return filteredChampions


def getRunes(championNameInput):
    # If nothing in the search, do nothing.
    if championNameInput is None:
        return

    # Define all necessary variables to place into URL.
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
        championNameSpreadsheet = sheet.cell_value(i, 0).lower()

        # if the input is a substring of the spreadsheet champion name, then check if the values are equal (in which case, you give the runes for that champion).
        if (championNameInput in championNameSpreadsheet):
            # i refers to row number, the second value refers to the column.
            # Columns are in the same order as variables above.
            # 0 = Champion Name, 1 = Primary Tree, etc.
            if (championNameSpreadsheet == championNameInput):
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

                # Gets chrome tabs
                hwnd = win32gui.GetForegroundWindow()
                omniboxHwnd = win32gui.FindWindowEx(hwnd, 0, 'Chrome_OmniboxView', None)

                baseURL = 'https://www.mobafire.com/league-of-legends/rune-page-planner#&rune={}:{}:{}:{}:{}::{}:{}:{}:::Shards:{}:{}:{}'
                newURL = baseURL.format(primaryTree, keyStone, topRune, midRune, bottomRune, secondaryTree, secondaryR1, secondaryR2, stat1, stat2, stat3)
                webbrowser.get(chromePath).open(newURL)

                return championNameInput
    return None
        
if __name__ == '__main__':
    # First, load all the champions
    loadChampions()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, filterChampions, getRunes)
    MainWindow.show()
    sys.exit(app.exec_())