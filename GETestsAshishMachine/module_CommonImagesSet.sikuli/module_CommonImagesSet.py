from sikuli import *
import os
import sys

mapTypeRoadImage = Pattern("mapTypeRoadImage.png").targetOffset(1,0)
settingsGearIcon = "settingsGearIcon.png"

selectViewImage = Pattern("SelectView.png").targetOffset(1,0)

imgTransformIcon = Pattern("imgTransformIcon.png").targetOffset(12,-13)
imgTranslateObjectIcon = "imgTranslateObjectIcon.png"
imgRotateObjectIcon = "imgRotateObjectIcon.png"
dropLocationAboveCamera =  Pattern("dropLocationAboveCamera.png").similar(0.86).targetOffset(0,1)
rollCameraIcon = Pattern("rollCameraIcon.png").targetOffset(1,0)
propertiesButton = Pattern("propertiesButton.png").targetOffset(1,1)
layersButton = Pattern("layersButton.png").targetOffset(1,0)
closeButton = Pattern("closeButton.png").targetOffset(1,0)
lockButtonToChangeMapView = Pattern("lockButtonToChangeMapView.png").targetOffset(1,0)
placeToClickToChangeMapView = Pattern("placeToClickToChangeMapView.png").targetOffset(1,-1)
createButton = Pattern("CreateButton.png").similar(0.88).targetOffset(1,1)
unloadingTruckImg = Pattern("unloadingTruckImg.png").similar(0.62).targetOffset(1,0)
transformPartition = Pattern("transformPartition.png").targetOffset(1,0)
scaleByDistance = Pattern("scaleByDistance.png").targetOffset(1,0)
applyScaleButton = Pattern("applyScaleButton.png").targetOffset(1,0)
saveButton = Pattern("saveButton.png").targetOffset(1,0)
changLogButton = Pattern("changLogButton.png").targetOffset(1,0)
saveButtonOnDialog = Pattern("saveButtonOnDialog.png").targetOffset(1,0)
columnNameHeader = Pattern("nameColumnHeader.png").targetOffset(1,0)
columnTitleHeader = Pattern("columnTitleHeader.png").targetOffset(1,0)
versionNumberColumnHeader = Pattern("versionNumberColumnHeader.png").targetOffset(1,0)
cancelButton = Pattern("cancelButton.png").targetOffset(1,0)

dialogRegion =  Region(457,0,1011,1080)
cancelOkayButton = Pattern("cancelOkayButton.png").targetOffset(39,0)
mapToolbar = Pattern("mapToolbar.png").targetOffset(1,0)
defualtPushpinOnIndia = Pattern("defaultPushpinOnIndia.png").targetOffset(1,0)
chooseFileButton = Pattern("chooseFileButton.png").targetOffset(1,0)

locationAccordion = Pattern("locationAccordion.png").targetOffset(1,0)

gotoLocationButton = Pattern("gotoLocationButton.png").similar(0.91).targetOffset(1,0)

predixCalibrationRequiredDialog = Pattern("predixCalibrationRequiredDialog.png").targetOffset(1,0)
forgeCalibrateNowDialog = Pattern("forgeCalibrateNowDialog.png").targetOffset(1,0)
componentLibraryTab = Pattern("componentLibraryTab.png").targetOffset(1,0)
refrenceDrawingTab = "refrenceDrawingTab.png"
addButton = Pattern("addButton.png").targetOffset(1,0)
cancelUploadButton = Pattern("cancelUploadButton.png").targetOffset(15,0)
removeButton = Pattern("removeButton.png").targetOffset(1,0)
cancelAndRemoveButton = Pattern("cancelAndRemoveButton.png").targetOffset(1,0)
chromeOkCancelDialog = Pattern("chromeOkCancelDialog.png").targetOffset(1,0)
TM2500_PULSE_ANTI_ICING_FILTER = Pattern("TM2500_PULSE_ANTI_ICING_FILTER.png").targetOffset(1,0)
GENERATOR_STEP_UP_TRANSFORMER_WITH_FIREWALL = Pattern("GENERATOR_STEP_UP_TRANSFORMER_WITH_FIREWALL.png").targetOffset(1,0)
DEMIN_WATER_TREATMENT_SKID = Pattern("DEMIN_WATER_TREATMENT_SKID.png").targetOffset(1,0)
def closeProject():
    click(closeButton)
    wait(0.5)
    match = dialogRegion.wait(cancelOkayButton, 5)
    click(match.getTarget())

def fitToView():
    match = find(dropLocationAboveCamera)
    click(match.getTarget().offset(12,-9))
    wait(1)
    click(match.getTarget().offset(0, -100))

def removePreExistingText():
    keyDown(Key.CTRL)
    keyDown("a")
    keyUp("a")
    keyUp(Key.CTRL)
    keyDown(Key.DELETE)

