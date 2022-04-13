import cv2 
import numpy as np

image = cv2.imread('giraffe.jpg')
(r,c,ch) = image.shape
# görüntüyü değişik filtrelerden geçirelim
k = 25 # pencere boyutu
fimage1 = cv2.blur(image, (k,k))
fimage2 = cv2.GaussianBlur(image, (k, k), 0)
fimage3 = cv2.medianBlur(image, k)
fimage4 = cv2.bilateralFilter(image, k, 125, 125)

# filtrelenmiş resimlerin üzerine filtre isimlerini yazalım
image = cv2.putText(image, 'original', (1200, 150), 2, 3, (0,0,0), 3, 2)
fimage1 = cv2.putText(fimage1, 'blur()', (1300, 150), 2, 3, (0,0,0), 3, 2)
fimage2 = cv2.putText(fimage2, 'GaussianBlur()', (900, 150), 2, 3, (0,0,0), 3, 2)
fimage3 = cv2.putText(fimage3, 'medianBlur()', (950, 150), 2, 3, (0,0,0), 3, 2)
fimage4 = cv2.putText(fimage4, 'bilateralFilter()', (900, 150), 2, 3, (0,0,0), 3, 2)

# filtrelenmiş resimleri tek bir resim haline getirelim
imageMerged = np.zeros((r,5*c,ch), np.uint8)
imageMerged[:,0:c,:] = image
imageMerged[:,c:2*c,:] = fimage1
imageMerged[:,2*c:3*c,:] = fimage2
imageMerged[:,3*c:4*c,:] = fimage3
imageMerged[:,4*c:5*c,:] = fimage4
# filtrelemiş resimleri ekranda görüntülemek için yeniden boyutlandıralım
s = 0.15
dim = (int(s*imageMerged.shape[1]) , int(s*imageMerged.shape[0]))
rimageMerged = cv2.resize(imageMerged, dim, interpolation=cv2.INTER_AREA)
# yeniden boyutlandırılmış resimleri ekranda görüntüleyelim
cv2.imshow('merged', rimageMerged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtrelenmiş ve üzerine filtre ismi yazılmış resimleri dosyaya kaydedip çıkalım
cv2.imwrite('birlesik resim.jpg', imageMerged, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('birlesik resim dusuk boyut.jpg', rimageMerged, [cv2.IMWRITE_JPEG_QUALITY, 100])