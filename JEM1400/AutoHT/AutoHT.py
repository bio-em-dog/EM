import pyautogui
import time
import pyperclip


def mouseClick(clickTimes,LR,img,shift):
    location=pyautogui.locateCenterOnScreen(img,confidence=0.9) # 0.9
    if location:
        pyautogui.click(location.x+shift, location.y, clicks=clickTimes, interval=0.2, duration=0.2,button=LR)
        print(img,location.x, location.y)
        ok=1
    else:
        ok=0
        print(img,"button not found")
    time.sleep(1)
    if ok == 1:
        ok=0
        return(1)

def inputValue(value):
    pyperclip.copy(value)
    pyautogui.hotkey('ctrl','v')

def temCenter(png1,png2):
    for i in range(5):
        location=pyautogui.locateCenterOnScreen(png1,confidence=0.9)
        if location:
            print("On")
        else:
            mouseClick(1,"left",png2,0)


