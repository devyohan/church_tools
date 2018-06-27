import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 862)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtVerseInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtVerseInput.setGeometry(QtCore.QRect(10, 10, 291, 301))
        self.txtVerseInput.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.txtVerseInput.setObjectName("txtVerseInput")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.txtResult = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtResult.setGeometry(QtCore.QRect(10, 360, 291, 451))
        self.txtResult.setObjectName("txtResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSdlfkjsdf = QtWidgets.QAction(MainWindow)
        self.actionSdlfkjsdf.setObjectName("actionSdlfkjsdf")
        self.menu.addAction(self.actionSdlfkjsdf)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.menu.setTitle(_translate("MainWindow", "기능"))
        self.actionSdlfkjsdf.setText(_translate("MainWindow", "Delete"))

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Helloworld')
    w.show()

    sys.exit(app.exec_())
