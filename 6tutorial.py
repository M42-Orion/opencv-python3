import cv2 as cv
import numpy as np
'''像素运算，对比度亮度调整'''


def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)

def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)

def logic_demo(m1,m2):#逻辑运算，与或非
    dst = cv.bitwise_and(m1,m2)
    # dst = cv.bitwise_or(m1,m2)
    # dst = cv.bitwise_not(m1)
    cv.imshow("logic_demo",dst)

def contrast_brightness_demo(image,c,b):#调整对比度与亮度
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("co_br_demo",dst)

def others(m1,m2):
    # M1 = cv.mean(m1)
    # M2 = cv.mean(m2)
    # print(M1)
    # print(M2)
    M1,dev1 = cv.meanStdDev(m1)#求图片的标准差
    M2,dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)



src1 = cv.imread("image\LinuxLogo.jpg")#读取图片
src2 = cv.imread("image\WindowsLogo.jpg")#读取图片
src = cv.imread("IMG/3.jpg")

cv.namedWindow("image1",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("image1",src1)#展示图片
cv.imshow("image2",src2)#展示图片
cv.imshow("image",src)
# 两张图片执行加减乘除逻辑运算等操作
# add_demo(src1,src2)
# subtract_demo(src1,src2)
# divide_demo(src1,src2)
# multiply_demo(src1,src2)
# others(src1,src2)
# logic_demo(src1,src2)
contrast_brightness_demo(src,1,100)#对比度于曝光 

cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口