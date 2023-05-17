# Image transformations

import cv2 as cv
import numpy as np

img = cv.imread("learn_opencv\Photos\cat_smart.jfif")

cv.imshow('Cat', img)

# --------------------------------------------

# Translation

# Shifting an Image along the x and y axis.
# You can shift image up, down, left and right using translation.
# x and y stands for number of pixels you want to shift along the x and y axis respectively.


def translate(img, x, y):
    # To translate an image we need to create a translation matrix.
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # dimentions of the image.
    # img.shape[1] is width and img.shape[0] is height of the image.
    dimentions = (img.shape[1], img.shape[0])
    # (img, transition matrix, dimentions)
    return cv.warpAffine(img, transMat, dimentions)

# -x --> left
# -y --> up
# x --> right
# y --> down

# Creating translated image.
translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

# -----------------------------------------------------

# Rotation

# Rotating an image by some angle.
# Opencv allows you to specify any rotation point that you like to rotate the image around.
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Rotation Matrix (rotation point, angle, scale value)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)

# negative angle value --> clockwise
# positive angle value --> anti-clockwise
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# ----------------------------------------------

# Resizing
# cv.resize(image, Destination size, interpolation)
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# -----------------------------------------------

# Flipping
# cv.flip(image, flip code)
# flip code = 0 means flipping the image vertically, 
# 1 means horizontally or over the y axis and
# -1 means flipping img both verticallyas well as horizontally. 
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# ------------------------------------------------

# Cropping

cropped = img

cv.waitKey(0)
