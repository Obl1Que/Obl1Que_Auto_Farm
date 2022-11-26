import os
import json
import pyautogui as pg
import time
import subprocess
from steam_guard import getCode

win_size = (pg.size()[0], pg.size()[1])
cs_in_row = win_size[0] // 400
px_between_cs = round((win_size[0] - (400 * cs_in_row)) / (cs_in_row - 1))
accept_click = (win_size[0] / 2, win_size[1] / 2 - 35)

def parce_l_p(str):
    return str.split(':')

def startCS(dict_css):
    counterX = 0
    counterY = 0
    new_d = {}

    for acc in dict_css:
        if counterX == cs_in_row:
            counterX = 0
            counterY += 1

        login = dict_css[acc]["login"]
        password = dict_css[acc]["password"]

        # subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe','-login',str(login),str(password),'-applaunch','730','-low','-nohltv','-nosound','-novid','-window','-w','640','-h','480','+exec''autoexec.cfg', '+connect', '-x',str(counterX * (400 + px_between_cs)),'-y',str(counterY * 300)])

        # time.sleep(8)
        # code = getCode(dict_css[acc]["shared_secret"])
        # pg.click(accept_click)
        # pg.moveTo(accept_click[0] + 10, accept_click[1])
        # pg.write(code)
        new_d[login] = [counterX * (400 + px_between_cs), counterY * 300]
        # time.sleep(8)
        counterX += 1

    return new_d

def check_maFile(acc_login):
    direc = "accounts/maFiles"

    for i in os.listdir(direc):
        if not i.endswith(".txt"):
            j = json.loads(open(direc + '\\' + i, 'r').read())["account_name"]

            if acc_login == j:
                return True, json.loads(open(direc + '\\' + i, 'r').read())["shared_secret"]

    return False, 'None'

def launchCs(mass_log_pass):
    go_start = {}
    ngo_start = {}

    for i in mass_log_pass:
        acc_login = parce_l_p(i)[0]
        acc_password = parce_l_p(i)[1]

        if check_maFile(acc_login)[0]:
            is_maFale = check_maFile(acc_login)[0]
            shared_secret = check_maFile(acc_login)[1]

            go_start[acc_login] = {'login': acc_login,
                                    'password': acc_password,
                                    'shared_secret': shared_secret,
                                    'is_maFile': is_maFale}

        else:
            is_maFale = check_maFile(acc_login)[0]
            shared_secret = check_maFile(acc_login)[1]

            ngo_start[i] = {'login': acc_login,
                            'password': acc_password,
                            'shared_secret': shared_secret,
                            'is_maFile': is_maFale}

    win_cs = startCS(go_start)
    return win_cs, ngo_start