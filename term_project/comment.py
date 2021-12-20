# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 111)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ID1 = QtWidgets.QLabel(self.centralwidget)
        self.ID1.setGeometry(QtCore.QRect(10, 20, 45, 10))
        self.ID1.setObjectName("ID1")
        self.ID2 = QtWidgets.QLabel(self.centralwidget)
        self.ID2.setGeometry(QtCore.QRect(10, 50, 45, 10))
        self.ID2.setObjectName("ID2")
        self.ID3 = QtWidgets.QLabel(self.centralwidget)
        self.ID3.setGeometry(QtCore.QRect(10, 80, 45, 10))
        self.ID3.setObjectName("ID3")
        self.Comment1 = QtWidgets.QLabel(self.centralwidget)
        self.Comment1.setGeometry(QtCore.QRect(70, 20, 350, 10))
        self.Comment1.setObjectName("Comment1")
        self.Comment2 = QtWidgets.QLabel(self.centralwidget)
        self.Comment2.setGeometry(QtCore.QRect(70, 50, 350, 10))
        self.Comment2.setObjectName("Comment2")
        self.Comment3 = QtWidgets.QLabel(self.centralwidget)
        self.Comment3.setGeometry(QtCore.QRect(70, 80, 350, 10))
        self.Comment3.setObjectName("Comment3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ID1.setText(_translate("MainWindow", "TextLabel"))
        self.ID2.setText(_translate("MainWindow", "TextLabel"))
        self.ID3.setText(_translate("MainWindow", "TextLabel"))
        self.Comment1.setText(_translate("MainWindow", "TextLabel"))
        self.Comment2.setText(_translate("MainWindow", "TextLabel"))
        self.Comment3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
