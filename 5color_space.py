import cv2 as cv
import numpy as np

def extract_object_demo():
    capture = cv.VideoCapture("VIDEO/test.ts")
    while(True):#一帧一帧读取
        ret,frame = capture.read()
        if ret == False:#如果没有返回就不继续读取了，退出循环
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)#根据HSV表格查询颜色，这里查找绿色
        lower_hsv = np.array([37,43,46])#最小范围
        upper_hsv = np.array([77,255,255])#最大范围
        mask = cv.inRange(hsv,lowerb = lower_hsv,upperb = upper_hsv)#逐帧查询包含绿色的部分
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitKey(40)
        if c == 27:
            break

def color_space_demo(image):#色彩空间转化
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#灰度处理
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)#HSV
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)#YUV
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)#YCrCb
    cv.imshow("Ycrcb",Ycrcb)


src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片

#color_space_demo(src)
#extract_object_demo()
#通道分离，分别展示
b,g,r = cv.split(src)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
#通道合并
src = cv.merge([b,g,r])
# src[:,:,0] = 0#修改第0个通道为0
cv.imshow("all image",src)



cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口