import cv2
import numpy as np

img = cv2.imread('cheetah.jpg')
(h,w,c) = img.shape
# görüntüyü değişik pencere boyutlarında bulandıralım
k = (5,15,25)
filtered1 = cv2.blur(img, (k[0],k[0]))
filtered2 = cv2.blur(img, (k[1],k[1]))
filtered3 = cv2.blur(img, (k[2],k[2]))
# resimlerin üzerine pencere boyutlarını yazalım
img = cv2.putText(img, 'original', (500,50), 0, 1, (255,255,255), 2, 0)
filtered1 = cv2.putText(filtered1, '(%ix%i)' %(k[0],k[0]), (520,50), 0, 1, (255,255,255), 2, 0)
filtered2 = cv2.putText(filtered2, '(%ix%i)' %(k[1],k[1]), (480,50), 0, 1, (255,255,255), 2, 0)
filtered3 = cv2.putText(filtered3, '(%ix%i)' %(k[2],k[2]), (480,50), 0, 1, (255,255,255), 2, 0)
# NumPy ile ayrı resimleri birleştirelim - 2 x 2
mimg = np.zeros((2*h,2*w,c), np.uint8)
mimg[0:h,0:w,:] = img
mimg[0:h,w:2*w,:] = filtered1
mimg[h:2*h,0:w,:] = filtered2
mimg[h:2*h,w:2*w,:] = filtered3
s = 0.5
rimg = cv2.resize(mimg, (int(s*mimg.shape[1]), int(s*mimg.shape[0])), interpolation=cv2.INTER_AREA)
# resimleri görüntüle
cv2.imshow('merged image', rimg)
cv2.imwrite('filtered merged cheetah images.jpg', mimg, [cv2.IMWRITE_JPEG_QUALITY,100])
cv2.waitKey(0)
