import cv2 as cv
import numpy as np

# # to create blank image for drawing
# # dtype means data type and uint8 is data type of an image
# (500, 500, 3) = (height, width, number of colour channels)
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# -------------------------------------------------
# # image for drawing
# img = cv.imread("learn_opencv_using_python\Photos\cat_smart.jfif")
# cv.imshow('Cat', img)

# ----------------------------------------------

# # 1. Paint the image a certain colour
# # blank[:] referencing all the pixels and setting equal to colour value
# blank[:] = 0, 255, 0
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# -------------------------------------------------

# # 2. Draw a rectangle

# # this method takes in an image to draw the rectangle over

# # rectangle(img, point1, point2, colour, thickness(2 is the thickness of the borders),...) 
# # (0, 0) origin to (250, 250) with border of thickness 2 which is green in colour
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.rectangle(blank, (0, 0), (400, 250), (0, 255, 0), thickness=2)

# # (cv.FILLED or -1) fills all the specified colour in the rectangle
# cv.rectangle(blank, (0, 0), (400, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.rectangle(blank, (0, 0), (400, 250), (0, 255, 0), thickness=-1)

# # (blank.shape[1] // 2) halfs the dimentions of the original image
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 250, 0), thickness=-1)

# cv.imshow('Rectangle', blank)

# -----------------------------------------------------------

# # 3. Draw a circle

# # circle(img, center, radius, colour, thickness, ...)
# cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
# cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)

# ------------------------------------------------------------

# # 4. Draw a line
# cv.line(blank, (100, 100), (250, 250), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# ------------------------------------------------------------

# # 5. Write text
# # cv.putText(img, text, origin, font face, font scale, colour, thickness, ...)
# cv.putText(blank, 'Hello, I am Shreyash', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
# cv.imshow('Line', blank)

# cv.waitKey(0)
