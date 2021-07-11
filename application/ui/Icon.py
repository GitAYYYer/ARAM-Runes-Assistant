from PyQt5 import QtCore, QtGui, QtWidgets

class Icon(QtWidgets.QLabel):
    def __init__(self, length, parent):
        super(Icon, self).__init__(parent)
        # Might need to pass object name into this, if necessary.
        self.setObjectName("icon")
        self.length = length
        self.pixmap = None
        self.setMinimumSize(QtCore.QSize(length, length))
        self.setMaximumSize(QtCore.QSize(length, length))

    def changeImage(self, pixmap):
        self.pixmap = pixmap

    def paintEvent(self, event):
        if self.pixmap is None:
            return
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

    def sizeHint(self):
        if self.pixmap is not None:
            return self.pixmap.size()
        else:
            return QtCore.QSize(self.length, self.length)