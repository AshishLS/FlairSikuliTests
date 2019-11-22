import os
import sys
import module_CommonImagesSet
import module_CreatePolygonInTexas
import module_ReopenSavedProject

#nameOfProject = "Test Delete Drag Drop Save And Reopen"
#saveThumbnail = Pattern("saveThumbnail.png").targetOffset(1,0)
nameOfProject = "Test Delete Drag Drop Save And Reopen"
saveThumbnail = Pattern("saveThumbnail.png").targetOffset(1,0)
times = 0

for step in range(25):
    times += 1 
    saveComplete = module_ReopenSavedProject.reopenSavedProject(nameOfProject, "v1.1", saveThumbnail, True);
    if saveComplete:
        if module_CommonImagesSet.waitForForgeActivation():
            Debug.log("Saving for %dth time", times)
            module_CommonImagesSet.clickOnMapModelSlider()
            module_CommonImagesSet.closeProject()
    else :
        break

Debug.log("Open close happened for %d times", times)