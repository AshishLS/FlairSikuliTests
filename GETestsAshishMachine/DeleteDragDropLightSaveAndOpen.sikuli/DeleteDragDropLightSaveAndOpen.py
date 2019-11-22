import os
import sys
import module_CreateProject
import module_DeleteProject
import module_CreatePolygonInTexas
import module_CommonImagesSet
import module_PublishDrawing
import module_ReopenSavedProject

nameOfProject = "Test Delete Drag Drop Save And Reopen"
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
    
    #confirm
    if not exists(Pattern("twoTMsSideBySide.png").similar(0.35)):
        Debug.log("Something went wrong in Forge View")
        #module_DeleteProject.deleteProject(nameOfProject)
        
    # First delete a bunch of components stone cold.
    module_CommonImagesSet.selectAbunchOfComponents()
    # Delete the selected components.
    type(Key.DELETE)
    
    # drag drop few components.
    dropTargetLocationMatch = find(module_CommonImagesSet.dropLocationAboveCamera)
    dropLocation = dropTargetLocationMatch.getTarget().offset(0,-142)
    # Drag drop a TM2500 PULSE ANTI ICING FILTER component
    module_CommonImagesSet.dragDropComponentToLocation("TM2500 PULSE ANTI ICING FILTER", module_CommonImagesSet.TM2500_PULSE_ANTI_ICING_FILTER, dropLocation)
    module_CommonImagesSet.dragDropComponentToLocation("TM2500 PULSE ANTI ICING FILTER", module_CommonImagesSet.TM2500_PULSE_ANTI_ICING_FILTER, dropLocation.offset(350, 0))
    module_CommonImagesSet.dragDropComponentToLocation("GENERATOR STEP UP TRANSFORMER WITH FIREWALL", module_CommonImagesSet.GENERATOR_STEP_UP_TRANSFORMER_WITH_FIREWALL, dropLocation.offset(-350, 0))

    # Rotate Whole model, place it at a new location.
    module_CommonImagesSet.rotateAndMoveWholeModel()
    wait(0.5)
    module_CommonImagesSet.dragDropComponentToLocation("DEMIN WATER TREATMENT SKID", module_CommonImagesSet.DEMIN_WATER_TREATMENT_SKID, dropLocation.offset(-500, -200))
    module_CommonImagesSet.fitToView()
    
    # Light Save the project.
    module_CommonImagesSet.clickOnLightSave()
    
    # close the project.
    module_CommonImagesSet.closeProject()
    wait(1)
    success = True
afterReloadModel = Pattern("afterReopenMovedScene.png").targetOffset(1,0)
saveThumbnail = Pattern("saveThumbnail.png").targetOffset(1,0)
saveComplete = module_ReopenSavedProject.reopenSavedProject(nameOfProject, "v1.1", saveThumbnail, True);
if saveComplete:
    Debug.log("INFO: Save is compelete")
    # check the forge view
    if module_CommonImagesSet.waitForForgeActivation():
        module_CommonImagesSet.clickOnMapModelSlider()
        wait(0.5)
        module_CommonImagesSet.fitToView()
        if not exists(afterReloadModel, 5):
            Debug.log("ERROR: Unexpected scene after reopen")
            success = False
    else:
        Debug.log("ERROR: Forge is not active")
        success = False
        
else:
    Debug.log("SAVE FAILED!!")
    success = False

# close the project.
module_CommonImagesSet.closeProject()
wait(1)

# Delete Project.
# module_DeleteProject.deleteProject(nameOfProject)

if success:
    Debug.log("TEST PASSED!!")
else:
    Debug.log("TEST FAILED!!")
