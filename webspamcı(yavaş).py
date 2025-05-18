
import pyautogui
import time

def mesaj():                 
    pyautogui.write("legacytsla sohbetın ıçınden geçıyor")
    pyautogui.press("enter")

while True:
    mesaj()
    time.sleep(1)  
