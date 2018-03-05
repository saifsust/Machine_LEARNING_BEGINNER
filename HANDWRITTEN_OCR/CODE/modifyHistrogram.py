import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# read image from DATA
img = cv.imread('../DATA/test1.jpg', cv.IMREAD_GRAYSCALE)
im = Image.open('../DATA/test1.jpg').convert("RGBA")

# properties
height = np.size(img, 0)
weight = np.size(img, 1)
print(height)
print(weight)

list_row = []
list_freq = []

start_point = []
end_point = []
cut_point = []


# end properties
# frequency calculation method
def frequencyCalculation():
    i = 0
    j = 0
    while i < height:
        # print("i=", i, "j=", j)
        freq = 0
        j = 0
        while j < weight:
            # print(j)
            px = img[i, j]
            if px < 150:
                freq += 1
            j += 1
        if i == 0:
            list_row.append(0)
            list_freq.append(freq)
        else:
            list_row.append(i)
            list_freq.append(freq)
        # print(i)
        i += 1


def calculateAverageFreq(list_freq):
    total = 0
    row = 0
    for freq in range(len(list_freq)):
        if (freq == 0):
            continue
        else:
            total += list_freq[freq]
            row += 1
    avr_freq = total / row
    return avr_freq * 0.36


def findAllfrequencyBelowAverage(list_freq, avr_freq):
    list = np.array(list_freq)
    list_below_avr = np.where(np.logical_and(list >= 0, list <= avr_freq))
    return list_below_avr[0]


def findStartEndPositionalListOfFrequency(list_below_avr):
    DIFFERENT = 4
    for x in range(1, len(list_below_avr)):
        if (int(list_below_avr[x]) - int(list_below_avr[x - 1])) >= DIFFERENT:
            end_point.append(list_below_avr[x - 1])
            start_point.append(list_below_avr[x])
            # print(end_point)
            # print(start_point)


# filtering
def line(row, prevRow, x, prevX):
    while row <= prevRow:
        MIN_FREE = 100
        free = 0
        while x < prevX:
            px = img[row, x]
            if (px < 100):
                free += 1
            x += 1
        if (MIN_FREE > free):
            MIN_FREE = free
            min_row = row
        row += 1


def getFreq(row, x1, x2):
    frq = 0
    while (x1 <= x2):
        if (img[row, x1] < 100):
            frq += 1
        x1 += 1
    return frq


def drawLine(prvEnd, nxtStrt, x1, x2):
    lmt = 0
    pe = prvEnd
    # print("called" , prvEnd , nxtStrt)
    while (getFreq(pe, x1, x2) > lmt and pe < nxtStrt):
        # print(" ---> " , getFreq(pe , x1 , x2), pe)
        pe += 1
    ns = nxtStrt
    while (getFreq(ns, x1, x2) > lmt and ns > prvEnd): ns -= 1

    if (ns >= pe):
        min_row = (ns + pe) / 2
    else:
        min_row = (prvEnd + nxtStrt) / 2

    # print(" =====> " , x1 , x2 , min_row)
    min_row = int(min_row)

    cv.line(img, (x1, min_row), (x2, min_row), (0, 0, 0))
    return [(x1, min_row), (x2, min_row)]




# cut line
def linecut(line_start, line_end, name):
    # print("called" , name)
    imArray = np.asarray(im)

    # create mask
    polygon = line_start
    i = len(line_end) - 1
    while i >= 0:
        polygon.append(line_end[i])
        i -= 1
    print(polygon)
    print(imArray.shape)
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
    mask = np.array(maskIm)

    # assemble new image (uint8: 0-255)
    newImArray = np.empty(imArray.shape, dtype='uint8')

    # colors (three first columns, RGB)
    newImArray[:, :, :3] = imArray[:, :, :3]
    # print(newImArray)
    # transparency (4th column)
    newImArray[:, :, 3] = mask * 255

    # back to Image from numpy
    newIm = Image.fromarray(newImArray, "RGBA")
    newIm.save("../SAVE/" + str(name) + ".png", "PNG")









def main():
    frequencyCalculation()
    print(list_row)
    print(list_freq)
    avr = calculateAverageFreq(list_freq)
    print(avr)
    below_avr_freq = findAllfrequencyBelowAverage(list_freq, avr)
    print(below_avr_freq)
    findStartEndPositionalListOfFrequency(below_avr_freq)
    print(end_point)
    return 0


if __name__ == '__main__':
    main()
