from PyQt5 import QtCore, QtGui, QtWidgets

class ChampionSearchArea(QtWidgets.QScrollArea):
    def __init__(self, scrollAreaWidth, scrollAreaHeight, parent):
        super(ChampionSearchArea, self).__init__(parent)
        self.scrollAreaWidth = scrollAreaWidth
        self.scrollAreaHeight = scrollAreaHeight
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.scrollAreaWidth - 2, 130*totalRows))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, self.scrollAreaWidth - 15, 90*totalRows))