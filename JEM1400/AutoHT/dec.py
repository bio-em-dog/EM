from AutoHT import *
import pyautogui
import time
import pyperclip

# icon 1
# control 2 - beam 3
# HT scheduling 4
# Target HT Voltage 5
# step 6 0.1kV 7  - interval 8 1s 9
# start 10
# sleep 420 ((120-80)/0.1=400s)
# off 11

def decrease():
    for i in range(8):
        print("###### Do not move the mouse ######")
        time.sleep(1)
    temCenter("dec/0.png","dec/1.png")
    mouseClick(1,"left","dec/2.png",0)
    mouseClick(1,"left","dec/3.png",0)
    mouseClick(1,"left","dec/4.png",0)
    if mouseClick(2,"left","dec/5.png",60):
        inputValue(80)
    mouseClick(1,"left","dec/6.png",60)
    mouseClick(1,"left","dec/7.png",80)
    mouseClick(1,"left","dec/8.png",60)
    mouseClick(1,"left","dec/9.png",80)
    mouseClick(1,"left","dec/10.png",0)
    time.sleep(420)
    mouseClick(1,"left","dec/11.png",0)


if __name__ == "__main__":
    decrease()
    a=input("##### Finished, Press any key to continue #####")
