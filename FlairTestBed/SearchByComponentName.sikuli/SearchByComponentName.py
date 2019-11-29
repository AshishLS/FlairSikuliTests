import os
import sys
import module_CommonResource

ifLogin = 0
ifCloseChrome = 0

if(ifLogin):
    module_CommonResource.openChrome()
    module_CommonResource.openFlair3DAndLogin()

# After signing in
module_CommonResource.searchForProjectAndOpen("pilot Project")
module_CommonResource.selectAllAndOpenProject()
module_CommonResource.clickOnViewHome()

def checkSearchByComponentName():
    assert exists("FullAirportTerminalLoaded.png"), "ERROR: looks Like Model is not loaded correctly"
    print "INFO: Model is loaded correctly. Switching to Search tab"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(175,55)) # Click on search tab

    assert module_CommonResource.region_leftPanel.exists("SearchByMissing.png", 2), "ERROR: Search By field seems missing."
    print "LOG: Select Search by Component Name"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,200)) # Click on Component Name Radio button
    
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(0,255)) # Click in the search tex box
    print "LOG: Clicked inside the Search Textbox"

    type("Gate counter - 2") 
    
    print "LOG: Clicking the Search button"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-10,335)) # Click on Fit To view checkBox

    print "LOG: Check whether any result appears"
    assert module_CommonResource.region_leftPanel.exists("SearchResults.png", 10), "ERROR: No or incorrect serach result appeared"
    print "LOG: Check the Fit To View checkbox"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(135,425)) # Click on Fit To view checkBox
    
    print "LOG: Click on the first result"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(40,620))

    assert exists("1574349626978.png", 2), "ERROR: Incorrect Search result or Fit To View didn't work"
    
    print "INFO: Search By Component Name worked fine. Exiting Test."

checkSearchByComponentName()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")