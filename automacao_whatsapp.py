
#!pip install pyautogui
#!pip install pyperclip


import pyautogui
import pyperclip

import time
pyautogui.hotkey("ctrl", "t")
num = "https://api.whatsapp.com/send?phone=número da pessoa"
pyperclip.copy(num)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

## Aguardar para carregar o sistema antes de seguir
time.sleep(2)

texto =f"""
mensagem
"""
#copiar o a mensagem
pyperclip.copy(texto)
pyautogui.PAUSE = 0.1
#colar e enviar
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
