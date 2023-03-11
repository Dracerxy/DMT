import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
cap= cv2.VideoCapture(0)

 
#url='http://192.168.165.144/cam-hi.jpg'
#url='1.jpg'
#im=None

 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        #img_resp=urllib.request.urlopen(url)
        #imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        #im = cv2.imdecode(imgnp,-1)
        ret,frame=cap.read()
        if not ret:
             break
        cv2.imshow('live transmission',frame)
        key=cv2.waitKey(100)
        if key==ord('q'):
            break 
            
    cv2.destroyAllWindows()
        
def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        #img_resp=urllib.request.urlopen(url)
        #imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        #im = cv2.imdecode(imgnp,-1)
        ret,frame=cap.read()
        if not ret:
             break
        bbox, label, conf = cv.detect_common_objects(frame)
        im = draw_bbox(frame, bbox, label, conf)
        print(label)
 
        cv2.imshow('detection',im)
        key=cv2.waitKey(100) 
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
 
 
 
if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            #f1= executer.submit(run1)
            f2= executer.submit(run2)