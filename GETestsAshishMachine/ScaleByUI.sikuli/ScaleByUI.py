import os
import sys
import module_CreateProject
import module_DeleteProject
import module_CreatePolygonInTexas
import module_CommonImagesSet
import module_PublishDrawing

nameOfProject = "Test Scale By UI"
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
    module_DeleteProject.deleteProject(nameOfProject)
# Test SACLING BY UI.

# First move three road blocks to North.
truckLocation = find(module_CommonImagesSet.unloadingTruckImg)
keyDown(Key.CTRL)
click(truckLocation.getTarget().offset(-425,26)) #left road arc
click(truckLocation.getTarget().offset(0,-26)) #road above
click(truckLocation.getTarget().offset(367,31)) #right road arc
keyUp(Key.CTRL)

transformPartitionLocation = find(module_CommonImagesSet.transformPartition)
click(transformPartitionLocation.getTarget().offset(0,0)) #open the transforms.
wait(1)
click(transformPartitionLocation.getTarget().offset(-22,82)) #transform by edit

module_CommonImagesSet.removePreExistingText()
type("20.5") # moving by 15.5 meters to north
click(transformPartitionLocation.getTarget().offset(33,132)) #NORTH BUTTON

click(truckLocation.offset(0,-50)) # Blank Space on canvas.
type(Key.ESC)

# Now scale with UI
gsutImg = Pattern("gsutImg.png").targetOffset(1,0)
keyDown(Key.CTRL)
click(gsutImg.targetOffset(-78,0)) # select left road.
click(gsutImg.targetOffset(749,0)) # select right road.
keyUp(Key.CTRL)

click(module_CommonImagesSet.scaleByDistance.targetOffset(-13,80))# Click on the Scale by distance vertical.
module_CommonImagesSet.removePreExistingText()
type("20.5") # scaling by 15.5 meters to north
click(module_CommonImagesSet.applyScaleButton.targetOffset(0,0)) # Apply scale button.

# Adjust the scaled blocks by moving up by half the distance.
click(transformPartitionLocation.getTarget().offset(-22,82)) #transform by edit
module_CommonImagesSet.removePreExistingText()
type("20.5 / 2") # moving by 15.5 meters to north
click(transformPartitionLocation.getTarget().offset(33,132)) #NORTH BUTTON

click(truckLocation.getTarget().offset(0,-50)) # Blank Space on canvas.
type(Key.ESC)
click(transformPartitionLocation.getTarget().offset(0,0)) #close the transforms.

module_CommonImagesSet.fitToView()

#validate
if not exists("finalResultImage.png"):
    Debug.log("Something went wrong While Scaling")
    module_DeleteProject.deleteProject(nameOfProject);
    Debug.log("TEST FAILED!!")
    exit()

# Soft Save the project.
module_CommonImagesSet.clickOnLightSave()

# Publish the drawing.
module_PublishDrawing.publishDrawing()

# close the project.
module_CommonImagesSet.closeProject()
wait(1)

# Delete the test project.
# module_DeleteProject.deleteProject(nameOfProject)

Debug.log("TEST PASSED!!")
