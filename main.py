import subprocess, time
import pyautogui as pg
from panel_v2 import *
from steam_guard import getCode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWinExtras import QtWin
import sys

# win_width = pg.size()[0]
# win_height = pg.size()[1]
# accept_click = (win_width / 2, win_height / 2 - 25)

# Example

# proc = subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe', '-login', 'makfa10', 'Sashok5544'])
# code = getCode(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\76561198202337078.maFile')
# time.sleep(4)
# pg.click(accept_click)
# pg.write(code)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./img/icon.png'))

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('./img/icon.png'))

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())