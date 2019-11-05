import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(220, 70, 47, 13))
        label.setObjectName("label")
        pushButtonArquivo = QtWidgets.QPushButton(self)
        pushButtonArquivo.setGeometry(QtCore.QRect(60, 320, 75, 23))
        pushButtonArquivo.setObjectName("pushButtonArquivo")
        pushButtonArquivo.clicked.connect(self.on_click)
        pushButton_2 = QtWidgets.QPushButton(self)
        pushButton_2.setGeometry(QtCore.QRect(440, 330, 75, 23))
        pushButton_2.setObjectName("pushButton_2")

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
