import cv2
img = cv2.imread('albert_einstein.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.putText(img, 'RGB resim', (1320,150), 0, 3, (255,255,255), 4, 0)
imgGray = cv2.putText(imgGray, 'gri tonlu resim', (1160,150), 0, 3, (255,255,255), 4, 0)
# resimleri yeniden boyutlandırıp ekranda görüntüle
s = 0.2
imgResized = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
imgGrayResized = cv2.resize(imgGray, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow('renkli resim', imgResized)
cv2.imshow('gri tonlu resim', imgGrayResized)
cv2.waitKey(0)
cv2.destroyAllWindows()