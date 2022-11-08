import pyautogui as pg
import time
import subprocess
from steam_guard import getCode

win_size = (pg.size()[0], pg.size()[1])
cs_in_row = win_size[0] // 480
px_between_cs = round((win_size[0] - (480 * cs_in_row)) / (cs_in_row - 1))
accept_click = (win_size[0] / 2, win_size[1] / 2 - 25)

cs_windows = {}

def launchCs(login, password, guardCode, posX, posY):
    proc = subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe', '-login', str(login), str(password), '-applaunch', '730', '-low',
                             '-nohltv', '-nosound', '-novid', '-window', '-w', '640', '-h', '480', '+exec', 'autoexec.cfg', '-x', str(posX), '-y', str(posY), '+connect', 'ipadress', '+password', 'pass'])

    time.sleep(5)
    pg.click(accept_click)
    pg.write(guardCode)

    cs_windows[login] = ('launch', posX, posY)

code = getCode(r'C:\Users\sdezh\PycharmProjects\Obl1Que_Auto_Farm\accounts\maFiles\76561197777777777.maFile')

launchCs('login', 'password', code, 100, 100)
print(code)
print(cs_windows)