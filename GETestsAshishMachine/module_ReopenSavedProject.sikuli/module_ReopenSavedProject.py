from sikuli import *
import os
import sys
import module_CommonImagesSet

def reopenSavedProject(projectName, version, patternToCompare, ifOpen):
    nameColumn = find(module_CommonImagesSet.columnNameHeader)
    click(nameColumn.getTarget().offset(0,34)) # Click in the filter field.
    module_CommonImagesSet.removePreExistingText()
    type(projectName)
    click(nameColumn.getTarget().offset(0,78)) # Select the project
    wait(4)# Because there is some lag in Production while fetching.
    wait(module_CommonImagesSet.versionNumberColumnHeader, 5)
    versionNumberHeader = find(module_CommonImagesSet.versionNumberColumnHeader)
    try:
        click(versionNumberHeader.getTarget().offset(0,42))
        type(version)
        wait(1)
        if not exists(patternToCompare, 5):
            click(module_CommonImagesSet.cancelButton)
            Debug.log("INFO: Saving is not yet complete")
            return False
        else:
            Debug.log("SUCCESS: Project is successfully Saved.")
            if ifOpen:
                click(versionNumberHeader.getTarget().offset(0,223))
            else:
                # Just check if the thumbnail is visible. This means that project is saved.
                click(module_CommonImagesSet.cancelButton)
            return True
    except:
       Debug.log("ERROR: Something went wrong while saving.")
       Debug.log("ERROR: Test Failed.")
    
#reopenSavedProject()
