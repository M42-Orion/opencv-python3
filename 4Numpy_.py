import cv2 as cv
import numpy as np 

def access_pixels(image):#图像处理
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(width,height,channels)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255-pv
    cv.imshow("pixels_demo",image)

def access_pixels_1(image):#上一个方法的优化
    dst = cv.bitwise_not(image)
    cv.imshow("pixels_demo",dst)

def creat_image():#自己修改通道生成图片
    # img = np.zeros([400,400,3],np.uint8)#赋值定义类型
    # img[:,:,0] = np.ones([400,400])*255#修改通道值
    # #print(img)
    # cv.imshow("creat_img",img)

    # img = np.ones([400,400,1],np.uint8)
    # img = img * 127
    # cv.imshow("new image",img)
    # cv.imwrite("IMG/test.jpg",img)\

    m1 = np.ones([3,3],np.uint8)
    m1.fill(127)#填充
    print(m1)

src = cv.imread("IMG/3.jpg")#读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片
#access_pixels(src)\
t1 = cv.getTickCount()
access_pixels_1(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print(time*1000)
#creat_image()
cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口