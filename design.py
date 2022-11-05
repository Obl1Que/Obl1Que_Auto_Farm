from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, pyautogui

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.n = 0

        self.setWindowTitle('Obl1Que Auto Farm')
        self.setGeometry(int(pyautogui.size()[0] / 2 - 400 / 2), int(pyautogui.size()[1] / 2 - 600 / 2), 400, 600)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Test text')
        self.main_text.move(25, 20)
        self.main_text.adjustSize()

        self.button = QtWidgets.QPushButton(self)
        self.button.move(100, 10)
        self.button.setText('Press button')
        self.button.setFixedWidth(275)
        self.button.clicked.connect(self.add_label)

    def add_label(self):
        self.n += 1
        self.new_text.setText(str(self.n))
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

application()