import imageio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from skimage.measure import compare_ssim as ssim
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import argparse
import imutils
#from imutils import contours
#from future.moves import tkinter
# %matplotlib inline

arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
first_pattern = cv2.imread("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern1.jpg")
middle_pattern = cv2.imread("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern50.jpg")
last_pattern = cv2.imread("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern100.jpg")

def image_measure():
    for x in range(4):
        y = x + 1
        for i in range(5):
            j = i + 1
            if y == 1:
                img = mpimg.imread(
                    '/home/socialvenu/SerialComm/TestImages/P' + str(y) + '/Cropped/Colors_Pattern' + str(j) + '.jpg')
                array1 = img[100:105, 40:45]
                mean = np.mean(array1)
                # print(mean)
                arr1 = np.append(arr1, mean)
                # print(arr1)
            if y == 2:
                img = mpimg.imread(
                    '/home/socialvenu/SerialComm/TestImages/P' + str(y) + '/Cropped/Colors_Pattern' + str(j) + '.jpg')
                array2 = img[100:105, 40:45]
                mean = np.mean(array2)
                # print(mean)
                arr2 = np.append(arr2, mean)
                # print(arr1)
            if y == 3:
                img = mpimg.imread(
                    '/home/socialvenu/SerialComm/TestImages/P' + str(y) + '/Cropped/Colors_Pattern' + str(j) + '.jpg')
                array3 = img[100:105, 40:45]
                mean = np.mean(array3)
                # print(mean)
                arr3 = np.append(arr3, mean)
                # print(arr1)
            if y == 4:
                img = mpimg.imread(
                    '/home/socialvenu/SerialComm/TestImages/P' + str(y) + '/Cropped/Colors_Pattern' + str(j) + '.jpg')
                array4 = img[100:105, 40:45]
                mean = np.mean(array4)
                # print(mean)
                arr4 = np.append(arr4, mean)
                # print(arr1)

    full_arr = np.vstack((arr1, arr2, arr3, arr4))
    print(full_arr)

########BREAK########
#Mean squared error and Structural Similarity Index calculations and visualizations
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()

def image_struct():
    # convert the images to grayscale
    first_pattern_gray = cv2.cvtColor(first_pattern, cv2.COLOR_BGR2GRAY)
    middle_pattern_gray = cv2.cvtColor(middle_pattern, cv2.COLOR_BGR2GRAY)
    last_pattern_gray = cv2.cvtColor(last_pattern, cv2.COLOR_BGR2GRAY)

    fig = plt.figure("Images")
    images = ("1st Pass", first_pattern_gray), ("50th Pass", middle_pattern_gray), ("100th Pass", last_pattern_gray)
    # loop over the images
    for (i, (name, image)) in enumerate(images):
        # show the image
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")
    # show the figure
    plt.show()
    # compare the images
    compare_images(first_pattern_gray, last_pattern_gray, "1st Pass vs. 100th Pass")
    compare_images(first_pattern_gray, middle_pattern_gray, "1st Pass vs. 50th Pass")
    compare_images(middle_pattern_gray, last_pattern_gray, "50th Pass vs. 100th Pass")


######## BREAK ##########
def image_diff(pattern1, pattern2):
    # Computing Image Differences
    # convert the images to grayscale
    pattern_1 = cv2.imread(pattern1)
    pattern_2 = cv2.imread(pattern2)
    grayA = cv2.cvtColor(pattern_1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(pattern_2, cv2.COLOR_BGR2GRAY)
    # diff is the difference image and score is the ssim value
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    # Threshold calculations
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(pattern_1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(pattern_2, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # show the output images
    cv2.imshow("First Pass", pattern_1)
    cv2.imshow("Last Pass", pattern_2)
    cv2.imshow("Diff", diff)
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def brightspot_detect(image_file, width):
    pattern = cv2.imread(image_file)
    gray = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blurred, 65, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)

    edged = cv2.Canny(blurred, 100, 255)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 100:
            continue
        # compute the rotated bounding box of the contour
        orig = pattern.copy()
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
        # loop over the original points and draw them
        for (x, y) in box:
            cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    # compute the midpoint between the top-left and top-right points,
    # followed by the midpoint between the top-righ and bottom-right
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    # draw the midpoints on the image
    cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
    # draw lines between the midpoints
    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
             (255, 0, 255), 2)
    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
             (255, 0, 255), 2)
    # compute the Euclidean distance between the midpoints
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    # if the pixels per metric has not been initialized, then
    # compute it as the ratio of pixels to supplied metric
    # (in this case, inches)
    if pixelsPerMetric is None:
        pixelsPerMetric = dB / width

    fig = plt.figure("Images")
    images = ("Pass", thresh)
    name = images[0]
    image = images[1]
    # show the image
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("on")

    plt.show()
    return fig


#z = brightspot_detect("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern1.jpg")
#y = brightspot_detect("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern100.jpg")
image_diff("/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern1.jpg", "/home/socialvenu/SerialComm/TestImages/P1/Cropped/Colors_Pattern2.jpg")
