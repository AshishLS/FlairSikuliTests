import os
import sys
import module_DeleteProject
import module_CreateProject
import module_CreatePolygonInTexas
import module_CommonImagesSet

nameOfProject = "Test Multiple Polygons"
# First delete existing project if any.
module_DeleteProject.deleteProject(nameOfProject)
# Create new project.
module_CreateProject.createProject(nameOfProject)

# Create first polygon somewhere in Texas.
module_CreatePolygonInTexas.createPolygonInTexas()

type(Key.ESC + Key.ESC)

# Check the properties.
click(Pattern("mapPropertiesAccordion.png").similar(0.81).targetOffset(-123,-1))
wait(1)

valueInSquareMeterDropdown = Pattern("valueInSquareMeterDropdown.png").targetOffset(36,1)
exists(valueInSquareMeterDropdown)


# check meter feet works or not.
click(valueInSquareMeterDropdown)
click(Pattern("sqFtInDropDown.png").targetOffset(1,0))
exists("valueSqFtButton.png")

# check location.
exists(Pattern("polygonsAndLocation.png").targetOffset(1,0))

# Draw second polygon.

click("polygonInMapToolbar.png")
click("corner1.png")
click("corner2.png")
click("corner3.png")
click("corner4.png")
click("corner5.png")

wait(1)
type(Key.ESC)
exists(Pattern("twoInstancesUnderPolygons.png").similar(0.88).targetOffset(1,0))

# close the project.
module_CommonImagesSet.closeProject()
wait(1)

# Delete the project.
module_DeleteProject.deleteProject(nameOfProject)

Debug.log("TEST PASSED!!")