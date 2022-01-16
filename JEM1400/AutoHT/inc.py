from AutoHT import *
import pyautogui
import time
import pyperclip

# icon 1
# control 2 - beam 3
# HT scheduling 4
# Target HT Voltage 5
# step 6 0.05kV 7  - interval 8 5s 9
# 60 10 - on 11
# wait 1min
# start 12

def increase():
    for i in range(8):
        print("###### Do not move the mouse ######")
        time.sleep(1)
    temCenter("dec/0.png","dec/1.png")
    mouseClick(1,"left","inc/2.png",0)
    mouseClick(1,"left","inc/3.png",0)
    mouseClick(1,"left","inc/4.png",0)
    if mouseClick(2,"left","inc/5.png",60):
        inputValue(120)
    mouseClick(1,"left","inc/6.png",60)
    mouseClick(1,"left","inc/7.png",80)
    mouseClick(1,"left","inc/8.png",60)
    mouseClick(1,"left","inc/9.png",80)
    mouseClick(1,"left","inc/10.png",0)
    mouseClick(1,"left","inc/11.png",0)
    time.sleep(60)
    mouseClick(1,"left","inc/12.png",0)


if __name__ == "__main__":
    increase()
    a=input("##### Finished, Press any key to continue #####")