# Delete the given user
import os
import sys
sys.path.append(os.path.abspath('../FlairTestBed/'))
print "importing module from %s" % os.path.abspath('../FlairTestBed/module_CommonResource.sikuli')
import module_CommonResource
ifLogin = 0
ifCloseChrome = 0

if(ifLogin):
    link = module_CommonResource.selectDevOrProd()
    module_CommonResource.openChrome()

def deleteGivenUser(username, password):
    if(ifLogin):
        module_CommonResource.openFlair3DAndLoginForGivenUser(link, username, pwd)
    print "LOG: Find and delete the user. Click on the User Management icon"
    click(module_CommonResource.getFlairWindowControls().targetOffset(-75, 0))
    wait(2)
    print "LOG: Searching for the user: ", username
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(940, 70))
    type(username)
    print "LOG: Select the result checkbox"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(270, 140))
    print "LOG: Click on the delete button"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(1310, 70))
    print "LOG: Delete user confirmation dialog should appear"
    assert exists("DeleteUserComfirmationMessage.png",2), "ERROR: Delete user confirmation dialog missing"
    print "LOG: Click on delete in the dialog box"
    click(Pattern("DeleteUserComfirmationMessage.png").targetOffset(145,85))
    module_CommonResource.logoutFromExistingAccount()
    
username = "ashish.shete108@gmail.com"
pwd = "winCCTECH@85"
deleteGivenUser(username, pwd)
Debug.log("TEST PASSED!!")

