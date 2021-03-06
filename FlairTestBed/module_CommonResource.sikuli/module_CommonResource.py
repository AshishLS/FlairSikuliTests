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

loginScreenLogo = "LoginScreenLogo.png"
def getloginScreenLogo(): 
    return Pattern(loginScreenLogo).similar(0.90).targetOffset(0,1)

modelsAreReadyMessage = "modelsAreReadyMessage.png"
def getModelsAreReadyMessage(): 
    return Pattern(modelsAreReadyMessage).similar(0.90).targetOffset(0,1)

region_leftPanel = Region(0,69,383,940)
region_centerOfForgeViewer = Region(692,211,898,797)

def removePreExistingText():
    keyDown(Key.CTRL)
    keyDown("a")
    keyUp("a")
    keyUp(Key.CTRL)
    keyDown(Key.DELETE)
    wait(0.5)

def selectDevOrProd():
    link = "https://dev-app.flair3d.com" # Default dev
    # Get input from user whether to check on production or dev
    items = ("dev", "prod")
    selected = select("Please select environment to run the test on", options = items)
    if selected == items[1]:
        link = "https://app.flair3d.com"
    return link

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
    # rightClick(getChromeLeftCorner().targetOffset(350,-15))
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
    
def logoutFromExistingAccount():
    click(getFlairWindowControls().targetOffset(20,0))
    wait(0.5)
    click(getFlairWindowControls().targetOffset(0,130))
    wait(0.5)
    if exists(Pattern("SignOutMessageBox.png"), 2):
        click(Pattern("SignOutMessageBox.png").targetOffset(-50,65))
    wait(2)
def openFlair3DAndLogin(link):
    username = "ashish.shete85@gmail.com"
    pwd = "winCCTECH@85"
    openFlair3DAndLoginForGivenUser(link, username, pwd)
    
def openFlair3DAndLoginForGivenUser(link, username, pwd):
    wait(0.5)
    # Open flair3D and login
    wait(0.5)
    paste(link)
    wait(1)
    type(Key.ENTER)
    if exists(getFlair3DLogoInTheApp(), 3):
        logoutFromExistingAccount()
    assert exists("FlairLoginScreen.png", 10), "ERROR: Login screen is not visible"
    click(Pattern("FlairLoginScreen.png").targetOffset(-150,50))
    wait(0.5)
    removePreExistingText()
    
    type(username)
    type(Key.TAB)
    type(pwd)
    click(Pattern("FlairLoginScreen.png").targetOffset(-10,190))
    Debug.log("INFO: Successfully logged in")
    assert exists(getFlair3DLogoInTheApp(), 8)
    wait(2)

def openFlair3DCreateNewUserAccount(link, username, pwd):
    wait(0.5)
    # Open flair3D and login
    wait(0.5)
    paste(link)
    wait(1)
    type(Key.ENTER)
    if exists(getFlair3DLogoInTheApp(), 3):
        logoutFromExistingAccount()
    assert exists("FlairLoginScreen.png", 4), "ERROR: Login screen is not visible"
    print "LOG: We want a new user account, so click on SignUp"
    click(Pattern("FlairLoginScreen.png").targetOffset(60,225))
    print "LOG: Click on the Email Field"
    wait(1)
    click(Pattern("NewSignUpScreen.png").targetOffset(-140,50))
    removePreExistingText()
    
    type(username)
    type(Key.TAB)
    type(pwd)
    print "LOG: Click on Sign up button"
    click(getloginScreenLogo().targetOffset(0,440))
    assert exists("VerificationEmailSentMessage.png",2), "ERROR: Verification email sent message doesn't see to have appeared."
    wait(2)
    
def searchProjectByName(projectName):
    print "LOG: Searching for project: %s " % projectName
    click(getFlair3DLogoInTheApp()) # Make sure you are at home page
    wait(0.5)
    click(getFlair3DLogoInTheApp().targetOffset(300,75))
    wait(2) # wait for projects to load
    
    click(getFlair3DLogoInTheApp().targetOffset(300,75)) # Click on the search bar
    type(projectName)
    wait(0.5)

def searchForProjectAndOpen(projectName):
    searchProjectByName(projectName)
    print "LOG: Opening project: %s " % projectName
    click(getFlair3DLogoInTheApp().targetOffset(865,320)) # Click on the projectTile
    print "INFO: Going inside the project."
    # Check if we are inside the project description
    #if exists("ProjectView.png""CheckBoxesInsideProjectView.png", 4), "ERROR: Project View seems different"
    if exists("CheckBoxesInsideProjectView.png", 4):
        print "INFO: Project view success."
        return 1
    else:
        print "INFO: No project found of the name %s", projectName
        return 0

def selectAllAndOpenProject():
    print "LOG: Click on Select All Checkbox - common_module"
    click(getFlair3DLogoInTheApp().targetOffset(280,338)) # Click on Select All Checkbox
    print "LOG: Click on a file to open the project - common_module"
    click(getFlair3DLogoInTheApp().targetOffset(515,390)) # Click on a file to open the project
    print "LOG: Wait for the AEC data load completion - common_module"
    wait("modelsAreReadyMessage.png", 30) # wait for the AEC data load completion
    print "LOG: Click on close of AEC load completion notification - common_module"
    click(Pattern("modelsAreReadyMessage.png").targetOffset(90,0))
    Debug.log("INFO: Models should be ready for search now.")

def clickOnViewHome():
    print "LOG: Click on the forge view button - common_module"
    click(Pattern("FlairWindowControls.png").targetOffset(-65,65)) 
    wait(0.5) # Wait a moment for it to settle.
def closeThePopupMessages():
    wait(0.5)
    print "LOG: Click on the forge view button - common_module"
    click(Pattern("FlairWindowControls.png").targetOffset(60,60)) # Click on the forge view button
    wait(0.5)
