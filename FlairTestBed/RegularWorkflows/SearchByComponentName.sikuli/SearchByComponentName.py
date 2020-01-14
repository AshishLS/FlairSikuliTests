import os
import sys
sys.path.append(os.path.abspath('../FlairTestBed/'))
import module_CommonResource

ifLogin = 0
ifCloseChrome = 0
projectName = "Admin Building For Auto Testing"

if(ifLogin):
    module_CommonResource.openChrome()
    module_CommonResource.openFlair3DAndLogin()

# After signing in
module_CommonResource.searchForProjectAndOpen(projectName)
module_CommonResource.selectAllAndOpenProject()
module_CommonResource.clickOnViewHome()

def checkSearchByComponentName():
    assert exists("AdminBuildingFullView.png"), "ERROR: looks Like Model is not loaded correctly"
    print "INFO: Model is loaded correctly. Switching to Search tab"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(175,55)) # Click on search tab

    assert module_CommonResource.region_leftPanel.exists("SearchByMissing.png", 2), "ERROR: Search By field seems missing."
    print "LOG: Select Search by Component Name"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,200)) # Click on Component Name Radio button
    
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(0,255)) # Click in the search tex box
    print "LOG: Clicked inside the Search Textbox"

    type("Basic Roof") 
    
    print "LOG: Clicking the Search button"
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-10,335)) # Click on Fit To view checkBox

    print "LOG: Check whether any result appears"
    assert module_CommonResource.region_leftPanel.exists("BasicRoofSearchResult.png", 10), "ERROR: No or incorrect serach result appeared"
    print "LOG: Check the Fit To View checkbox"
    if module_CommonResource.region_leftPanel.exists(Pattern("FitToViewCheckBox.png").similar(0.90)):
        click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(135,425)) # Click on Fit To view checkBox
    
    print "LOG: Click on the second result - Basic Roof [615290]"
    click(Pattern("BasicRoofSearchResult.png").targetOffset(-30,35))

    assert exists("BasicRoofSearchObjectFit.png", 2), "ERROR: Incorrect Search result or Fit To View didn't work"
    
    print "INFO: Search By Component Name worked fine. Exiting Test."

checkSearchByComponentName()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")