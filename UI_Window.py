from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, filterChampions, getRunes):
        MainWindow.setObjectName("Duc's ARAM Assistant")
        MainWindow.resize(840, 597)

        # Helper funcs that use funcs from other file
        self.filterChampions = filterChampions
        self.getRunes = getRunes

        # Styling and Layout
        font = QtGui.QFont()
        font.setPointSize(16)
        layout = QtWidgets.QGridLayout()

        # Central, needed for some reason.
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(layout)
        MainWindow.setCentralWidget(self.centralwidget)

        # LineEdit, basically the champion search box
        self.championInput = QtWidgets.QLineEdit(self.centralwidget)
        self.championInput.setObjectName("championInput")
        self.championInput.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.championInput.setFont(font)
        self.championInput.textChanged.connect(lambda: self.handleInputChange(self.championInput.text(), layout))
        self.championInput.returnPressed.connect(lambda: self.handleInputEnter(self.championInput.text()))

        # MenuBar, needed for some reason.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # StatusBar, default code but maybe not needed.
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Duc's ARAM Assistant", "Duc's ARAM Assistant"))
        self.championInput.setPlaceholderText(_translate("championInput", "Enter Champion Here"))

    def handleInputChange(self, input, layout):
        filteredChampions = self.filterChampions(input)

        # Clear current champions in layout
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

        # If no champions filtered, just return
        if len(filteredChampions) == 0:
            return

        # Determine number of rows and columns needed, given total filteredChampions
        totalColumns = int(math.sqrt(len(filteredChampions)))
        totalRows = int(math.ceil(len(filteredChampions) / float(totalColumns)))

        currentRow = 0
        currentCol = 0
        for champ in filteredChampions:
            layout.addWidget(ChampionButton(champ, self.getRunes), currentRow, currentCol)
            currentCol += 1
            if currentCol == totalColumns:
                currentRow += 1
                currentCol = 0

    def handleInputEnter(self, input):
        self.getRunes(input)

        
class ChampionButton(QtWidgets.QPushButton):
    def __init__(self, champion, getRunes, parent=None):
        super(ChampionButton, self).__init__(parent)
        self.champion = champion
        self.getRunes = getRunes
        self.setText(champion)
        self.clicked.connect(self.handleClick)

    def handleClick(self):
        self.getRunes(self.champion.lower())