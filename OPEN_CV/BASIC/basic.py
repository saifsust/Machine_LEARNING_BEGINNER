import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


''' Properties '''

PATH='../data/data.jpg'
BACK='../data/back.jpg'
def readImg(path):
    return cv.imread(path)

def readImgAsGray(path):
    return cv.imread(path,0)

def show(img):
    cv.imshow('img',img)
    cv.waitKey()
    cv.destroyAllWindows()


def processing():
    img=readImg(BACK)
    HSV_Img(img)
   # img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #print(img.shape)
    #show(img)
    #print(img)



def HSV_Img(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow('img 0',img[:,:,0])
    cv.imshow('img 1',img[:,:,1])
    cv.imshow('img 2',img[:,:,2])
    cv.waitKey()
    cv.destroyAllWindows()




def spliteImg(path):
    img=readImg(path)
    B,G,R=cv.split(img)
    cv.imshow('B',B)
    cv.imshow('G',G)
    cv.imshow('R',R)
    cv.waitKey()
    cv.destroyAllWindows()

    merged=cv.merge([B,G,R])
    merged2=cv.merge([B+100,G,R])
    cv.imshow('merge',merged)
    cv.imshow('merged2',merged2)
    cv.waitKey()
    cv.destroyAllWindows()





def main():
    #img=readImg(PATH)
    #print(img)
   # processing()
    spliteImg(BACK)
    return 0



if __name__ =='__main__':
    main()
