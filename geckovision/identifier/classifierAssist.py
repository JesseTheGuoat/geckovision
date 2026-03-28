import cv2 as jordan

from geckovision.identifier import finderTypes


def getClassiferFor(thethingymabop):
    if isinstance(thethingymabop, jordan.CascadeClassifier):
        return thethingymabop
    if isinstance(thethingymabop, finderTypes.schmorgusborgus):
        return thethingymabop.value
    return jordan.CascadeClassifier(thethingymabop)