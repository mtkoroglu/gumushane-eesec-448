import cv2
img = cv2.imread('albert_einstein.jpg')
print('Yükseklik = %i piksel   Genişlik = %i piksel' %(img.shape[0], img.shape[1]))
print('Kanal sayısı = %i' %img.shape[2])
print('BGR resim sol en üst pikselin şiddet değeri ve bilgileri')
print(img[0][0])
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.putText(img, 'RGB resim', (1320,150), 0, 3, (255,255,255), 4, 0)
# imgGray = cv2.putText(imgGray, 'gri tonlu resim', (1160,150), 0, 3, (255,255,255), 4, 0)
print('Gri tonlu resim sol en üst pikselin şiddet değeri ve bilgileri')
print(imgGray[0][0])
T = 60
(T, imgBW) = cv2.threshold(imgGray, T, 255, cv2.THRESH_BINARY)
# resimleri yeniden boyutlandırıp ekranda görüntüle
s = 0.2
imgResized = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
imgGrayResized = cv2.resize(imgGray, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
imgBWResized = cv2.resize(imgBW, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow('renkli resim', imgResized)
cv2.imshow('gri tonlu resim', imgGrayResized)
textWindow = 'T = %i icin siyah beyaz resim' %T
cv2.imshow(textWindow, imgBWResized)
cv2.waitKey(0)
cv2.destroyAllWindows()