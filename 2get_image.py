import cv2 as cv


def video_demo():
    capture = cv.VideoCapture("VIDEO/test.ts")
    while (True):
        ret,frame = capture.read()
        #frame = cv.flip(frame,1)
        cv.namedWindow("video",cv.WINDOW_AUTOSIZE)
        cv.imshow("video",frame)
        c = cv.waitKey(27)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))#类型
    print(image.shape)#形状
    print(image.size)#尺寸
    print(image.dtype)

src = cv.imread("IMG/3.jpg")#读取图片
get_image_info(src)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#建立窗口
cv.imshow("input image",src)#展示图片
video_demo()
cv.waitKey(0)#无限等待图像显示
cv.destroyAllWindows()#销毁窗口