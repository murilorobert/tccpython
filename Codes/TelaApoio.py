# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaApoio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaApoio():
    def setupUi(self, Form, txt):
        Form.setObjectName("Form")
        Form.resize(359, 107)
        self.texto = QtWidgets.QLabel(Form)
        self.texto.setGeometry(QtCore.QRect(40, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.texto.setFont(font)
        self.texto.setObjectName("texto")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aspide Recognizer"))
        self.texto.setText(_translate("Form", "Transcrevendo..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaApoio()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
