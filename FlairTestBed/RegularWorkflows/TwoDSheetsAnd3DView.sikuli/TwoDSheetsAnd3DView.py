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

def check2DViewsAreOkay():
    
    assert exists("AdminBuildingFullView.png"), "ERROR: looks Like Model is not loaded correctly"
    print ("LOG: Click on the show 2D view slider button")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-65,135))
    print ("LOG: Check if the first sheet looks okay.")
    assert exists("FirstSheetBottom.png"), "ERROR: 1st sheet doesn't look okay"
    print ("LOG: 2D Sheets should show up in the left panel")
    assert module_CommonResource.region_leftPanel.exists("SheetList.png"), "ERROR: 2D sheets list not visible"

    rdoButton1st2DsheetLocation = Location(-40,310) # Offset from the FlairLogo
    print ("LOG: Check if the 2nd Sheet of 1st Model (ARCH) is okay")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(rdoButton1st2DsheetLocation.getX(),rdoButton1st2DsheetLocation.getY()+45))
    assert exists("FourtSheetRightTop.png", 5), "ERROR: 2nd sheet of 1st Model (ARCH) doesn't look okay"

    print ("LOG: Check if the 1st sheet in second model (STR) is okay. Click on the expand button")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(230,450))
    print ("LOG: click on the 000- Cover sheet of STR model")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-40,400))
    assert exists("FirstSheetBottom.png"), "ERROR: 2nd sheet of 2nd Model (STR) doesn't look okay"

    Debug.log("INFO: Looks like 2D Sheets are fine.")

check2DViewsAreOkay()
if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")