def waitForForgeActivation():
    if exists("allowKnowYourLocation.png",2):
        click("AllowButton.png")
    # wait for forge to load.
    if not exists(selectViewImage, 50):
        Debug.log("ERROR: FORGE LOADING FAILED!!")
        Debug.log("TEST FAILED!!")
        return False
    return True

def waitForBingMapActivation():
    if exists("allowKnowYourLocation.png",2):
        click("AllowButton.png")
    # wait for forge to load.
    if not exists(mapTypeRoadImage, 30):
        Debug.log("ERROR: BINGMAP LOADING FAILED!!")
        Debug.log("TEST FAILED!!")
        return False
    return True

def clickOnMapModelSlider():
    match = find(placeToClickToChangeMapView)
    click(match.getTarget().offset(0, -48))
    click(match.getTarget().offset(0, -23)) # redundant

def clickOnLightSave():
    match = find(saveButton)
    click(match.getTarget())
    click(match.getTarget().offset(0, 30))

def clickOnSaveAsVersion():
    match = find(saveButton)
    click(match.getTarget())
    click(match.getTarget().offset(0, 50))

def dragDropComponentToLocation(componentName, componentImage, dropLocation):
    componentPartitionImage = Pattern("componentPartitionImage.png").targetOffset(1,0)
    match = find(componentPartitionImage)
    
    click(match.getTarget())
    wait(1)
    click(match.getTarget().offset(250,42))
    # Delete preexisting text and add our own.
    removePreExistingText()    
    # Get a given component and drag drop.
    type(componentName)
    wait(1)
    if not exists(componentImage):
        message = "ERROR: Component %s thumbnail is not visible. Something went wrong." % (componentName)
        Debug.log(message)
        Debug.log("ERROR: TEST FAILED!!!")
        raise Exception(message)
    # Drop on the given location
    dragDrop(match.getTarget().offset(72,195), dropLocation)
    # close the accordian
    click(match.getTarget())
    wait(1)

def selectAbunchOfComponents():
    # Wrench Icon (Transform as reference)
    transformIcon = imgTransformIcon.targetOffset(0,0)
    match = find(transformIcon)
    matchLocation = match.getTarget()
    
    keyDown(Key.CTRL)
    click(matchLocation.offset(-509,-366)) #left TM
    click(matchLocation.offset(-158,-366)) #right TM
    click(matchLocation.offset(-636,-564)) # GSUT
    
    click(matchLocation.offset(-280, -672)) #left Unlocading Truck
    click(matchLocation.offset(-158,-672)) #right Unlocading Truck
    
    click(matchLocation.offset(-176,-510)) # Leftmost Horizontal Tank
    click(matchLocation.offset(-141,-510))
    click(matchLocation.offset(-105,-510))
    click(matchLocation.offset(-68,-510))
    click(matchLocation.offset(-34,-510))
    click(matchLocation.offset(5,-510)) # RightmostHorizontal Tank
    keyUp(Key.CTRL)

def deleteDefaultPushPin(pushpinLocation):
    match = find(mapToolbar)
    click(match.getTarget().offset(47,0))
    wait(1)
    click(pushpinLocation)

def goToLocation(locationString):
    match = find(locationAccordion)
    if not exists("locationAccordianContent.png"):
        click(match.getTarget())
    
    hover(changLogButton)
    click(match.getTarget().offset(67,61))
    # Delete preexisting text and add our own.
    removePreExistingText()
    
    # Open plot somewhere in Texas.
    type(locationString)
    hover(changLogButton)
    rightHandSideRegion = find(changLogButton).left(100).right(500).below(1000)
    rightHandSideRegion.click(gotoLocationButton)

def switchToArialView():
    match = find(mapTypeRoadImage)
    wait(0.5)
    click(match.getTarget())
    wait(0.5)
    click(match.getTarget().offset(-27,153))

def changeTheRollCameraModeToDefault():
    rollCameraLocation = find(rollCameraIcon).getTarget()
    click(rollCameraLocation.offset(12,-12))
    click(rollCameraLocation.offset(0,-100))    

def rotateAndMoveWholeModel():
    # Rotate Whole model, place it at a new location.
    # Unlock map and move model on appropriate position.
    lockButtonPosition = find(lockButtonToChangeMapView)
    click(lockButtonPosition)
    
    cameraLocation = find(dropLocationAboveCamera).getTarget()
    click(cameraLocation)
    wait(0.5)
    click(cameraLocation.offset(0,-50))
    wait(0.5)
    
    referencePosition = find(imgTransformIcon).getTarget()
    # Rotate
    dragDrop(referencePosition.offset(-650, -75) , referencePosition.offset(500, -75))
    
    # Pan
    click(cameraLocation.offset(-100, 0)) # Click on Pan Button.
    wait(0.5)
    dragDrop(referencePosition.offset(-650, -75) , referencePosition.offset(-0, -75))
    
    click(lockButtonPosition)
    wait(0.5)
    
    # Permit to make the positional changes.
    click(chromeOkCancelDialog)

    # Change the roll camera mode back.
    changeTheRollCameraModeToDefault()
    
    