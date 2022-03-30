import cv2 as cv
import numpy as np
import lanes

video = cv.VideoCapture(0)

if not  video.isOpened():
    print('error while opening the video')

cv.waitKey(1)

while video.isOpened():
    _, frame = video.read()


    frame = lanes.canny(frame)

    cv.imshow("video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()

video.release()
cv.destroyAllWindows()