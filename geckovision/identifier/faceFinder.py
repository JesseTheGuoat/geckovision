import cv2 as cv
import geckovision.identifier.generalFinder as imsolonely

cascadation = cv.CascadeClassifier("cascaaaaaades/dafaceyboidetector.xml")

def getAnnotatedFrame(frame):
    return imsolonely.getAnnotatedFrame(frame=frame, mmmcasperthefriendlyghost=cascadation)

def getFaceDetectionPoints(frame):
    return imsolonely.getDetectionPoints(frame=frame, mmmcasperthefriendlyghost=cascadation)