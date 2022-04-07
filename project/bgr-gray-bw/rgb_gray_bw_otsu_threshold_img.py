import cv2
img = cv2.imread('albert_einstein.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
T = 60 # 0 < T < 255
(T, imgBW) = cv2.threshold(imgGray, T, 255, cv2.THRESH_OTSU)
# resimleri yeniden boyutlandırıp ekranda görüntüle
s = 0.2
imgGrayResized = cv2.resize(imgGray, (int(s*imgGray.shape[1]), int(s*imgGray.shape[0])), 0)
imgBWResized = cv2.resize(imgBW, (int(s*imgBW.shape[1]), int(s*imgBW.shape[0])), 0)
cv2.imshow('gri tonlu resim', imgGrayResized)
cv2.imshow('Otsu metodu ile esik degeri T = %i' %T, imgBWResized)
cv2.waitKey(0)
cv2.destroyAllWindows()