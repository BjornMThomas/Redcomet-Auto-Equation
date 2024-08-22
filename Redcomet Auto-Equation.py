import pyautogui as pyag
import keyboard as key
import time as t
import pyperclip

print('press f4 for manual (f10 to exit),')
print('press f8 for auto   (f9 to exit)')
last_clipboard_content = 0
x = True
y=True

def equate():
    global last_clipboard_content
    #Copy line
    pyag.hotkey('shift','home')
    pyag.hotkey("ctrl", "c")
    clipboard_content=pyperclip.paste()
    if clipboard_content==last_clipboard_content:
        pyag.press("down")
        pyag.press("end")
        return
    symbols = 0
    letters = 0
    for i in range (len(clipboard_content)):
        if clipboard_content[i].isalpha():
            letters+=1
        else: 
            symbols+=1
    print(str(symbols)+","+str(letters))
    if letters>symbols and clipboard_content.find("=")==-1 and clipboard_content.find("~")==-1:
        pyag.press("down")
        pyag.press("down")
        pyag.press("end")
        return

    #Wait to copy
    # t.sleep(0.5)
    #Click equation button
    #pyag.moveTo(equate_button[0],equate_button[1])
    pyag.leftClick()
    #Paste line
    pyag.hotkey("ctrl", "v")
    last_clipboard_content = pyperclip.paste()
    #Save
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("enter")
    #Next Line
    pyag.press("down")
    pyag.press("end")
    x=True



while x:
    #Enable key
    if key.is_pressed('f4'):
        print("Equating...")
        x=False
        equate()

    if key.is_pressed('f8'):
        print("Auto Equating...")
        y=True
        while y:
            if key.is_pressed('f9'):
                y=False
                break
            equate()    

    #Break key
    if key.is_pressed('f10'):
        print("Nooooooo")
        y=False
        break

    #Keeps my pc fan quite
    t.sleep(0.01)

t.sleep(2)