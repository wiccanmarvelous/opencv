# # Essential functions in OpenCV

import cv2 as cv
img = cv.imread('learn_opencv\Photos\cat_rainbow.jfif')
# cv.imshow('Cat', img)

# -----------------------------------------------

# # Converting to grayscale

# # to see only the intensity distribution of pixel rather than the colour itself
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# -----------------------------------------------

# # Blur (Gaussian Blur)

# # bluring of image removes noise that exists in an image
# # noise may be because of bad lighting while taking or camera sensor issue
# # (source img, kernel size(2 by 2 tuple)(has to be odd number)(whit inc. size blur inc.), ...)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# -----------------------------------------------

# # Edge Cascade
# # basically finding the edges present in the image
# # using Canny edge detector:- multi step process that involves lot of blurring and grading computations
# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# -----------------------------------------------

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow('Dilated', dilated)

# -----------------------------------------------

# # Eroding
# # Eroding dilated image to get back the structuring element.
eroded = cv.erode(dilated, (7, 7), iterations=1)
# cv.imshow('Eroded', eroded)

# -----------------------------------------------

# # Resize
# # Takes any img to be resized and a destination size.
# # By default interpolation value is cv.INTER_AREA and this mehod useful
# # if we are shrinking the image to dimentions that are smaller than that of original dime.
# # In case of enlarging the image and scale the image to much larger dimentions we can use
# # INTER_LINEAR or INTER_CUBIC (CUBIC is slowest among them all but the resulting img quality is higher).
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',  resized)

# ------------------------------------------------

# # Cropping
# # Images are arrays and we can employ something called Array Slicing, we can select a
# # portion of image on the basis of your pixel values.
cropped = img[200:350, 500:800]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
