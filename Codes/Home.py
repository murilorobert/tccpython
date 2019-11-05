# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot
from time import sleep as wait
from tkinter import *
import capta_audio
from Saida import *


class Ui_AspideRecognizer(QWidget):
    def setupUi(self, AspideRecognizer):
        self.asp = AspideRecognizer
        AspideRecognizer.setObjectName("AspideRecognizer")
        AspideRecognizer.resize(523, 351)
        self.label_2 = QtWidgets.QLabel(AspideRecognizer)
        self.label_2.setGeometry(QtCore.QRect(125, 20, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label1 = QtWidgets.QLabel(AspideRecognizer)
        self.label1.setGeometry(QtCore.QRect(55, 40, 640, 200))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label")
        #botão audio
        self.pushButton_3 = QtWidgets.QPushButton(AspideRecognizer)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 240, 85, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_click2)
        #botão arquivo
        self.pushButton = QtWidgets.QPushButton(AspideRecognizer)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 100, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arquivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(AspideRecognizer)
        QtCore.QMetaObject.connectSlotsByName(AspideRecognizer)

    @pyqtSlot()
    def on_click(self):

        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                      "Arquivo WAV(*.wav)", options=options)
            if fileName:
                self.telaApoio(fileName)
        except ValueError:
            print("Erro");

    @pyqtSlot()
    def on_click2(self):
        print("passei")
        fileName = capta_audio.entrada_microfone()
        if fileName:
            self.trancrever(fileName)

    def retranslateUi(self, AspideRecognizer):
        _translate = QtCore.QCoreApplication.translate
        AspideRecognizer.setWindowTitle(_translate("AspideRecognizer", "Aspide Recognizer"))
        self.label_2.setText(_translate("AspideRecognizer", "Aspide Recognizer"))
        self.label1.setText(_translate("AspideRecognizer", "Ferramenta de trancrição de audio em texto!\n \n\n\nSelecione a forma de transcrição:"))
        self.pushButton_3.setText(_translate("AspideRecognizer", "Audio"))
        self.pushButton.setText(_translate("AspideRecognizer", "Arquivo"))

    def openWindow(self, txt, path):

        self.Form = QtWidgets.QWidget()
        from Codes.Saida import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form, txt, path)
        self.asp.hide()
        self.Form.show()

    def telaApoio(self, fileName):
        #class Application:
        #    def __init__(self, master=None):
        #        self.widget1 = Frame(master)
        #        self.widget1.pack()
        #        self.msg = Label(self.widget1, text="Primeiro Widget")
        #        self.msg.pack()
        #self.tela = Tk()
        #Application(self.tela)
        #self.tela.mainloop(0)

        #self.asp.hide()
        #self.TelaTranscrevendo = QtWidgets.QWidget()
        #from Codes.telaTranscrevendo import Ui_TelaTranscrevendo
        #self.ui = Ui_TelaTranscrevendo()
        #self.ui.setupUi(self.TelaTranscrevendo)
        #self.TelaTranscrevendo.clearFocus()
        #self.TelaTranscrevendo.show()
        print(fileName)
        print("to Aqui")
        self.trancrever(fileName)


    def trancrever(self, file):
        wait(2)
        txt = capta_audio.transc_file(file)
        if txt:
            print("to Aqui")
            self.openWindow(txt, file)
        # self.TelaTranscrevendo.close()
        #self.tela.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AspideRecognizer = QtWidgets.QWidget()
    ui = Ui_AspideRecognizer()
    ui.setupUi(AspideRecognizer)
    AspideRecognizer.show()
    sys.exit(app.exec_())
