import cv2 as cv
import numpy as np

'''
高斯模糊，自定义噪声对高斯模糊没有太大影响
'''
def clamp(pv):#防止通道超出范围
    if pv>255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv

def gaussian_noise(image):#自定义噪声
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            image[row,col,0] = clamp(b + s[0])
            image[row,col,1] = clamp(g + s[1])
            image[row,col,2] = clamp(r + s[2])
    cv.imshow("noise image",image)

src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片

# gaussian_noise(src)
dst = cv.GaussianBlur(src,(0,0),15)#高斯模糊
cv.imshow("Gaussion Blur",dst)


cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口
