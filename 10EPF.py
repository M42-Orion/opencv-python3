import cv2 as cv
import numpy as np

'''
边缘保留滤波
'''
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,50,5)
    cv.imshow("bi_demo",dst)

def py_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("py_demo",dst)

src = cv.imread("IMG/10.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片

bi_demo(src)#双边滤波
py_demo(src)#均值迁移
cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口
