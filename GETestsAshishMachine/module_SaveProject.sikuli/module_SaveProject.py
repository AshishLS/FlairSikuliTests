from sikuli import *
import os
import sys
import module_CommonImagesSet

def saveProject(title, description):
    
    saveTitle = title if title else "Default Title"
    saveDescription = description if description else "Default Description"
    if Region(1033,0,647,274).exists(module_CommonImagesSet.saveButton):
        # Also click on light save.
        module_CommonImagesSet.clickOnLightSave()
        wait(1)
        module_CommonImagesSet.clickOnSaveAsVersion()
    else:
        Debug.log("ERROR: Save Project Image - Couldn't find. Trying By location.")
        exit()

    wait(0.5)
    commitChangesLabel = find(Pattern("commitChangesLabel.png").targetOffset(1,0))
    try:
        click(commitChangesLabel.getTarget().offset(0,77))
        type(saveTitle)
        click(commitChangesLabel.getTarget().offset(0,162))
        type(saveDescription)
        click(module_CommonImagesSet.saveButtonOnDialog)
        # Wait till save is done. The save button should get activated again.
        wait(module_CommonImagesSet.saveButton, 180)
        if not exists(module_CommonImagesSet.saveButton):
            Debug.log("ERROR: After 3 minutes, save hasn't completed.")
            Debug.log("ERROR: Save Failed.")
            exit()            
    except:
       Debug.log("ERROR: Something went wrong while saving.")
       Debug.log("ERROR: Save Failed.")
    
#saveProject()
