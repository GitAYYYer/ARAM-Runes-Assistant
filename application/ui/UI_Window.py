from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ChampionsScrollArea import ChampionSearchArea
from ui.RunesGroupbox import RunesArea
from ui.Icon import Icon
from ui.ChampionButton import ChampionButton
import math

global currentChampion
currentChampion = ""

global windowWidth, windowHeight
windowWidth = 1000
windowHeight = 900

global scrollAreaWidth, scrollAreaHeight
scrollAreaWidth = windowWidth * 0.6
scrollAreaHeight = windowHeight - 60

class Ui_MainWindow(QtWidgets.QWidget):
    championChanged = QtCore.pyqtSignal(str)
    runesChanged = QtCore.pyqtSignal(list)

    def __init__(self, MainWindow, filterChampions, getRunes):
        super().__init__()
        self.setupUi(MainWindow, filterChampions, getRunes)
        self.runesChanged.connect(self.groupbox.changeRunes)
        self.championChanged.connect(self.changeCurrentChampion)

    def setupUi(self, MainWindow, filterChampions, getRunes):
        MainWindow.setObjectName("Duc's ARAM Assistant")
        MainWindow.resize(windowWidth, windowHeight)

        # Helper funcs that use funcs from other file
        self.filterChampions = filterChampions
        self.getRunes = getRunes

        # Central for when choosing runes
        self.centralwidgetRunes = QtWidgets.QWidget(MainWindow)
        self.centralwidgetRunes.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidgetRunes)

        # Styling
        font = QtGui.QFont()
        font.setPointSize(16)

        # ScrollArea, and the gridlayout which goes inside the scroll area.
        self.scrollArea = ChampionSearchArea(scrollAreaWidth, scrollAreaHeight, self.centralwidgetRunes)

        # LineEdit, basically the champion search box
        self.championInput = QtWidgets.QLineEdit(self.centralwidgetRunes)
        self.championInput.setObjectName("championInput")
        self.championInput.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.championInput.setFont(font)
        self.championInput.setClearButtonEnabled(True)
        self.championInput.textChanged.connect(lambda: self.handleInputChange(self.championInput.text()))
        self.championInput.returnPressed.connect(lambda: self.handleInputEnter(self.championInput.text()))

        # GroupBox area, used to show runes itself. Updates when current runes changes
        self.groupbox = RunesArea(scrollAreaWidth, self.centralwidgetRunes)

        # Icon to display user's current champion selected.
        self.currentChampionIcon = Icon(60, self.centralwidgetRunes)
        xOffset = ((windowWidth - scrollAreaWidth) * 0.5) - 30
        yOffset = 10
        self.currentChampionIcon.setGeometry(scrollAreaWidth + xOffset, yOffset, 60, 60)

        # MenuBar, needed for some reason.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Show all champions on startup
        self.handleInputChange("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Duc's ARAM Assistant", "Duc's ARAM Assistant"))
        self.championInput.setPlaceholderText(_translate("championInput", "Enter Champion Here"))

    def handleInputChange(self, input):
        filteredChampions = self.filterChampions(input)

        # Clear current champions in layout
        for i in reversed(range(self.scrollArea.gridLayout.count())):
            self.scrollArea.gridLayout.itemAt(i).widget().setParent(None)

        # If no champions filtered, just return
        if len(filteredChampions) == 0:
            return

        # Determine number of rows and columns needed, given total filteredChampions
        totalColumns = 7
        totalRows = int(math.ceil(len(filteredChampions) / totalColumns))
        self.scrollArea.updateGeometry(totalRows)

        currentRow = 0
        currentCol = 0
        currentChampionRow = []
        for champ in filteredChampions:
            # First, check if this champion has multiple builds (if so, since we just want the name, get the token before ':')
            if ':' in champ:
                championName = champ.split(':')[0]
                currentChampionRow.append(champ)
            else:
                championName = champ
                currentChampionRow.append(championName)
            
            pixmap = QtGui.QPixmap("assets/champions/{0}Square.png".format(championName))
            btn = ChampionButton(champ, self, pixmap)
            self.scrollArea.addWidget(btn, currentRow, currentCol)
            currentCol += 1

            # When finishing a row, increment counters and create the next row to be labels for each champion's name
            if len(currentChampionRow) == 7:
                currentCol = 0
                # Add labels
                for currentChampion in currentChampionRow:
                    self.scrollArea.addWidget(QtWidgets.QLabel(currentChampion), currentRow + 1, currentCol)
                    currentCol += 1

                currentChampionRow.clear()
                currentRow += 2
                currentCol = 0

        # For the last row, add the labels
        currentCol = 0
        for currentChampion in currentChampionRow:
            self.scrollArea.addWidget(QtWidgets.QLabel(currentChampion), currentRow + 1, currentCol)
            currentCol += 1

    def handleInputEnter(self, input):
        returnDict = self.getRunes(input)
        if returnDict is None:
            return
        currentChampion = next(iter(returnDict))
        currentRunes = returnDict[currentChampion]
        self.championChanged.emit(currentChampion)
        self.runesChanged.emit(currentRunes)

    def changeCurrentChampion(self, currentChampion):
        pixmap = QtGui.QPixmap("assets/champions/{0}Square.png".format(currentChampion))
        self.currentChampionIcon.changeImage(pixmap)
        self.currentChampionIcon.hide()
        self.currentChampionIcon.show()


