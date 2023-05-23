# Reading images and videos

import cv2 as cv

# # reading images
img = cv.imread("learn_opencv_using_python\Photos\cat_tongue.jfif")

# # to display the image
# # new window = cat, actual matrix of pixels to display = img
# cv.imshow("Cat", img)

# # keyboard binding function waits for a specific delay or a time in millisecons for a key to pressed
# cv.waitKey(0)

# ---------------------------------
# this method either takes integer (0, 1, 3, etc.) for webcam or a path to a video file
capture = cv.VideoCapture("learn_opencv_using_python\Videos\cat_meow.mp4")

while True:

    # capture.read() reads int this video frame by frame and returns the frame and a boolean to tell
    # weather frame was succesfully read or not
    isTrue, frame = capture.read()

    # display an individual frame
    cv.imshow("Video", frame)

    # way to stop the video for playing indefinitely, if letter 'd' is pressed break out of this loop
    # and stop playing this video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# to release capture pointer
capture.release()
cv.destroyAllWindows()

# when video stops we get this error (-215:Assertion failed) which means open CV could not find a media
# file at a particular location that you specified
# reason: video ran out of frames as open CV could not find any more frames after the last frame in video.
# So unexpectedly broke out of while loop by itself by raising a cv2 error.
