import subprocess, time
import pyautogui as pg
from steam_guard import getCode

win_width = pg.size()[0]
win_height = pg.size()[1]
accept_click = (win_width / 2, win_height / 2 - 25)

# Example

proc = subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe', '-login', 'makfa10', 'Sashok5544'])
code = getCode(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\76561198202337078.maFile')
time.sleep(4)
pg.click(accept_click)
pg.write(code)