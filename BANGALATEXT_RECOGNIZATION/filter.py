# import lib in here
import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt

img = cv.imread('my.jpg')

def imageBluring():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return cv.blur(gray, (10, 10))


def imageMedianBlurring():
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.medianBlur(img,5)


def showImage(img):
    # cv.imshow('img',img)
    cv.imshow('img',img)
    cv.waitKey(0)






def kernelFiltering():
    blur=cv.blur(img,(5,5))
    plt.imshow(img)



def bilateralFiltering():
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.bilateralFilter(img,75,75,75)




# main function is executing here

def main():

    #image bluring using blur method
   # imag=imageBluring()

   # imag=imageMedianBlurring()



    #kernelFiltering()
    imag=bilateralFiltering()
    showImage(imag)
    return 0


if __name__ == '__main__':
    main()
