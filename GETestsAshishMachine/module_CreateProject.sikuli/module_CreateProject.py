from sikuli import *
import os
import sys
import module_CommonImagesSet

def _commonStepsForCeateProject(name):
    projectName = name if name else "Auto Test"
    downloadBar =  Pattern("showAllButtonInDownload.png").targetOffset(44,2)
    if exists(downloadBar):
        click(downloadBar)

    click("newProjectButton.png")
    wait(Pattern("createNewProjectDialogPortion.png").similar(0.59), 5)
    click(Pattern("EnterProjectName.png").targetOffset(-2,14))
    type(projectName)
    click("createNewProjectLabel.png")
    click(Pattern("ProjectDescription.png").targetOffset(-47,13))
    type("Testing By CCTECH Automation")

    module_CommonImagesSet.dialogRegion.click("enterNumberOfTMsField.png")
    type("2")
    module_CommonImagesSet.dialogRegion.click("enterSFDCCodeField.png")
    type("0101011")
    module_CommonImagesSet.dialogRegion.click(Pattern("InstallationCountry.png").targetOffset(-58,21))
    module_CommonImagesSet. dialogRegion.click(Pattern("SearchLens.png").targetOffset(-29,1))
    type("India")

    if(module_CommonImagesSet.dialogRegion.exists("indiaInTheCountryListDropdown.png")):
        module_CommonImagesSet.dialogRegion.click("indiaInTheCountryListDropdown.png")
    else:
        Debug.log("ERROR: Image - Couldn't find. Trying By location.")
        click(Location(775, 738))
    
    module_CommonImagesSet.dialogRegion.click(Pattern("fullTemplateThumbnail.png").similar(0.59))
def _scrollToBottomOfDialog():
    # Sometimes if the templates are more, we need to scroll down for the 
    # create project button.
    if not module_CommonImagesSet.dialogRegion.exists(module_CommonImagesSet.createButton):
        scrolldown = find("ScrollDownButton.png")
        hover(scrolldown)
        mouseDown(Button.LEFT)
        wait(3)
        mouseUp(Button.LEFT)    
    
def createProject(name):
    _commonStepsForCeateProject(name)            
    _scrollToBottomOfDialog()
    module_CommonImagesSet.dialogRegion.click(module_CommonImagesSet.createButton)

def createProjectForPDFWorkflow(name):
    _commonStepsForCeateProject(name)
    _scrollToBottomOfDialog()
    # click on checkbox for PDF Reference drawing.
    match = find(Pattern("PdfRefernceCheckBoxOnCreateProjectDialog.png").similar(0.82).targetOffset(1,0))
    click(match.getTarget().offset(-64,0))
    module_CommonImagesSet.dialogRegion.click(module_CommonImagesSet.createButton)
    
    
#createProject()