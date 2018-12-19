# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myForm(object):
    def setupUi(self, myForm):
        myForm.setObjectName("myForm")
        myForm.resize(628, 427)
        self.pushButton = QtWidgets.QPushButton(myForm)
        self.pushButton.setGeometry(QtCore.QRect(420, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(myForm)
        self.pushButton.clicked['bool'].connect(myForm.close)
        QtCore.QMetaObject.connectSlotsByName(myForm)

    def retranslateUi(self, myForm):
        _translate = QtCore.QCoreApplication.translate
        myForm.setWindowTitle(_translate("myForm", "Form"))
        self.pushButton.setText(_translate("myForm", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myForm = QtWidgets.QWidget()
    ui = Ui_myForm()
    ui.setupUi(myForm)
    myForm.show()
    sys.exit(app.exec_())

