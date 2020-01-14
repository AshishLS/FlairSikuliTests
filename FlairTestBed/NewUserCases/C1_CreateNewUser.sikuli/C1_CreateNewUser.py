# Create new given user
import os
import sys
sys.path.append(os.path.abspath('../FlairTestBed/'))
print "importing module from %s" % os.path.abspath('../FlairTestBed/module_CommonResource.sikuli')
import module_CommonResource
ifLogin = 1
ifCloseChrome = 0

if(ifLogin):
    link = module_CommonResource.selectDevOrProd()
    module_CommonResource.openChrome()

def createGivenUserAccount(username, password):
    print "LOG: Creating a new account with username: %s " % username
    module_CommonResource.openFlair3DCreateNewUserAccount(link, username, pwd)

    print "LOG: Go to the gmail account with username:%s and verify the link." % username
    answer = popAsk("Have you verified the email address?")
    if not answer:
        exit(1)
    print "LOG: Now Check if the new login is successful."
    module_CommonResource.openChrome()
    module_CommonResource.openFlair3DAndLoginForGivenUser(link, username, pwd)

    print "LOG: Once in, check if there is a default project and it actually works."
    defaultProjectName = "Industrial building"
    module_CommonResource.searchForProjectAndOpen(defaultProjectName)
    module_CommonResource.selectAllAndOpenProject()
    module_CommonResource.clickOnViewHome()
    assert exists("InsideDefaultProject.png"), "ERROR: looks Like Model is not loaded correctly"
    
username = "ashish.shete108@gmail.com"
pwd = "winCCTECH@85"
createGivenUserAccount(username, pwd)
Debug.log("TEST PASSED!!")

