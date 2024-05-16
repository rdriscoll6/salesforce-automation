import pyautogui as pyag
import keyboard
import time

prospectClientName = 'The Tube on Lincoln LLC'
branchNum = '052'
paychexReps = ['Luchel Sylvain','Courtney Coblentz','Jeremy Scarson']
contactName = 'Alex Craig'
icAssigned = False
clientType = 'HTML5'
additionalClientType = 'Non-CPA'
accountingSoftware = 'Quickbooks - Online'
anticipateRunDate = '5/15/2024'
timeZone = 'Eastern'
followUpDate = '5/22/2024' #will have to update a week from when case has been submitted
x,y = 2335,418
caseCreator = 'Ryan Driscoll'
coaRec = 'Yes'
message = """DEVONS HOUSE LLC 0039-70135931 is requiring GL setup and their shell is now complete. The run date at this time is 5/15/2024. The client contact that should be used for setup is below.


GL Contact

Name: Devon Escoffery, Phone: N/A, Email: jr@devonshouses.org<mailto:jr@devonshouses.org>



If there are any questions, please reach out to Charles Davis (cdavis12@paychex.com<mailto:cdavis12@paychex.com>) and include them on any updates.



Comments



SMB client requesting GL Services. See below information.



Client Contact First & Last Name: Devon Escoffery

Client Contact Phone Number: 757-291-8685

Client Contact Email: Jr@devonshouses.org<mailto:Jr@devonshouses.org>

Is this a Multi ID or Acquisition?

(If multi ID enter all IDs associated and only fill this in on one client in Insite)



"""



def editCase():
  pyag.moveTo(2551,546) #locate the edit button
  pyag.leftClick() #click edit button

def caseInformation():
  time.sleep(2)
  pyag.moveTo(2352,558) #locate the Prospect-Client Tab
  pyag.leftClick() #click in the search box
  keyboard.write(prospectClientName) #search name
  pyag.moveTo(2556,557)
  pyag.leftClick()
  time.sleep(5) #allows user 5 seconds to select company name from list

  pyag.moveTo(2352,602) #locate Contact Name tab
  pyag.leftClick() #click in the search box
  keyboard.write(contactName) #search name
  pyag.moveTo(2556,597)
  pyag.leftClick()
  time.sleep(5) #allows user 5 seconds to select company name from list

  pyag.moveTo(2358,730) #locate Reassign-Category 1 and select GL Onboarding
  pyag.leftClick()
  keyboard.write('GL Onboarding')
  keyboard.press('Enter')

  pyag.scroll(-2000)

  pyag.moveTo(1989,795) #Assignusing active assignment rules
  pyag.leftClick()

  pyag.moveTo(1989,826) #Send notification email to contact
  pyag.leftClick()

  pyag.moveTo(2547,888) #click save
  pyag.leftClick()

def referenceGL():
  #this function clicks the reference case at the bottom
  pyag.moveTo(2065, 655)
  pyag.scroll(-5000)
  time.sleep(.5)
  pyag.leftClick()
  time.sleep(3)

def referenceGLDetail():
  pyag.moveTo(2351,850)
  pyag.doubleClick()
  pyag.write(branchNum) #Branch
  time.sleep(1)
  pyag.moveRel(0,30)
  pyag.doubleClick()
  keyboard.write(clientType) #Client type
  time.sleep(.5)
  pyag.moveRel(0,60)
  pyag.doubleClick()
  time.sleep(.5)
  keyboard.write(additionalClientType) # Additional Client type
  time.sleep(.5)
  pyag.moveRel(0,55)
  pyag.doubleClick()
  time.sleep(.5)
  keyboard.write(accountingSoftware) # Additional Client type
  time.sleep(.5)
  pyag.moveTo(3250,737)
  pyag.doubleClick()
  keyboard.write(anticipateRunDate) #Update Anticipated Run date *WILL HAVE TO UPDATE

  time.sleep(.5)
  keyboard.press('Enter')
  pyag.moveTo(3341,760)
  pyag.doubleClick()
  keyboard.write(followUpDate) #Update follow up date *WILL HAVE TO UPDATE
  time.sleep(.5)
  keyboard.press('Enter')
  pyag.moveTo(3242,845)
  pyag.doubleClick()
  time.sleep(.5)
  keyboard.write(timeZone) #Update Anticipated Run date *WILL HAVE TO UPDATE
  time.sleep(.5)
  keyboard.press('Enter')

def notes():
  pyag.scroll(-500)
  pyag.moveTo(2348,440)
  pyag.doubleClick()
  keyboard.write(message)
  pyag.moveTo(2838,502)
  time.sleep(.5)
  pyag.leftClick()
  time.sleep(.5)

def contacts():
  savage = 35

  pyag.scroll(-600)
  pyag.moveTo(2335,418)

  for i in paychexReps:
      pyag.doubleClick()
      keyboard.write(i)
      pyag.moveRel(210,0)
      pyag.leftClick()
      #Manually selet the paychex employee
      time.sleep(5)
      pyag.moveTo(x,y+savage)
      time.sleep(1)
      savage += 30

#USE ONLY IF PROJECT MANAGER IS THERE
#pyag.moveTo(3257,705)
#pyag.doubleClick()
#time.sleep(.5)
#keyboard.write(projectManager) #write the project manager
#pyag.moveRel(210,0)
#pyag.leftClick()
#Manually selet the paychex employee
#time.sleep(3)

pyag.moveTo(3257,608)
time.sleep(.5)
pyag.doubleClick()
time.sleep(.5)
keyboard.write(caseCreator)
pyag.moveRel(210,0)
pyag.leftClick()
#Manually selet the paychex employee
time.sleep(5)  

def coaReceived():
  pyag.moveTo(2337,712) #go to COA Recieved
  pyag.doubleClick()
  keyboard.write(coaRec) #currently set to "Yes" may have to adjust
  keyboard.press('Enter')
  pyag.moveTo(2540,517)
  pyag.leftClick() #saves the notes you made so far
  time.sleep(4)

def attachedCOA(): #attaches the COA to the case
  pyag.moveTo(2651,596)
  time.sleep(.4)
  pyag.scroll(-3000)
  pyag.leftClick()
  time.sleep(.5)

  for i in range(1): #adjust the range for how many attachments you need to put
    pyag.moveTo(2039,456)
    pyag.leftClick()
    time.sleep(5) #give time for user to manually select the case and click "open"
    pyag.moveTo(2019,572)
    pyag.leftClick()
    time.sleep(2)
  pyag.moveTo(2008,696)
  pyag.leftClick()
  time.sleep(2)
  
def goToBin():
  pyag.moveTo(2329,258)
  pyag.leftClick()
  time.sleep(.5)
  pyag.moveTo(2417,395)
  pyag.leftClick()
  
editCase()
caseInformation()
time.sleep(5)
referenceGL()
referenceGLDetail()
notes()
time.sleep(3)
contacts()
coaReceived()
attachedCOA()
goToBin()