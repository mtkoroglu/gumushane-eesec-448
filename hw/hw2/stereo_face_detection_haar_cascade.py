import cv2
import numpy as np

print('[BİLGİ] Yüz Tespiti için Haar Cascade yükleniyor...')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# read image sequence (stereo) pair by pair
for i in range(66): # make 66 for furkan-data-1 and 47,114,1 for furkan-data-2
    img1 = cv2.imread('furkan-data-1/left cam %i.jpg' %i)
    img2 = cv2.imread('furkan-data-1/right cam %i.jpg' %i)
    (h,w,c) = img1.shape
    stereo = np.zeros((h,2*w,c), np.uint8)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    rects1 = detector.detectMultiScale(gray1, scaleFactor=1.05, minNeighbors=25, 
                                minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    rects2 = detector.detectMultiScale(gray2, scaleFactor=1.05, minNeighbors=25, 
                                minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,width,height) in rects1:
        cv2.rectangle(img1, (x,y), (x+width,y+height), (0,255,0), 2)
    for (x,y,width,height) in rects2:
        cv2.rectangle(img2, (x,y), (x+width,y+height), (0,255,0), 2)
    stereo[:,0:w,:] = img1
    stereo[:,w:2*w,:] = img2
    cv2.imshow('Haar Cascade metodu ile Yuz Tespiti', stereo)
    cv2.waitKey(1)
cv2.destroyAllWindows()