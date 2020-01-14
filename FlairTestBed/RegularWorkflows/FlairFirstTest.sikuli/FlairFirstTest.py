import os
import sys
sys.path.append(os.path.abspath('../FlairTestBed/'))
import module_CommonResource

ifLogin = 0
ifCloseChrome = 0
projectName = "Admin Building For Auto Testing"

if(ifLogin):
    link = module_CommonResource.selectDevOrProd()
    module_CommonResource.openChrome()
    module_CommonResource.openFlair3DAndLogin(link)

# After signing in
module_CommonResource.searchForProjectAndOpen(projectName)
module_CommonResource.selectAllAndOpenProject()
module_CommonResource.clickOnViewHome()

def checkLevelsViewIsOkay():
    print("LOG: First Expand the All the models.")
    click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-80, 230))
    
    assert exists("AdminBuildingFullView.png"), "ERROR: looks Like Model is not loaded correctly"
    
    assert module_CommonResource.region_leftPanel.exists("AllModelsInLeftPanel.png"), "ERROR: Check Left panel model names; something is wrong there."
    
    # Click On select all models
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,230))
    message = "ERROR: After unselecting all the levels, something is still visibile"
    assert module_CommonResource.region_centerOfForgeViewer.exists("1574152971881.png"), message
    print("LOG: Make everything visible again")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-60,230))
    
    # We will unselect each level one by one
    cbxLocation = Location(-35,255)  # Offset from the FlairLogo
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()+50))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()+100))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()+150))

    

    # Expand the levels as well.
    expndrLocation = Location(-60,265)  # Offset from the FlairLogo
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(expndrLocation.getX(),expndrLocation.getY()))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(expndrLocation.getX(),expndrLocation.getY()+310))
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(expndrLocation.getX(),expndrLocation.getY()+620))
    assert not exists("AdminBuildingFullView.png", 1), "ERROR: After unselecting all models, the terminal is still visible."
    print "LOG: Click On select Arch model"
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()))
    print cbxLocation
    assert exists("1576082292029.png", 2), "ERROR: After selecting only Arch model, something went wrong."
    assert module_CommonResource.region_leftPanel.exists("AllLevelsInArchModel.png"), "ERROR: Arch model selected, but it problem with all the level count. Check."
    # Click On select Arch models to make it all invisible.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX(),cbxLocation.getY()))
    # Click on 3rd level and see if we have proper output
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX()+25, cbxLocation.getY()+170))
    wait(1)
    assert module_CommonResource.region_centerOfForgeViewer.exists(Pattern("ArchLevel3.png").similar(0.80)), "ERROR: 3rd Level was selected but not an expected result"
    # Click on Level 1 of Structure model and check if the output is correct.
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(cbxLocation.getX()+25,cbxLocation.getY()+435))
    message = "ERROR: 3rd Level of Arch and Level 1 of Structure were selected but not an expected result"
    assert module_CommonResource.region_centerOfForgeViewer.exists(Pattern("1576081933516.png").similar(0.80), 2), message
    Debug.log("INFO: Looks like levels are fine.")

checkLevelsViewIsOkay()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")