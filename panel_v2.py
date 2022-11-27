import os, subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import parce_log_pass as plp
import launch_cs as lcs
import json

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
        self.CheckAccounts.clicked.connect(lambda: self.ShowAccounts(os.path.abspath('accounts/log_pass.txt'), 'mass'))

    def ShowAccounts(self, path, typeOpen):
        self.itemsToLaunch.clear()
        self.listWidget.clear()

        for _ in plp.getLogPass(path, typeOpen):
            self.listWidget.addItem((_))
            if not lcs.check_maFile(plp.parceLogPass(_)[0])[0]:
                self.listWidget.item(self.listWidget.count() - 1).setBackground(QtGui.QColor(255, 140, 140, 255))

        self.confOut(f'Показаны аккаунты: {plp.getLogPass(path, typeOpen)}')
        self.confInfo.scrollToBottom()

    def AddmaFilesF(self):
        path = os.path.abspath('accounts/maFiles/_test.txt')
        self.AddmaFiles.clicked.connect(lambda: self.openFolder(rf'explorer /select,{path}'))
        self.AddmaFiles.clicked.connect(lambda: self.ShowAccounts(os.path.abspath('accounts/log_pass.txt'), 'mass'))

    def AddLogPassF(self):
        path = os.path.abspath('accounts/log_pass.txt')
        self.AddLogPass.clicked.connect(lambda: self.openFile(path))

    def openFile(self, path):
        os.system(path)

    def openFolder(self, path):
        folder = subprocess.Popen(path)

    def chooseItems(self):
        self.listWidget.itemClicked.connect(self.choosenItems)

    def choosenItems(self, clItem):
        if clItem.background().color().getRgb() != (255, 140, 140, 255) and clItem.background().color().getRgb() != (46, 252, 142, 255):
            if clItem.text() not in self.itemsToLaunch:
                self.itemsToLaunch.append(clItem.text())
                clItem.setBackground(QtGui.QColor(235, 242, 255, 255))

            else:
                self.itemsToLaunch.remove(clItem.text())
                clItem.setBackground(QtGui.QColor(255, 255, 255, 255))

            self.confOut(f'Выбраны аккаунты для запуска: {self.itemsToLaunch}')
            self.confInfo.scrollToBottom()

        elif clItem.background().color().getRgb() == (46, 252, 142, 255):
            self.CloseWin(plp.parceLogPass(clItem.text())[0])
            clItem.setBackground(QtGui.QColor(255, 255, 255, 255))

    def AddServersF(self):
        path = os.path.abspath("accounts/servers.txt")
        self.AddServers.clicked.connect(lambda: self.confOut("Данная функция в разработке!"))
        self.AddServers.clicked.connect(lambda: self.openFile(path))
        self.confInfo.scrollToBottom()

    def confOut(self, str):
        self.confInfo.addItem(str)

    def StartFarmingF(self):
        self.StartFarming.clicked.connect(lambda: self.launchCSGO())

    def CloseWin(self, login):
        file = open('win_opened.json')
        all_req = json.load(file)
        file.close()

        for acc in all_req.items():
            if acc[0] == login:
                file = open('win_opened.json')
                new_req = json.load(file)
                file.close()
                file = open('win_opened.json', 'w')
                new_req.pop(acc[0])
                file.write(json.dumps(new_req))
                file.close()

    def launchCSGO(self):
        start = lcs.launchCs(self.itemsToLaunch)
        self.itemsToLaunch.clear()
        go_start = start[0]
        not_go_start = start[1]

        for i in range(self.listWidget.count()):
            for j in not_go_start:
                if plp.parceLogPass(self.listWidget.item(i).text())[0] == j:
                    self.listWidget.item(i).setBackground(QtGui.QColor(255, 140, 140, 255))
            for k in go_start:
                if plp.parceLogPass(self.listWidget.item(i).text())[0] == k:
                    self.listWidget.item(i).setBackground(QtGui.QColor(46, 252, 142, 255))
        win_opened = open('win_opened.json', 'w')
        win_opened.write(json.dumps(start[0]))
        win_opened.close()

        # file = open('win_opened.json', 'r')
        # print(json.loads(file.read()))
        # file.close()