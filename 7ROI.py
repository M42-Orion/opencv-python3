import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyimag = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)#必须+2，代码底层原因
    cv.floodFill(copyimag,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)#从30，30点开始填充
    cv.imshow("fill_color_demo",copyimag)

def fill_binary():
    image = np.zeros([400, 400, 3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fillbinary", image)
    mask =np.ones([402, 402, 1], np.uint8)
    mask[101:301,101:301] = 0#必须为0
    cv.floodFill(image, mask,(200, 200),(100,2, 255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow ("filled binary", image)

def gray(src):
    face = src[50:400,100:400]
    gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
    backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    src[50:400,100:400] = backface
    cv.imshow("face",src)

src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片、

gray(src)
#fill_color_demo(src)
# fill_binary()

cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口