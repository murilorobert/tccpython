# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot


class Ui_AspideRecognizer(QWidget):
    def setupUi(self, AspideRecognizer):
        AspideRecognizer.setObjectName("AspideRecognizer")
        AspideRecognizer.resize(523, 351)
        self.label_2 = QtWidgets.QLabel(AspideRecognizer)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(AspideRecognizer)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 210, 75, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(AspideRecognizer)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 81, 71))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(AspideRecognizer)
        QtCore.QMetaObject.connectSlotsByName(AspideRecognizer)

    @pyqtSlot()
    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        
    def retranslateUi(self, AspideRecognizer):
        _translate = QtCore.QCoreApplication.translate
        AspideRecognizer.setWindowTitle(_translate("AspideRecognizer", "Aspide Recognizer"))
        self.label_2.setText(_translate("AspideRecognizer", "Aspide Recognizer"))
        self.pushButton_3.setText(_translate("AspideRecognizer", "Audio"))
        self.pushButton.setText(_translate("AspideRecognizer", "Arquivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AspideRecognizer = QtWidgets.QWidget()
    ui = Ui_AspideRecognizer()
    ui.setupUi(AspideRecognizer)
    AspideRecognizer.show()
    sys.exit(app.exec_())
