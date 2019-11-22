# Component Upload and Delete Testing.
import os
import sys
import module_CommonImagesSet

componentName = "AUTOMATION TEST COMPONENT"
uploadDialogRegion = Region(647,219,601,668)
success = True

# Open settings page.
click(module_CommonImagesSet.settingsGearIcon)

# Click on component Library tab.
click(module_CommonImagesSet.componentLibraryTab)

# Click on component add button.
click(module_CommonImagesSet.addButton)

match = uploadDialogRegion.find(Pattern("addComponentDialogTitle.png").targetOffset(1,0))

# Title of the component.
click(match.getTarget().offset(-43,85))
type(componentName)

# Description
click(match.getTarget().offset(-43,150))
type("Automation Test")

# category, subcategory
click(uploadDialogRegion.find(Pattern("categoryDropdown.png").targetOffset(1,0)))
click(uploadDialogRegion.find(Pattern("miscCategory.png").targetOffset(1,0)))
click(uploadDialogRegion.find(Pattern("subCategoryDropdown.png").targetOffset(1,0)))
click(uploadDialogRegion.find(Pattern("subcategoryOthers.png").targetOffset(1,0)))

# Upload a sample component file.
# A. get the sample file path.
commonImagePath = module_CommonImagesSet.mapTypeRoadImage.getFilename()
commonDirectoryPath = os.path.dirname(commonImagePath)
componentDWG = commonDirectoryPath + "\\" + componentName + ".DWG"
Debug.log(componentDWG)
# B. Type the path in File Open Dialog hit enter.
click(module_CommonImagesSet.chooseFileButton)
wait(1)
type(componentDWG + Key.ENTER)

# Click on upload button.
click(uploadDialogRegion.find(module_CommonImagesSet.cancelUploadButton).getTarget().offset(60, 0))
wait(1)

# Wait till the upload is complete.
# Add button once again gets activated once upload is complete.
#wait(module_CommonImagesSet.addButton, 40)

wait(module_CommonImagesSet.addButton, 100)

if not exists(module_CommonImagesSet.addButton):
    Debug.log("ERROR: Component loading either failed or took too much time.")
    success = False
    
else:
    # Check if the model has been added successfully.
    click(Pattern("categoryDropdown.png").targetOffset(1,0))    
    click(Pattern("miscCategory.png").targetOffset(1,0))
    click(Pattern("subCategoryDropdown.png").targetOffset(1,0))
    click(Pattern("subcategoryOthers.png").targetOffset(1,0))
    
    click(find(Pattern("miscAndOthersCombo.png").targetOffset(1,0)).getTarget().offset(200, 0))
    type(componentName)
    
    newComponentThumbnail = Pattern("newComponentThumbnail.png").targetOffset(1,0)
    if not exists (newComponentThumbnail):
        Debug.log("ERROR: Component is not found in the library after upload.")
        success = False
    else:
        Debug.log("INFO: Component is uploaded successfully.")
    
    # Now delete the component to clean the library.
    click(newComponentThumbnail)
    click(module_CommonImagesSet.removeButton)
    
    click(module_CommonImagesSet.cancelAndRemoveButton)
    wait(1)
    # Check if the component has been deleted.
    if exists(newComponentThumbnail):
        Debug.log("ERROR: Component couldn't be removed from library.")
        success = False
    else:
        Debug.log("INFO: Component is removed successfully.")

# close admin page
click(module_CommonImagesSet.closeButton)

if success:
    Debug.log("TEST PASSED!!")
else:
    Debug.log("TEST FAILED!!")


    
