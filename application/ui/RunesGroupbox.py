from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Icon import Icon

global windowWidth, windowHeight
windowWidth = 1000
windowHeight = 900

class RunesArea(QtWidgets.QGroupBox):
    def __init__(self, scrollAreaWidth, parent):
        super(RunesArea, self).__init__(parent)
        self.setObjectName("runesArea")
        self.width = (windowWidth * 0.4) - 30
        self.height = windowHeight * 0.5 - 10
        self._rect = QtCore.QRect(scrollAreaWidth + 20, windowHeight * 0.5, self.width, self.height)
        self.setGeometry(self._rect)

        # Styling
        self.setStyleSheet("QGroupBox#runesArea { border: 1px solid grey; }")

        # PrimaryLayout is the vertical which contains primary runes, Secondary is for secondary runes + the stat runes
        self.primaryLayoutWidget = QtWidgets.QWidget(self)
        self.primaryLayoutWidget.setObjectName("primaryLayoutWidget")
        self.primaryLayoutWidget.setGeometry(QtCore.QRect(self.width * 0.2, 20, 81, self.height * 0.95))
        self.primaryLayout = QtWidgets.QVBoxLayout(self.primaryLayoutWidget)
        self.primaryLayout.setObjectName("primaryLayout")
        self.primaryLayout.setContentsMargins(0, 0, 0, 0)

        self.secondaryLayoutWidget = QtWidgets.QWidget(self)
        self.secondaryLayoutWidget.setObjectName("secondaryLayoutWidget")
        self.secondaryLayoutWidget.setGeometry(QtCore.QRect(self.width*0.6, 20, 81, self.height * 0.95))
        self.secondaryLayout = QtWidgets.QVBoxLayout(self.secondaryLayoutWidget)
        self.secondaryLayout.setObjectName("secondaryLayout")
        self.secondaryLayout.setContentsMargins(0, 0, 0, 0)

        # First, generate the labels for each rune. Do this to have reference to the runes, to change it whenever user changes their champion
        self.runeLabels = []
        runeIconSize = 50
        for i in range(11):
            if i < 5:
                rune = Icon(runeIconSize, self.primaryLayoutWidget)
                self.runeLabels.append(rune)
                self.primaryLayout.addWidget(rune)
            else:
                rune = Icon(runeIconSize, self.secondaryLayoutWidget)
                self.runeLabels.append(rune)
                self.secondaryLayout.addWidget(rune)

    # For each label in runeLabels, change it to match currentRunes
    def changeRunes(self, currentRunes):
        for i in range(11):
            # The stat runes are prefixed by the word 'Stat' before their rune number, hence handle using if condition.
            if i < 8:
                pixmap = QtGui.QPixmap("assets/runes/{0}.png".format(currentRunes[i]))
            else:
                pixmap = QtGui.QPixmap("assets/runes/Stat{0}.png".format(currentRunes[i]))
            self.runeLabels[i].changeImage(pixmap)

        # Not the best practice, but works for now. Should instead do some threading I think.
        self.hide()
        self.show()