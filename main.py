import os, subprocess
import ait as autoit
from steam_guard import getCode
from parce_log_pass import getLogPass

# Example
path_to_steam = '"C:/Program Files (x86)/Steam/steam.exe" -login ilias_122 Sashok5544'

# os.startfile(path_to_steam)
# print('1')

subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe', '-login', 'ilias_122', 'Sashok5544'])

# autoit.win_wait("Steam Guard")
# autoit.win_activate("Steam Guard")
# autoit.win_wait_active("Steam Guard")
# autoit.send(getCode('C:\\Users\\sdezh\\PycharmProjects\\Obl1Que_Auto_Farm\\76561198191656163.maFile'))
