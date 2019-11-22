import os
import sys
import module_CommonImagesSet

if exists(module_CommonImagesSet.settingsGearIcon):
    click(module_CommonImagesSet.settingsGearIcon)
else:
    Debug.log("ERROR: Image - Couldn't find. Trying By location.")
    click(Location(1533, 135))
    
exists("tabReferenceDrawings.png")
click(Pattern("projectsTabInAdmin.png").targetOffset(1,0))
exists(Pattern("removeUnderProjectsTab.png").targetOffset(1,0))
click(Pattern("ruleManagementTab.png").targetOffset(1,0))
exists(Pattern("addButtonUnderRulesManagementTab.png").targetOffset(1,0))
click(Pattern("componentLibraryTabInAdmin.png").targetOffset(1,0))
exists(Pattern("addButtonUnderComponentLibTab.png").targetOffset(1,0))
click(Pattern("equipOfInterestTabInAdmin.png").targetOffset(1,0))
exists(Pattern("addButtonUnderEquipOfInterestTab.png").targetOffset(1,0))
click(Pattern("userManagementTabInAdmin.png").targetOffset(1,0))
exists("addButtonUnderUserManagementTab.png")
# close the admin page.
click(module_CommonImagesSet.closeButton)
Debug.log("TEST PASSED!!")





