import cv2
import numpy as np

(r,c) = (256,256)
img = np.zeros((r,c), np.uint8) # boş bir resim oluşturalım

# şimdi resmin bütün piksellerini tek tek dolaşacağız
# dolaşırken piksel değerlerini belirleyeceğiz
for i in range(r): # satırları dolaşalım
    for j in range(c): # sütunları dolaşalım
        img[i,j] = i # siz de j veya (i+j)/2 veya (i*j)/255 deneyin

cv2.imshow('gri tonlu resim', img)
cv2.waitKey(0)
cv2.destroyAllWindows()