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
    
    assert module_CommonResource.region_leftPanel.exists("AllModelsInLeftPanel.png"), "ERROR: Check Left panel model names; something is wrong there."
    
    # Check if all the levels are okay
    # Unselect all levels
    
    # Click On select all models - Not available in current deployment.
    #module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-45,140)) 

    # We will unselect each level one by one.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,90))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,115))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,140))

    message = "ERROR: After unselecting all the levels, something is still visibile"
    assert module_CommonResource.region_centerOfForgeViewer.exists("1574152971881.png"), message

    # Expand the levels as well.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-83,90))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-83,303))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-83,510))
    assert not exists("AirportTerminalHomeView.png", 1), "ERROR: After unselecting all models, the terminal is still visible."
    # Click On select Arch models
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,90))
    assert exists("AirportTerminalOnlyArchModel.png", 2), "ERROR: After selecting only Arch model, something went wrong."
    assert module_CommonResource.region_leftPanel.exists("AllLevelsInAirportTerminalArchModel.png"), "ERROR: Arch model selected, but it problem with all the level count. Check."
    # Click On select Arch models to make it all invisible.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,90)) 
    # Click on 3rd level and see if we have proper output
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-36,163)) 
    wait(1)
    assert module_CommonResource.region_centerOfForgeViewer.exists("AirportTerminalArchModelOnlyThirdLevel.png"), "ERROR: 3rd Level was selected but not an expected result"
    # Click on LevelS of MEP model and check if the output is correct.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-36,425))
    message = "ERROR: 3rd Level of Arch and LevelS of MEP were selected but not an expected result"
    assert module_CommonResource.region_centerOfForgeViewer.exists(Pattern("TerminalModelLvl3OfArchAndLvlSofMEP.png").similar(0.80), 2), message
    Debug.log("INFO: Looks like levels are fine.")

checkLevelsViewIsOkay()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")