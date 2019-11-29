from sikuli import *
import os
import sys

flairWindowControls = "FlairWindowControls.png"
def getFlairWindowControls(): 
    return Pattern(flairWindowControls).similar(0.90).targetOffset(0,1)
chromeLeftCorner = "chromeLeftCorner.png"

def getChromeLeftCorner(): 
    return Pattern(chromeLeftCorner).similar(0.90).targetOffset(0,1)

incognitoChromeLeftCorner = "incognitoChromeLeftCorner.png"
def getIncognitoChromeLeftCorner(): 
    return Pattern(incognitoChromeLeftCorner).similar(0.90).targetOffset(0,1)

old_flair3DLogoInTheApp = "old_flair3DLogoInTheApp.png"
flair3DLogoInTheApp = "Flair3DLogoInTheApp.png"
def getFlair3DLogoInTheApp(): 
    return Pattern(flair3DLogoInTheApp).similar(0.90).targetOffset(0,1)

region_leftPanel = Region(0,69,383,940)
region_centerOfForgeViewer = Region(692,211,898,797)

def removePreExistingText():
    keyDown(Key.CTRL)
    keyDown("a")
    keyUp("a")
    keyUp(Key.CTRL)
    keyDown(Key.DELETE)
    wait(0.5)

def openChrome():
    # Open Chrome
    keyDown(Key.WIN)
    keyUp(Key.WIN)
    wait(1)
    #type("Chrome")
    type("Chrome --incognito")
    wait(1)
    type(Key.ENTER)
    wait(1)
    # Maximize the window if it's not already
    #rightClick(getChromeLeftCorner().targetOffset(350,-15))
    rightClick(getIncognitoChromeLeftCorner().targetOffset(350,-15))
    wait(0.5)
    #click(getChromeLeftCorner().targetOffset(400,90)) # Click on maximize
    click(getIncognitoChromeLeftCorner().targetOffset(400,90))
    # take cursor back to address bar
    type(Key.ESC)
    click(getIncognitoChromeLeftCorner().targetOffset(400,15))
    wait(1)

def closeChrome():
    wait(0.5)
    keyDown(Key.ALT)
    keyDown(Key.F4)
    keyUp(Key.ALT)
    keyUp(Key.F4)
    
def logoutFromExistingAccont():
    click(getFlairWindowControls().targetOffset(20,0))
    wait(0.5)
    click(getFlairWindowControls().targetOffset(0,130))
    wait(0.5)
    if exists(Pattern("SignOutMessageBox.png"), 2):
        click(Pattern("SignOutMessageBox.png").targetOffset(145,50))
    wait(2)

def openFlair3DAndLogin():
    wait(0.5)        
    # Open flair3D and login
    paste("http://dev-flair.get-tech-solutions.com/")
    wait(1)
    type(Key.ENTER)
    if exists(getFlair3DLogoInTheApp(), 3):
        logoutFromExistingAccont()
    assert exists("FlairLoginScreen.png", 4), "ERROR: Login screen is not visible"
    click(Pattern("FlairLoginScreen.png").targetOffset(-150,50))
    removePreExistingText()
    
    type("ashish.shete85@gmail.com")
    type(Key.TAB)
    type("winCCTECH@85")
    click(Pattern("FlairLoginScreen.png").targetOffset(-10,190))
    Debug.log("INFO: Successfully logged in")
    wait(2)

def searchForProjectAndOpen(projectName):
    click(getFlair3DLogoInTheApp()) # Make sure you are at home page
    wait(0.5)
    click(getFlair3DLogoInTheApp().targetOffset(300,75))
    wait(2) # wait for projects to load
    
    click(getFlair3DLogoInTheApp().targetOffset(300,75)) # Click on the search bar
    type(projectName)
    wait(0.5)
    
    click(getFlair3DLogoInTheApp().targetOffset(865,320)) # Click on the projectTile
    print "INFO: 33."
    assert exists(Pattern("projectView.png").targetOffset(1,0), 2) # Check if we are inside the project description
    print "INFO: Project view success."

def selectAllAndOpenProject():
    click(Pattern("Flair3DLogoInTheApp.png").targetOffset(280,315)) # Click on Select All Checkbox
    click(Pattern("Flair3DLogoInTheApp.png").targetOffset(425,370)) # Click on a file to open the project
    wait("ModelsAreReadyMsg.png", 30) # wait for the AEC data load completion
    click(Pattern("ModelsAreReadyMsg.png").targetOffset(145,0), 30)
    Debug.log("INFO: Models should be ready for search now.")

def clickOnViewHome():
    click(Pattern("FlairWindowControls.png").targetOffset(-35,55)) # Click on the forge view button
    wait(0.5) # Wait a moment for it to settle.
def closeThePopupMessages():
    wait(0.5)
    click(Pattern("FlairWindowControls.png").targetOffset(60,60)) # Click on the forge view button
    wait(0.5)