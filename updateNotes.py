import pyautogui
import time
import keyboard

updateDate2 = '5/16/2024'

def updateCase():
  #choosing the case from the bin
  pyautogui.moveTo(2259,446)
  pyautogui.leftClick()
  time.sleep(1)

def writeMessage(message):
  #write message
  pyautogui.scroll(-500)
  pyautogui.moveTo(2581,422)
  pyautogui.doubleClick(button="left")
  pyautogui.moveRel(500,0)
  pyautogui.scroll(-2000)
  pyautogui.moveTo(3060,456)
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.press("enter")
  pyautogui.press("enter")
  pyautogui.write(message)
  pyautogui.moveTo(2843,502)
  pyautogui.leftClick()
  time.sleep(0.5)

def updateDate():
  #updateDate
  pyautogui.scroll(3000)
  pyautogui.moveTo(3261,765)
  pyautogui.doubleClick()
  time.sleep(0.5)
  keyboard.write(updateDate2)
  keyboard.press('Enter')
  time.sleep(0.5)

def saveCase():
  #save the case
  pyautogui.moveTo(2558,529) #Go to save button
  time.sleep(.5)
  pyautogui.leftClick()
  time.sleep(2)
  pyautogui.moveTo(2323,261) #Go to reference GLs
  time.sleep(.5)
  pyautogui.leftClick()
  time.sleep(2)
  pyautogui.moveTo(2423,392) #Go to Go button
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)

def mappingNotes():
  time.sleep(1)
  pyautogui.scroll(-2000)
  #Set Up Status
  pyautogui.moveTo(2514,511)
  pyautogui.doubleClick()
  time.sleep(1)
  pyautogui.leftClick()
  pyautogui.moveRel(0,65) #Move to Mapping COmplete
  time.sleep(1)
  pyautogui.leftClick()
  #mapping Time
  pyautogui.doubleClick()
  time.sleep(1)
  pyautogui.leftClick()
  pyautogui.moveRel(0,45)
  pyautogui.leftClick()



def welcomeCall():
  pyautogui.scroll(-1200)
  pyautogui.moveTo(2454,718)
  pyautogui.doubleClick()
  pyautogui.moveTo(2497,904) #YOU HAVE TO CHANGE DATE
  pyautogui.leftClick()



for i in range (3):
  time.sleep(1)
  updateCase()
  writeMessage('\n 5/14 - Did call with client to answer her questions related to the General Ledger. Showed her how to export COA from QBO. Set up ID:14133950 and sent client ADR. Will meet with her again on 5/16.')
  #welcomeCall()
  updateDate()
  #mappingNotes()
  saveCase()

