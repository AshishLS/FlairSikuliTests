import os
import sys
import module_CommonImagesSet
import module_CreatePolygonInTexas
import module_ReopenSavedProject

if(1):
    dropTargetLocationMatch = find(module_CommonImagesSet.dropLocationAboveCamera)
    dropLocation = dropTargetLocationMatch.getTarget().offset(0,-142)
    # Drag drop a TM2500 PULSE ANTI ICING FILTER component
    module_CommonImagesSet.dragDropComponentToLocation("UNLOADING TRUCK", module_CommonImagesSet.TM2500_PULSE_ANTI_ICING_FILTER, dropLocation)