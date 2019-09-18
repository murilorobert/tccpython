# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SAIDA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot
import pygame
from Home import *


class Ui_Form(QWidget):

    def setupUi(self, Form, txt, path):
        self.file = path
        self.form=Form
        Form.setObjectName("Form")
        Form.resize(640, 443)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 571, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 410, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 410, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_click2)
        self.retranslateUi(Form, txt)
        QtCore.QMetaObject.connectSlotsByName(Form)

    @pyqtSlot()
    def on_click(self):
        self.playAudio(self.file)

    @pyqtSlot()
    def on_click2(self):
        print("passei")
        self.chamaHome()

    def playAudio(self, path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def retranslateUi(self, Form, txt):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setText(_translate("Form", txt))
        self.pushButton.setText(_translate("Form", "PLAY AUDIO"))
        self.pushButton_2.setText(_translate("Form", "HOME"))

    def chamaHome(self):

        self.AspideRecognizer = QtWidgets.QWidget()
        self.ui = Ui_AspideRecognizer()
        self.ui.setupUi(self.AspideRecognizer)
        self.form.close()
        self.AspideRecognizer.show()
        print("To aqui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
