from matplotlib import pyplot #was ognan use but I ended up looking like a crappy powerpoint slideshow :> (transitions and allllll)
import cv2 as cv

#ok so now time to USE CASCADATION CLASSIFIERATION
cascadation = cv.CascadeClassifier("cascaaaaaades/haarcascade_eye.xml")

#try and probably fail to open the video feeeed bc me is donut
cap = cv.VideoCapture(0) #Select da camera (if youse has 2 cameras plugged in, then you could also use the second (1) or not bc the second is CRINGE and it commits ARSON on EVERYTHING and is a GENERAL I CANT SPELL THE WORD BUT YOU GET THE IDEA)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#main loop :>
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    #apparently this checks if the frame is ok (they just have a boolean for that :0)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # OK THIS IS MEANT TO MAKE A COLOR FILTER BUT IT JUST MAKES ME INTO A SMURF IFAOIFHEIEJKFWFEI
    greyyyyson = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    #MMMMM DETECTIONSSSS YUMMM AND EATTTT BACONATORRRR
    theGoods = cascadation.detectMultiScale(greyyyyson, minSize=(40, 40)) #minimum detection size: small chungus

    for (x, y, wideee, highh) in theGoods:
        cv.circle(img=greyyyyson, center=(int(x+(wideee/2)), int(y+(highh/2))), radius=5, color=(255, 0, 0), thickness=-1)

    # Display the resulting frame (frame name, then the actual thingymabop)
    cv.imshow("something or the other", greyyyyson)

    #I think this nukes your dog or smth idk
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
#fin :>