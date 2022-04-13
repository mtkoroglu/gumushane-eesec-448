import cv2
import numpy as np

(r,c) = (256,256)
imgBlack = np.zeros((r,c), np.uint8)
imgWhite = 255*np.ones((r,c), np.uint8)
imgGray = 127*np.ones((r,c), np.uint8)
imgMerged = np.zeros((r,3*c), np.uint8)
imgMerged[:,0:c] = imgBlack
imgMerged[:,c:2*c] = imgWhite
imgMerged[:,2*c:3*c] = imgGray
imgPatterns = np.zeros_like(imgMerged)
for i in range(r):
    for j in range(c):
        imgPatterns[i,j] = i
    for j in range(c,2*c):
        imgPatterns[i,j] = j
    for j in range(2*c,3*c):
        imgPatterns[i,j] = (i+j)/2
cv2.imshow('siyah beyaz gri', imgMerged)
cv2.imshow('gri tonlu desenler', imgPatterns)
cv2.waitKey(0)
cv2.destroyAllWindows()