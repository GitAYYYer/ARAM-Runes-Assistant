from PyQt5 import QtCore, QtGui, QtWidgets

class ChampionButton(QtWidgets.QPushButton):
    championChanged = QtCore.pyqtSignal(str)
    runesChanged = QtCore.pyqtSignal(list)

    def __init__(self, champion, MainWindow, pixmap, parent=None):
        super(ChampionButton, self).__init__(parent)
        self.length = 60
        self.champion = champion
        self.getRunes = MainWindow.getRunes
        self.groupbox = MainWindow.groupbox
        self.pixmap = pixmap

        self.setText(champion)
        self.setToolTip(champion)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clicked.connect(self.handleClick)
        self.setFixedWidth(self.length)
        self.setFixedHeight(self.length)
        self.championChanged.connect(MainWindow.changeCurrentChampion)
        self.runesChanged.connect(MainWindow.groupbox.changeRunes)

    def handleTooltip():
        if True:
            return

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

    def handleClick(self):
        returnDict = self.getRunes(self.champion.lower())
        currentChampion = next(iter(returnDict))
        currentRunes = returnDict[currentChampion]
        self.championChanged.emit(currentChampion)
        self.runesChanged.emit(currentRunes)