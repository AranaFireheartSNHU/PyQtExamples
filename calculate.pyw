#!/usr/bin/env python
__author__ = "Arana Fireheart"

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QTextBrowser, QVBoxLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit("Type an expression and press Enter")
        self.lineEdit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineEdit.text()
            self.browser.append("{0} = <b>{1}</b>".format(text, eval(text)))
        except:
            self.browser.append("<font color=red>{0} is invalid!</font>".format(text))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
