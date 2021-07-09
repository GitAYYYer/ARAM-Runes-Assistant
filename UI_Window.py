from PyQt5 import QtCore, QtGui, QtWidgets
import math

# The current champion that the user has selected (through the getRunes method)
global currentChampion
currentChampion = ""

global windowWidth, windowHeight
windowWidth = 1000
windowHeight = 800

global scrollAreaWidth, scrollAreaHeight
scrollAreaWidth = windowWidth * 0.6
scrollAreaHeight = windowHeight - 60

class RunesArea(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super(RunesArea, self).__init__(parent)
        self.setObjectName("runesArea")
        self.setGeometry(QtCore.QRect(scrollAreaWidth + 20, windowHeight*0.6, (windowWidth*0.4)-30, windowHeight*0.4-10))
        self.keystone = QtWidgets.QLabel()

class ChampionSearchArea(QtWidgets.QScrollArea):
    def __init__(self, parent):
        super(ChampionSearchArea, self).__init__(parent)
        self.setObjectName("scrollArea")
        self.setGeometry(QtCore.QRect(10, 50, scrollAreaWidth, scrollAreaHeight))
        self.setWidgetResizable(False)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, scrollAreaWidth - 2, 0))

        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, scrollAreaWidth - 50, 0))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.setWidget(self.scrollAreaWidgetContents)

    def addWidget(self, widget, row, col):
        self.gridLayout.addWidget(widget, row, col, QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)

    # Used when filtering view to match number of rows needed
    def updateGeometry(self, totalRows):
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, scrollAreaWidth - 2, 130*totalRows))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, scrollAreaWidth - 49, 90*totalRows))

class Ui_MainWindow(object):
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
        self.scrollArea = ChampionSearchArea(self.centralwidgetRunes)

        # LineEdit, basically the champion search box
        self.championInput = QtWidgets.QLineEdit(self.centralwidgetRunes)
        self.championInput.setObjectName("championInput")
        self.championInput.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.championInput.setFont(font)
        self.championInput.setClearButtonEnabled(True)
        self.championInput.textChanged.connect(lambda: self.handleInputChange(self.championInput.text()))
        self.championInput.returnPressed.connect(lambda: self.handleInputEnter(self.championInput.text()))

        # GroupBox area, used to show runes itself
        self.groupbox = RunesArea(self.centralwidgetRunes)

        # MenuBar, needed for some reason.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # StatusBar, default code but maybe not needed.
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

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
        # totalColumns = int(math.sqrt(len(filteredChampions)))
        # totalRows = int(math.ceil(len(filteredChampions) / float(totalColumns)))
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
            btn = ChampionButton(champ, self.getRunes, pixmap)
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
        currentChampion = self.getRunes(input)
        print(currentChampion)

class RuneIcon(QtWidgets.QLabel):
    def __init__(self, parent):
        super(RuneIcon, self).__init__(parent)
        self.pixmap = None

    def changeImage(self, pixmap):
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
        
class ChampionButton(QtWidgets.QPushButton):
    def __init__(self, champion, getRunes, pixmap, parent=None):
        super(ChampionButton, self).__init__(parent)
        self.length = 60
        self.champion = champion
        self.getRunes = getRunes
        self.pixmap = pixmap

        self.setText(champion)
        self.setToolTip(champion)
        self.clicked.connect(self.handleClick)
        self.setFixedWidth(self.length)
        self.setFixedHeight(self.length)

    def handleTooltip():
        if True:
            return

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

    def handleClick(self):
        self.getRunes(self.champion.lower())