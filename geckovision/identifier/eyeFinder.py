import cv2 as cv
import geckovision.identifier.generalFinder as imsolonely

cascadation = cv.CascadeClassifier("cascaaaaaades/dalookeyboidetector.xml")

def getAnnotatedFrame(frame):
    return imsolonely.getAnnotatedFrame(frame=frame, mmmcasperthefriendlyghost=cascadation)

def getEyeDetectionPoints(frame):
    return imsolonely.getDetectionPoints(frame=frame, mmmcasperthefriendlyghost=cascadation)