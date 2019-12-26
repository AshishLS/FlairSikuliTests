import os
import sys
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
    print ("LOG: Click on the show 2D view radio button")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(-65,135))
    print ("LOG: Check if the first sheet looks okay.")
    assert exists("FirstSheetBottom.png"), "ERROR: 1st sheet doesn't look okay"
    print ("LOG: 2D Sheets should show up in the left panel")
    assert module_CommonResource.region_leftPanel.exists("SheetList.png"), "ERROR: 2D sheets list not visible"

    rdoButton1st2DsheetLocation = Location(-65,265) # Offset from the FlairLogo
    print ("LOG: Hovering over the first sheet name should display tooltip of Arc model name")
    module_CommonResource.region_leftPanel.hover(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(rdoButton1st2DsheetLocation.getX(),rdoButton1st2DsheetLocation.getY()))
    assert module_CommonResource.region_leftPanel.exists("ModelNameOnHover.png"), "ERROR: Tooltip not visible when hovered over the sheet name"
    
    print ("LOG: Check if the 4th Sheet is okay")
    module_CommonResource.region_leftPanel.click(module_CommonResource.getFlair3DLogoInTheApp().targetOffset(rdoButton1st2DsheetLocation.getX(),rdoButton1st2DsheetLocation.getY()+125))
    assert exists("FourtSheetRightTop.png", 5), "ERROR: 1st sheet doesn't look okay"

    Debug.log("INFO: Looks like 2D Sheets are fine.")

check2DViewsAreOkay()
if(ifCloseChrome):
    module_CommonResource.closeChrome()
Debug.log("TEST PASSED!!")