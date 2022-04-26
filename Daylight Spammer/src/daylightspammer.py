import pyautogui
import webbrowser
import time


message =input("message to spam (leave blank to spam what is in clip board):")
messageRepeat = int(input("send message x times:"))
delay = int(input("ms between messages:"))
text = '''
██████╗░░█████╗░██╗░░░██╗██╗░░░░░██╗░██████╗░██╗░░██╗████████╗
██╔══██╗██╔══██╗╚██╗░██╔╝██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝
██║░░██║███████║░╚████╔╝░██║░░░░░██║██║░░██╗░███████║░░░██║░░░
██║░░██║██╔══██║░░╚██╔╝░░██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░
██████╔╝██║░░██║░░░██║░░░███████╗██║╚██████╔╝██║░░██║░░░██║░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝'''
input(text)
isLoaded = input("press enter when discord is loaded...")

print("Starting in 5 seconds...")

time.sleep(5)

for i in range(0, messageRepeat):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl','v')
        pyautogui.press("enter")

        time.sleep(delay/1000)

print("Done\n")