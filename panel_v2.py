import os, subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import parce_log_pass as plp
from pathlib import Path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 250)
        MainWindow.setMinimumSize(QtCore.QSize(800, 250))
        MainWindow.setMaximumSize(QtCore.QSize(800, 250))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CheckAccounts = QtWidgets.QPushButton(self.centralwidget)
        self.CheckAccounts.setGeometry(QtCore.QRect(10, 10, 400, 50))
        self.CheckAccounts.setObjectName("CheckAccounts")

        self.AddmaFiles = QtWidgets.QPushButton(self.centralwidget)
        self.AddmaFiles.setGeometry(QtCore.QRect(10, 70, 400, 50))
        self.AddmaFiles.setObjectName("AddmaFiles")

        self.AddLogPass = QtWidgets.QPushButton(self.centralwidget)
        self.AddLogPass.setGeometry(QtCore.QRect(10, 130, 400, 50))
        self.AddLogPass.setObjectName("AddLogPass")

        self.StartFarming = QtWidgets.QPushButton(self.centralwidget)
        self.StartFarming.setGeometry(QtCore.QRect(10, 190, 400, 50))
        self.StartFarming.setObjectName("StartFarming")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(430, 10, 350, 230))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.CheckAccountsF()
        self.AddmaFilesF()
        self.AddLogPassF()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Obl1Que\'s CS:GO Panel"))
        self.CheckAccounts.setText(_translate("MainWindow", "CheckAccounts"))
        self.AddmaFiles.setText(_translate("MainWindow", "Add maFiles"))
        self.AddLogPass.setText(_translate("MainWindow", "Add LOGIN:PASSWORD"))
        self.StartFarming.setText(_translate("MainWindow", "Start Farming"))

    def CheckAccountsF(self):
        self.CheckAccounts.clicked.connect(lambda: self.ShowAccounts())

    def ShowAccounts(self):
        self.listWidget.clear()
        self.listWidget.addItems(plp.getLogPass('./accounts/log_pass.txt', 'mass'))

    def AddmaFilesF(self):
        self.AddmaFiles.clicked.connect(lambda: self.OpenFolder())

    def OpenFolder(self):
        subprocess.Popen(r'explorer /select,"C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\maFiles\_test.txt"')

    def AddLogPassF(self):
        self.AddLogPass.clicked.connect(lambda: self.openFile())

    def openFile(self):
        os.system(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\log_pass.txt')
        self.ShowAccounts()