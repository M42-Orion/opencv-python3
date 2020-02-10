import cv2 as cv
import numpy as np


def blur_demo(image):#均值模糊
    dst = cv.blur(image,(1,21))#模糊1*3 y方向
    # dst = cv.blur(image,(3,1))#模糊3*1 x方向
    cv.imshow("blur_demo",dst)

def median_blur_demo():#中值模糊
    image = cv.imread("IMG/8.jpg")
    cv.imshow("test_demo",image)
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",dst)

def custom_blur_demo(image):#自定义模糊
    # kernel = np.ones([5,5],np.float32)/25
    # kernel = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)#锐化
    dst = cv.filter2D(image,-1,kernel = kernel)
    cv.imshow("custom_blur_demo",dst)

src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片

blur_demo(src)
# median_blur_demo()
# custom_blur_demo(src)
cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口