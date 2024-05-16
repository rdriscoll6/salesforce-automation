import pyautogui
import time
import keyboard

graduateDate = "5/15/2024"
graduationTime = "5/15/2024, 11:24 AM"



def updateCase():
  pyautogui.moveTo(2259,446)
  pyautogui.leftClick()
  time.sleep(2)

def writeMessage(message):
  #write message
  pyautogui.scroll(-500)
  pyautogui.moveTo(2581,422)
  pyautogui.doubleClick(button="left")
  pyautogui.moveRel(500,0)
  pyautogui.scroll(-2000)
  pyautogui.moveTo(3060,456)
  pyautogui.leftClick()
  pyautogui.press("enter")
  pyautogui.press("enter")
  pyautogui.write(message)
  pyautogui.moveTo(2843,502)
  pyautogui.leftClick()
  time.sleep(0.5)

  time.sleep(2)
  pyautogui.scroll(-700)

def graduate():
  pyautogui.moveTo(3284,440) # click GL Onboarding Complete
  time.sleep(1)
  pyautogui.doubleClick()
  keyboard.write(graduateDate) #you will need to update graduateDate variable
  pyautogui.moveRel(-500,0)
  time.sleep(.5)
  pyautogui.leftClick()
  time.sleep(1)

  pyautogui.moveTo(3345, 557) #click graduation call complete
  time.sleep(1)
  pyautogui.doubleClick()
  time.sleep(1)
  keyboard.write(graduationTime) #you will need to update graduateDate variable
  pyautogui.moveRel(-500,0)
  pyautogui.leftClick()
  time.sleep(1)

  pyautogui.scroll(2000)
  pyautogui.moveTo(2546, 510) #save changes
  time.sleep(1)
  pyautogui.leftClick()

  time.sleep(1)

def changeStatus():
  time.sleep(1)
  pyautogui.moveTo(2347, 648) #click Case Lookup
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.moveTo(3326,579) #click Status
  time.sleep(1)
  pyautogui.doubleClick()
  pyautogui.leftClick()
  pyautogui.moveTo(3293, 837) #move to solved
  pyautogui.leftClick()

def save():
  pyautogui.moveTo(2558,539) #Go to save button
  pyautogui.leftClick()
  time.sleep(2)
  pyautogui.moveTo(2323,261) #Go to reference GLs
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.moveTo(2423,392) #Go to Go button
  pyautogui.leftClick()

def newEmail():
  if pyautogui.locateOnScreen('newEmail.png',grayscale=True):
      pyautogui.moveTo('newEmail.png')
      pyautogui.leftClick()
  else:
    print('it wasn not there')

  time.sleep(1)

def include():

  pyautogui.moveTo(448,182)
  time.sleep(.5)
  pyautogui.leftClick()
  time.sleep(1)

def graduationEmail():

  pyautogui.locateOnScreen('graduationCallComplete.png')

  pyautogui.moveTo(587,338)
  time.sleep(.5)
  pyautogui.leftClick() #Click Signatures
  time.sleep(1)
  pyautogui.moveTo(681,785) #Click Graduation template
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.leftClick()

def outlook():
  if pyautogui.locateOnScreen('Outlook.png',region=(500,975,200,100),grayscale=True):
      pyautogui.moveTo('Outlook.png')
      pyautogui.leftClick()
      time.sleep(10)
      newEmail()
      include()
      graduationEmail()

  else:
      print('I cannot see it')

for i in range(1):
  time.sleep(1)
  updateCase()
  writeMessage('5/14 - sent client the graduation email. Closing the case')
  graduate()
  changeStatus()
  save()