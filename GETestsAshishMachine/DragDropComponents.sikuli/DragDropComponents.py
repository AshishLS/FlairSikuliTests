import os
import sys
import module_CreateProject
import module_DeleteProject
import module_CreatePolygonInTexas
import module_CommonImagesSet

nameOfProject = "Test Drag-Drop"

if(1):
    # First delete existing project if any.
    module_DeleteProject.deleteProject(nameOfProject)
    
    # Create new project.
    module_CreateProject.createProject(nameOfProject)
    
    # Create a polygon.
    module_CreatePolygonInTexas.createPolygonInTexas()
    
    # Polygon is done. Go to Forge.
    module_CommonImagesSet.clickOnMapModelSlider()
    wait(5)
    
module_CommonImagesSet.fitToView()

dropTargetLocationMatch = find(module_CommonImagesSet.dropLocationAboveCamera)
dropLocation = dropTargetLocationMatch.getTarget().offset(0,-142)
# Drag drop a TM2500 PULSE ANTI ICING FILTER component
module_CommonImagesSet.dragDropComponentToLocation("TM2500 PULSE ANTI ICING FILTER", module_CommonImagesSet.TM2500_PULSE_ANTI_ICING_FILTER, dropLocation)

module_CommonImagesSet.fitToView()
if not exists(Pattern("draggedTMOnCanvas.png").targetOffset(1,0), 5):
    Debug.log("Drag Failed!!")
    Debug.log("TEST FAILED!!")
    module_DeleteProject.deleteProject(nameOfProject)
    exit()

# Light Save the project.
module_CommonImagesSet.clickOnLightSave()

# close the project.
module_CommonImagesSet.closeProject()
wait(1)

# Delete Project.
# module_DeleteProject.deleteProject(nameOfProject)

Debug.log("TEST PASSED!!")