import cv2
print('[BİLGİ] Yüz Tespiti için Haar Cascade yükleniyor...')
detector = cv2.CascadeClassifier('requirement/haarcascade_frontalface_default.xml')
img = cv2.imread('image/tahaSharp.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('[BİLGİ] Yüz tespiti gerçekleştiriliyor...')
rects = detector.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=25)
print('Toplam %i yüz tespit edildi.' %len(rects))
for (x,y,w,h) in rects:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 7)
cv2.imwrite('result/taha phd columbus HC.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])
s = 0.25
rimg = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), cv2.INTER_LINEAR)
cv2.imshow('Haar Cascade metodu ile Yuz Tespiti', rimg)
cv2.waitKey(0)