import pyautogui
from random import randint
from time import sleep
import sys


dict_treasure = {
                    'gifts': 'image/dari.PNG',
                    'treasure1': 'image/socrovishe.PNG',
                    'treasure2': 'image/socrovishe2.PNG',
                    'treasure3': 'image/socrovishe3.PNG',
                    'treasure5': 'image/socrovishe5.PNG',
                    'treasure6': 'image/socrovishe6.PNG',
                    }

dict_find_and_fight = {
                        'fight': "image/napastdungeon.PNG",
                        'drive_away': 'image/progon.PNG',
                        'find': "image/obiskat.PNG"
                        }


def find_and_click_picture(picture):
    if button := pyautogui.locateOnScreen(picture, confidence=0.8):
        pyautogui.click(button)
        return True
    else:
        return False


def find_picture(picture):
    if pyautogui.locateOnScreen(picture, confidence=0.8):
        return True
    else:
        return False


pyautogui.alert('You ready?')
while True:
    if find_and_click_picture(dict_find_and_fight['find']):
        sleep(randint(83, 86))
    else:
        find_and_click_picture(dict_find_and_fight['fight'])
        sleep(randint(2, 3))
        for now_picture in dict_treasure:
            now_picture = dict_treasure[now_picture]
            if find_picture(now_picture):
                pyautogui.alert('Сongratulations on your find')
                sys.exit()
        find_and_click_picture(dict_find_and_fight['drive_away'])
        sleep(randint(2, 3))
