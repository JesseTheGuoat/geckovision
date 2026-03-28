from enum import Enum
import cv2 as cv

class schmorgusborgus(Enum):
    FACES = cv.CascadeClassifier("cascaaaaaades/dafaceyboidetector.xml")
    EYES = cv.CascadeClassifier("cascaaaaaades/dalookeyboidetector.xml")