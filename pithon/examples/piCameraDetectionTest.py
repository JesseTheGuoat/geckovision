from picamera2 import Picamera2
from flask import Flask, Response
import cv2 as cv

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())
picam2.start()

#ok so now time to USE CASCADATION CLASSIFIERATION
cascadation = cv.CascadeClassifier("cascaaaaaades/haarcascade_eye.xml")
if cascadation.empty():
    raise RuntimeError(f"Failed to load cascade")

""" the previous code is not applicable to the pi camera module 3
hence must obtain individual frames and then pass it into opencv """

def generate():
    while True:
        frame = picam2.capture_array()
        filteredFrame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        theGoods = cascadation.detectMultiScale(filteredFrame, minSize=(40, 40))
        for (x, y, wideee, highh) in theGoods:
            cv.circle(img=filteredFrame, center=(int(x+(wideee/2)), int(y+(highh/2))), radius=5, color=(255, 0, 0), thickness=-1)
        _, buffer = cv.imencode('.jpg', filteredFrame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=5000)

# #main loop :>
# while True:
#     try:
#         frame = picam2.capture_array()
#         filteredFrame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
#         #MMMMM DETECTIONSSSS YUMMM AND EATTTT BACONATORRRR
#         theGoods = cascadation.detectMultiScale(filteredFrame, minSize=(40, 40)) #minimum detection size: small chungus
#         # ............... nathan. we are not doing this again.
#         for (x, y, wideee, highh) in theGoods:
#             cv.circle(img=filteredFrame, center=(int(x+(wideee/2)), int(y+(highh/2))), radius=5, color=(255, 0, 0), thickness=-1)
#         # Display the resulting frame (frame name, then the actual thingymabop)
#     except KeyboardInterrupt: # quit
#         break

# cv.destroyAllWindows()
# picam2.stop()
#fin :>