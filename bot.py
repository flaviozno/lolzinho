from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x ,y)
    

def verifica():
    button_pos = pyautogui.locateOnScreen('./aceitar.png')
    print('Relaxa que tem tempo ainda amigo')

    if button_pos != None:
        print('ACHOU PARTIDA ARROMBADO')
        click(button_pos.left, button_pos.top)
        
    return False

def main():
    print('Pode dar um mijão tranquilo amigo eu cuido de tudo',  end="\n\n\n")
    
    while True: 
        if verifica():
            sleep(4)

main()            