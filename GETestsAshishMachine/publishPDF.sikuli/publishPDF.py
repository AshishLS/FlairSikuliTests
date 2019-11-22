import os
import sys
import module_CreateProject
import module_DeleteProject
import module_CreatePolygonInTexas
import module_CommonImagesSet
import module_PublishDrawing

nameOfProject = "Test Publish PDF"
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
    module_DeleteProject.deleteProject(nameOfProject);
    

# Test translation.

click(module_CommonImagesSet.imgTransformIcon)
click(module_CommonImagesSet.imgTranslateObjectIcon)

turbinePattern = Pattern("turrbineImage.png").similar(0.35).targetOffset(2,10)
turbinePatternMatch = find(turbinePattern)
click(turbinePatternMatch.getTarget())
hover(module_CommonImagesSet.selectViewImage)
dropTargetLocationMatch = find(module_CommonImagesSet.dropLocationAboveCamera)
dragDrop(turbinePatternMatch.getTarget().offset(10,-10), dropTargetLocationMatch.getTarget().offset(0,-142))

module_CommonImagesSet.fitToView()

# Test Rotate.
wait(1)
# First time unselect.
click(module_CommonImagesSet.imgTransformIcon.targetOffset(0,0))
# Second time select.
click(module_CommonImagesSet.imgTransformIcon)
# Click on the rotate tool.
click(module_CommonImagesSet.imgRotateObjectIcon)

# Select the component again by clicking on the drop location.
click(dropTargetLocationMatch.getTarget().offset(0,-135))

# If I use same pattern with offset, it won't work because pattern finding for the drop location provides it some delay.
#dragDrop(module_CommonImagesSet.propertiesButton.targetOffset(-85,-142), module_CommonImagesSet.layersButton.targetOffset(0,-265))
dragDrop(Pattern("rotateHandleBall.png").targetOffset(1,0), module_CommonImagesSet.layersButton.targetOffset(-125,-275))
hover(module_CommonImagesSet.selectViewImage)
if not exists(Pattern("rotatedTMToTestSuccess.png").similar(0.39)):
    Debug.log("Something went wrong with rotation")
    Debug.log("TEST FAILED!!")
    module_DeleteProject.deleteProject(nameOfProject)
    exit()
# Exit transform mode and proceed for publish.
hover(module_CommonImagesSet.selectViewImage)

click(module_CommonImagesSet.imgTransformIcon.targetOffset(0,0))

# Light Save the project.
module_CommonImagesSet.clickOnLightSave()

# Publish the drawing.
module_PublishDrawing.publishDrawing()

# close the project.
module_CommonImagesSet.closeProject()
wait(1)

# Delete the test project.
#module_DeleteProject.deleteProject(nameOfProject)

Debug.log("TEST PASSED!!")





























