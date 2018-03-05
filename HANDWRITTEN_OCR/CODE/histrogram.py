import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from shapely.geometry import Point
from shapely.geometry import Polygon

# import load.py
img = cv2.imread('../DATA/test1.jpg', cv2.IMREAD_GRAYSCALE)
im = Image.open("../DATA/test1.jpg").convert("RGBA")
height = np.size(img, 0)
width = np.size(img, 1)
i = 0
j = 0
list_row = []
list_fqncy = []
while i < height:
    j = 0
    fqncy = 0
    while j < width:
        px = img[i, j]
        if px < 150:
            fqncy = fqncy + 1

        j = j + 1
    if i == 0:
        list_row.append(0)
        list_fqncy.append(fqncy)
    else:
        list_row.append(i)
        list_fqncy.append(fqncy)
    i = i + 1
total = 0
row = 0

#print(list_fqncy)
for k in range(len(list_fqncy)):
    if list_fqncy[k] == 0:
        continue
    else:
        total = total + list_fqncy[k]
        row += 1
avr_fqncy = total / row
avr_fqncy = avr_fqncy * 0.36
# print(avr_fqncy)
list_belo_avr = np.array(list_fqncy)
ara_belo_avr = np.where(np.logical_and(list_belo_avr >= 0, list_belo_avr <= avr_fqncy))
belo_avr = ara_belo_avr[0]
print(belo_avr)

# filtering  the rows



min_diff = 4

indexCount = 0;
start_index = []
end_index = []

firstIndex = True
for x in range(1, len(belo_avr)):

    if int(belo_avr[x]) - int(belo_avr[x - 1]) >= min_diff:
        end_index.append(belo_avr[x - 1])
        start_index.append(belo_avr[x])

print("starting and ending index")
print(start_index)
print(end_index)


# filtering image
def line(row1, row2, x1, x2):
    print('x1=', x1, x2)
    while row1 <= row2:
        min_free = 100
        free = 0
        # print(row1," ")
        while x1 <= x2:
            px = img[row1, x1]
            # print(x1)
            if px < 100:
                free = free + 1
            x1 = x1 + 1
        if min_free > free:
            min_free = free
            min_row = row1
        # cv2.line(img, (x1, min_row), (x2, min_row), (0, 0, 0))
        row1 += 1
        # print(x1," ",x2," ",min_row)
        # cv2.line(img, (x1, min_row), (x2, min_row), (0, 0, 0))


def getFreq(row, x1, x2):
    frq = 0
    while (x1 <= x2):
        if (img[row, x1] < 100):
            frq += 1
        x1 += 1
    return frq


list_cut_points = []


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

    cv2.line(img, (x1, min_row), (x2, min_row), (0, 0, 0))
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


# calculation of function value
uper_line = [(0, 0), (width, 0)]
last = 0
low_line = []
for start in range(len(start_index) - 1):
    last = start
    row1 = start_index[start]
    row2 = end_index[start + 1]
    pre_w = 0
    test = True
    for x in range(row1, row2, 1):
        if (list_fqncy[x]) == 0:
            low_line = low_line + [(0, x), (width, x)]
            linecut(uper_line, low_line, start)
            uper_line.clear()
            test = False
            break
    if test == False:
        for y in range(len(low_line)):
            uper_line.append(low_line[y])
            #    print("uper_line=",uper_line)

    if test == True:
        for w in range(10, width, 10):
            # print(row1, " ", row2, " ", pre_w, " ", w)
            list_cut_points = list_cut_points + drawLine(row1, row2, pre_w, w)
            # print("points=",list_cut_points)
            pre_w = w
        for y in range(len(list_cut_points)):
            low_line.append(list_cut_points[y])
            # print("==>",low_line)
        # print("===>",low_line)
        linecut(uper_line, low_line, start)
        uper_line.clear()
        # list_cut_points.clear()
    #        print("=>",low_line)
    for y in range(len(low_line)):
        uper_line.append(low_line[y])
    # print(uper_line)
    list_cut_points.clear()
    low_line.clear()
low_line = [(0, height), (width, height)]
linecut(uper_line, low_line, last + 1)

# cv2.imshow("ima",im)
'''liists_avr=[]
for i in list_fqncy:
    if i<5:
        liists_avr=liists_avr+list_fqncy[i]
        continue
    elif i>len(list_fqncy)-6:
 
        continue
    avr=0
    j=i-4
    while 1:
        avr=avr+list_fqncy[j]
        j+=1
        if j==i+4:
            continue
    avr=avr/9
    liists_avr[i]=avr
print(liists_avr)'''
for i in range(height):
    if list_fqncy[i] == 0:
        cv2.line(img, (0, i), (width, i), (0, 0, 0))
'''    elif list_fqncy[i]>0 and list_fqncy[i]<7:
        line()'''
'''plt.bar(list_row,liists_avr,lebel='balta')
plt.show()'''
plt.bar(list_row, list_fqncy, label='histogram')
plt.xlabel('row_no')
plt.ylabel('frequency of black pixels')
plt.title('histogram')
plt.show()
"print(height," ",width)"
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
