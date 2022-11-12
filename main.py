from panel_v2 import *
from PyQt5 import QtGui, QtWidgets
import sys, ctypes, os

try:
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system("pip install -r requirements.txt")
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon('./img/icon.png'))

        MainWindow = QtWidgets.QMainWindow()
        MainWindow.setWindowIcon(QtGui.QIcon('./img/icon.png'))

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        MainWindow.show()
        sys.exit(app.exec_())
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
except Exception as ex:
    input(f"\n\n\n{ex}")
