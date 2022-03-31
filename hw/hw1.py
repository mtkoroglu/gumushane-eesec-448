import cv2 
image = cv2.imread('giraffe.jpg')

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

# filtrelemiş resimleri ekranda görüntülemek için yeniden boyutlandıralım
s = 0.2
dim = (int(s*image.shape[1]) , int(s*image.shape[0]))
rimage = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
rfimage1 = cv2.resize(fimage1, dim, interpolation = cv2.INTER_AREA)
rfimage2 = cv2.resize(fimage2, dim, interpolation = cv2.INTER_AREA)
rfimage3 = cv2.resize(fimage3, dim, interpolation = cv2.INTER_AREA)
rfimage4 = cv2.resize(fimage4, dim, interpolation = cv2.INTER_AREA)

# yeniden boyutlandırılmış resimleri ekranda görüntüleyelim
cv2.imshow('original', rimage)
cv2.imshow('blur()', rfimage1)
cv2.imshow('GaussianBlur()', rfimage2)
cv2.imshow('medianBlur()', rfimage3)
cv2.imshow('BilateralFilter()', rfimage4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtrelenmiş ve üzerine filtre ismi yazılmış resimleri dosyaya kaydedip çıkalım
cv2.imwrite('original.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('blur filter.jpg', fimage1, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('gaussian blur filter.jpg', fimage2, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('median filter.jpg', fimage3, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('bilateral filter.jpg', fimage4, [cv2.IMWRITE_JPEG_QUALITY, 100])