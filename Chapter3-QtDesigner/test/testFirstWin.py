#!/usr/bin/env python
# encoding: utf-8
# testFirstWin.py in PyQt5-dev-book
# Created by maverick on 2018-12-19, 13:42
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: testFirstWin.py
@time: 2018-12-19 13:42
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui.ui_firstWin import Ui_Form

class MyUiClass(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(MyUiClass, self).__init__(parent)
        self.setupUi(self)  ##?


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    myWin: MyUiClass = MyUiClass()
    myWin.show()

    sys.exit(app.exec_())

