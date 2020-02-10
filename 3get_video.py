import cv2 as cv
'''
调用摄像头
'''

def video_demo():
    capture = cv.VideoCapture(0)#调用摄像头
    while (True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.namedWindow("video",cv.WINDOW_AUTOSIZE)
        cv.imshow("video",frame)
        cv.waitKey(50)
video_demo()