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

def checkMarkupWorkflow():
    # Markup Creation
    bottomToolBarFirstSection = Pattern("bottomToolBarFirstSection.png").targetOffset(1,0)
    # doubleClick on roof to zoom to it
    doubleClick(Pattern("bottomToolBarFirstSection.png").targetOffset(80,-330))
    click(Pattern("bottomToolBarFirstSection.png").targetOffset(-140,-70)) # click outside to unselect
    click(Pattern("bottomToolBarFirstSection.png").targetOffset(530,0)) # click on markup button
    # Check if the markup window opens up
    assert exists(Pattern("markupViewDialog.png").targetOffset(1,0)), "ERROR: Markup dialog isn't visible."
    # Enable the edit mode.
    click(Pattern("markupViewDialog.png").targetOffset(-85,-85))
    # Select cloud markup
    click(Pattern("markupViewDialog.png").targetOffset(55,-85))
    click(Pattern("markupViewDialog.png").targetOffset(70,-10))
    wait(0.5)
    
    drawLocation = module_CommonResource.getFlair3DLogoInTheApp().targetOffset(775, 725).getTargetOffset()
    dragDrop(drawLocation, Location(drawLocation.getX() + 200, drawLocation.getY() + 100))

    # add a markup name and save
    click(Pattern("markupViewDialog.png").targetOffset(-115,25)) # editable textbox
    assert exists(Pattern("cloudMarkupCorner.png").targetOffset(1,0)), "ERROR: Cloud markup messed while drawing"
    paste("Protruding Beams")
    click(Pattern("markupViewDialog.png").targetOffset(95,25)) # save
    # close the markup saved message
    module_CommonResource.closeThePopupMessages()

    click(Pattern("markupViewDialog.png").targetOffset(130,-130)) # close markup
    wait(0.5)
    # click on forge view home
    module_CommonResource.clickOnViewHome()
    # click on top view
    click(module_CommonResource.getFlairWindowControls().targetOffset(50, 75))
    wait(0.5)

    # new markup a circle perhaps.
    # doubleClick on mid section to zoom to it
    doubleClick(Pattern("bottomToolBarFirstSection.png").targetOffset(275,-460))
    click(Pattern("bottomToolBarFirstSection.png").targetOffset(-140,-70)) # click outside to unselect
    
    click(Pattern("bottomToolBarFirstSection.png").targetOffset(530,0)) # click on markup button
    # Check if the markup window opens up
    assert exists(Pattern("markupViewDialog.png").targetOffset(1,0)), "ERROR: Markup dialog isn't visible."
    # Enable the edit mode.
    click(Pattern("markupViewDialog.png").targetOffset(-85,-85))
    # Select new markup
    click(Pattern("markupViewDialog.png").targetOffset(55,-85))
    # Select circle markup
    click(Pattern("markupViewDialog.png").targetOffset(65,-125))
    wait(0.5)
    
    drawLocation = module_CommonResource.getFlair3DLogoInTheApp().targetOffset(875, 425).getTargetOffset()
    dragDrop(drawLocation, Location(drawLocation.getX() + 200, drawLocation.getY() + 200))

    # add a markup name and save
    click(Pattern("markupViewDialog.png").targetOffset(-115,25)) # editable textbox
    assert exists(Pattern("circleMarkup.png").similar(0.90)), "ERROR: Circle markup messed while drawing"
    paste("Middle Road")
    click(Pattern("markupViewDialog.png").targetOffset(95,25)) # save
    # close the markup saved message
    module_CommonResource.closeThePopupMessages()
    
    click(Pattern("markupViewDialog.png").targetOffset(130,-130)) # close markup
    
    # Check if both the markups are saved properly
    def checkMarkupsAreSavedCorrectly():
        click(Pattern("bottomToolBarFirstSection.png").targetOffset(530,0)) # click on markup button
        assert exists(Pattern("twoMarkupEntries.png").targetOffset(1,0)), "ERROR: Markups are not shown in the UI"
        # click on 1st markup and check if the view shows it appropriately
        click(Pattern("twoMarkupEntries.png").targetOffset(-85,-20)) # select 1st cloud markup
        assert exists(Pattern("cloudMarkupCorner.png").targetOffset(1,0)), "ERROR: Something wrong with the 1st cloud Markup"
        click(Pattern("twoMarkupEntries.png").targetOffset(-85,20)) # select second markup
        assert exists(Pattern("circleMarkup.png").similar(0.90)), "ERROR: Something wrong with the 1st Markup"
    
    checkMarkupsAreSavedCorrectly()
    print ("INFO: Both markups seems correct. In the same session. Let's check for different session.")
    
    # Go to project view and open project again
    click(module_CommonResource.getFlair3DLogoInTheApp())
    wait(0.5)
    type(Key.F5) # Refresh the page
    wait(2)
    module_CommonResource.searchForProjectAndOpen("pilot Project")
    module_CommonResource.selectAllAndOpenProject()
    
    # Now check if the markups are showing up in this session
    checkMarkupsAreSavedCorrectly()
    print ("INFO: Both markups seems correct in this session as well. Let's proceed to delete")
    
    # delete the markups.
    
    click(Pattern("twoMarkupEntries.png").targetOffset(100,-20)) # delete first markup
    click(Pattern("1574252639877.png").targetOffset(145,50)) # confirm delete
    click(Pattern("twoMarkupEntries.png").targetOffset(100,-20)) # delete second markup
    click(Pattern("1574252639877.png").targetOffset(145,50)) # confirm delete
    
    assert not exists (Pattern("twoMarkupEntries.png").similar(0.90).targetOffset(1,0)), "ERROR: Markups are still showing in the UI"

    # Prepare to close.
    click(Pattern("markupViewDialog.png").targetOffset(130,-130)) # close markup
    
checkMarkupWorkflow()

if(ifCloseChrome):
    module_CommonResource.closeChrome()
wait(0.5)
Debug.log("TEST PASSED!!")