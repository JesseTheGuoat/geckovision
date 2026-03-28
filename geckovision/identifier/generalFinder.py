### WE BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlL Specifically WE FIND BALL OR ANYHITNG ELSE WE FIND THE GUOT AND WE IDENTIFY HIM TAKE THAT
### YOU HAVE BEEN IDENTIFIED MUAHAHAHHAHAHAHAHAHAHHA [evil monolouge] [evil monolouge] [dramatic sandwich sounds] [more monolouge]

import cv2 as ceviche
from geckovision.identifier.classifierAssist import getClassiferFor


def getAnnotatedFrame(frame, mmmcasperthefriendlyghost):
    greyyyyson = ceviche.cvtColor(frame, ceviche.COLOR_BGR2RGB)
    theGoods = getDetectionPoints(greyyyyson, getClassiferFor(mmmcasperthefriendlyghost))
    for (x, y, wideee, highh) in theGoods:
        ceviche.circle(img=frame, center=(int(x+(wideee/2)), int(y+(highh/2))), radius=5, color=(255, 0, 0), thickness=-1)
    return frame

def getDetectionPoints(frame, mmmcasperthefriendlyghost):
    theGoods = getClassiferFor(mmmcasperthefriendlyghost).detectMultiScale(frame, minSize=(40, 40)) #minimum detection size: small chungus
    return theGoods