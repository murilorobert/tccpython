# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaTrancrevendo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from Codes import capta_audio


class Ui_TelaTranscrevendo(QWidget):
    def setupUi(self, TelaTranscrevendo):
        TelaTranscrevendo.setObjectName("TelaTranscrevendo")
        TelaTranscrevendo.resize(295, 95)
        self.label = QtWidgets.QLabel(TelaTranscrevendo)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(TelaTranscrevendo)
        QtCore.QMetaObject.connectSlotsByName(TelaTranscrevendo)

    def retranslateUi(self, TelaTranscrevendo):
        _translate = QtCore.QCoreApplication.translate
        TelaTranscrevendo.setWindowTitle(_translate("TelaTranscrevendo", "Aspide Recognizer"))
        self.label.setText(_translate("TelaTranscrevendo", "Transcrevendo..."))

    def trancrever(self, file):
        txt = capta_audio.transc_file(file)
        print("to Aqui")
        self.openWindow(txt, file)
        #self.TelaTranscrevendo.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaTranscrevendo = QtWidgets.QWidget()
    ui = Ui_TelaTranscrevendo()
    ui.setupUi(TelaTranscrevendo)
    TelaTranscrevendo.show()
    sys.exit(app.exec_())
