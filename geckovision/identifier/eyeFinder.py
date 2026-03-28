import cv2 as cv
import geckovision.identifier.generalFinder as imsolonely

cascadation = cv.CascadeClassifier("cascaaaaaades/dalookeyboidetector.xml")

def getAnnotatedFrame(frame):
    imsolonely.getAnnotatedFrame(frame=frame, mmmcasperthefriendlyghost=cascadation)

def getEyeDetectionPoints(frame):
    imsolonely.getDetectionPoints(frame=frame, mmmcasperthefriendlyghost=cascadation)