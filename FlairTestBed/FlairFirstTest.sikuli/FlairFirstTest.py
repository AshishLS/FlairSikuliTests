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

def checkLevelsViewIsOkay():
    assert exists("FullAirportTerminalLoaded.png"), "ERROR: looks Like Model is not loaded correctly"
    
    assert module_CommonResource.region_leftPanel.exists("AllAirportTerminalModelNamesInsideProject.png"), "ERROR: Check Left panel model names; something is wrong there."
    
    # Check if all the levels are okay
    
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,140)) # Click On select all models
    assert not exists("AirportTerminalHomeView.png", 1), "ERROR: After unselecting all models, the terminal is still visible."
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,185)) # Click On select Arch models
    assert exists("AirportTerminalOnlyArchModel.png", 2), "ERROR: After selecting only Arch model, something went wrong."
    assert module_CommonResource.region_leftPanel.exists("AllLevelsInAirportTerminalArchModel.png"), "ERROR: Arch model selected, but it problem with all the level count. Check."
    
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,390)) # Click to unselect All levels
    
    assert module_CommonResource.region_centerOfForgeViewer.exists("1574152971881.png"), "ERROR: After unselecting all the levels, something is still visibile"
    # Click on 3rd level and see if we have proper output
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,515)) # Click on 3rd level
    wait(1)
    assert module_CommonResource.region_centerOfForgeViewer.exists("AirportTerminalArchModelOnlyThirdLevel.png"), "ERROR: 3rd Level was selected but not an expected result"
    Debug.log("INFO: Looks like levels are fine.")

checkLevelsViewIsOkay()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")