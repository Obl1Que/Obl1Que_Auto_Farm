import os, subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import parce_log_pass as plp
import launch_cs as lcs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))

        self.itemsToLaunch = []

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

        self.AddServers = QtWidgets.QPushButton(self.centralwidget)
        self.AddServers.setGeometry(QtCore.QRect(10, 250, 400, 50))
        self.AddServers.setObjectName("AddServers")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(430, 10, 350, 230))
        self.listWidget.setObjectName("listWidget")

        self.confInfo = QtWidgets.QListWidget(self.centralwidget)
        self.confInfo.setGeometry(QtCore.QRect(10, 309, 770, 181))
        self.confInfo.setObjectName("confInfo")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.CheckAccountsF()
        self.AddmaFilesF()
        self.AddLogPassF()
        self.chooseItems()
        self.AddServersF()
        self.StartFarmingF()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Obl1Que\'s CS:GO Panel"))
        self.CheckAccounts.setText(_translate("MainWindow", "CheckAccounts"))
        self.AddmaFiles.setText(_translate("MainWindow", "Add maFiles"))
        self.AddLogPass.setText(_translate("MainWindow", "Add LOGIN:PASSWORD"))
        self.StartFarming.setText(_translate("MainWindow", "Start Farming"))
        self.AddServers.setText(_translate("MainWindow", "Add servers"))

    def CheckAccountsF(self):
        self.CheckAccounts.clicked.connect(lambda: self.ShowAccounts('./accounts/log_pass.txt', 'mass'))

    def ShowAccounts(self, path, typeOpen):
        self.itemsToLaunch.clear()
        self.listWidget.clear()
        self.listWidget.addItems(plp.getLogPass(path, typeOpen))
        self.confOut(f'Показаны аккаунты: {plp.getLogPass(path, typeOpen)}')

    def AddmaFilesF(self):
        self.AddmaFiles.clicked.connect(lambda: self.openFolder(r'explorer /select,"C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\maFiles\_test.txt"'))

    def AddLogPassF(self):
        self.AddLogPass.clicked.connect(lambda: self.openFile(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\log_pass.txt'))

    def openFile(self, path):
        os.system(path)

    def openFolder(self, path):
        subprocess.Popen(path)

    def chooseItems(self):
        self.listWidget.itemClicked.connect(self.choosenItems)

    def choosenItems(self, clItem):
        if ':27' not in clItem.text():
            if clItem.text() not in self.itemsToLaunch:
                self.itemsToLaunch.append(clItem.text())
                clItem.setBackground(QtGui.QColor(235, 242, 255))

            else:
                self.itemsToLaunch.remove(clItem.text())
                clItem.setBackground(QtGui.QColor(255, 255, 255))

            self.confOut(f'Выбраны аккаунты для запуска: {self.itemsToLaunch}')

    def AddServersF(self):
        self.AddServers.clicked.connect(lambda: self.confOut("Данная функция в разработке!"))
        self.AddServers.clicked.connect(lambda: self.openFile(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\servers.txt'))

    def confOut(self, str):
        self.confInfo.addItem(str)

    def StartFarmingF(self):
        self.StartFarming.clicked.connect(lambda: self.launchCSGO())

    def launchCSGO(self):
        lcs.launchCs(self.itemsToLaunch)