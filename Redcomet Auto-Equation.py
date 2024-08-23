import pyautogui as pyag
import keyboard as key
import time as t
import pyperclip
import os

print('press f4 for manual (f1 to exit),')
print('press f8 for auto   (f2 to exit)')
last_clipboard_content = 0
y=False

def equate():
    global last_clipboard_content
    #Copy line
    pyag.hotkey('shift','home')
    pyag.hotkey("ctrl", "x")
    #Checks if line copied is the same as the line copied before if so skips to the next line
    clipboard_content=pyperclip.paste()
    if clipboard_content==last_clipboard_content:
        pyag.hotkey("ctrl", "v")
        pyperclip.copy("")
        pyag.press("down")
        pyag.press("end")
        # pyag.hotkey("ctrl", "c")  # Copy the new line
        # last_clipboard_content = pyperclip.paste()
        return
    #Checks if the line copied is a line of text or an equation using predetermined rules
    symbols = 0
    letters = 0
    for i in range (len(clipboard_content)):
        if clipboard_content[i].isalpha():
            letters+=1
        else: 
            symbols+=1
    if letters>symbols and clipboard_content.find("=")==-1 and clipboard_content.find("~")==-1 and clipboard_content!=last_clipboard_content:
        pyag.hotkey("ctrl", "v")
        last_clipboard_content = pyperclip.paste()
        pyperclip.copy("")
        pyag.press("down")
        pyag.press("end")
        return
    
    #Clicks The Equation button the mouse is hovering over
    pyag.leftClick()
    #Pastes line
    pyag.hotkey("ctrl", "v")
    last_clipboard_content = pyperclip.paste()
    #Saves pasted line as equation
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("tab")
    pyag.press("enter")
    #Skip To Next Line
    pyag.press("down")
    pyag.press("end")
    #Replaces clipboard with a blank space
    pyperclip.copy("")

def stop_auto_equating():
    global y
    y = False

def stop_program():
    global running
    running = False
    print('Bye')
    os._exit(0)


key.add_hotkey('f2', stop_auto_equating)
key.add_hotkey('f1', stop_program)

while True:
    #Manual Enable Key
    if key.is_pressed('f4'):
        print("Equating...")
        # x=False
        equate()
        if key.is_pressed('f2'):
            y = False
            break

    #Automatic Enable Key
    if key.is_pressed('f8'):
        print("Auto Equating...")
        y=True
        while y:
            equate()
            t.sleep(0.01)

    #Keeps my pc fan quiet
    t.sleep(0.01)

t.sleep(2)
