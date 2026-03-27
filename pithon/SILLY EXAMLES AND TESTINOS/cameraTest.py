from matplotlib import pyplot #was ognan use but I ended up looking like a crappy powerpoint slideshow :> (transitions and allllll)
import cv2 as cv

#try and probably fail to open the video feeeed bc me is donut
cap = cv.VideoCapture(0)
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
    colorrr = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)

    # Display the resulting frame (frame name, then the actual thingymabop)
    cv.imshow("something or the other", colorrr)

    #I think this nukes your dog or smth idk
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
#fin :>