from sikuli import *
import os
import sys
import module_CommonImagesSet

def deleteProject(name):
    projectName = name if name else "Auto Test"
    # Check if project is not closed. In that case first close the project.
    if exists(module_CommonImagesSet.selectViewImage):
        Debug.log("Closing existing Project")
        module_CommonImagesSet.closeProject()
        wait(1)
    if(Region(1033,0,647,274).exists(module_CommonImagesSet.settingsGearIcon)):
        Region(964,0,716,249).click(module_CommonImagesSet.settingsGearIcon)
    else:
        Debug.log("ERROR: Image - Couldn't find. Trying By location.")
        click(Location(1561, 115))

    wait(0.5)
    try:
        click("projectsTab.png")
        nameColumn = find(module_CommonImagesSet.columnNameHeader)
        click(nameColumn.getTarget().offset(0,34)) # Click in the filter field.
        type(projectName)
        click(nameColumn.getTarget().offset(0,78)) # Select the project
        click(Pattern("removeProjectButton.png").targetOffset(1,0))
        click("removeButtonOnDialog.png")
        click(module_CommonImagesSet.closeButton)
    except:
       click(module_CommonImagesSet.closeButton)
    
#deleteProject("vv")
