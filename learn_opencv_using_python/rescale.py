# Resizing and Rescaling Frames

import cv2 as cv

# img = cv.imread("learn_opencv_using_python\Photos\cat_smart.jfif")
# cv.imshow("Cat", img)

# Rescaling: modifing height and width to a particular height and width. Changing width and height
# to a smaller value than the origunal dimension.

# passing frame to be resized and scale the vale which by default we're going to set as 0.75
# Images, Videos and Live Videos


def rescaleFrame(frame, scale=0.75):
    # frame.shape[1] is basically the width of your frame or image
    width = int(frame.shape[1] * scale)
    # frame.shape[0] is basically the height of your frame or image
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)

    # resize frame to particular dimension
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow("Image", resized_image)

# another way of rescaling and resizing video frames specifically and will work for images
# this function works ONLY for Live Videos (external camera or webcam)


def changeRes(width, height):
    # 3 and 4 stands for the properties of this capture class where
    # 3 references width and 4 references height
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture("learn_opencv_using_python\Videos\cat_meow.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
