import cv2 # OpenCV kütüphanesine erişim
import numpy as np

(r,c) = (256,256) # row = satır  column = sütun
# gri tonlu resimde 0 siyah 255 beyaz ve 127 gri renktir.
imgBlack = np.zeros((r,c), np.uint8) # siyah resim
imgWhite = 255*np.ones((r,c), np.uint8) # beyaz resim
imgGray = 127*np.ones((r,c), np.uint8) # gri resim
cv2.imshow('siyah', imgBlack)
cv2.imshow('beyaz', imgWhite)
cv2.imshow('gri', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()