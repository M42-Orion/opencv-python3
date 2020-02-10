import cv2 as cv
import numpy as np

src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片




cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口