import cv2

print('[BİLGİ] Yüz Tespiti için Haar Cascade yükleniyor...')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image/messi.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print('[BİLGİ] yüz tespitini gerçekleştiriyoruz...')
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, 
                                minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
print('Toplam %i yüz tespit edildi.' %len(rects))
# tespit ettiğimiz yüzler rects değişkeni içinde bilgileri mevcut
# şimdi tespit edilen yüzleri resim üzerine çizdirelim ve kaydedelim
for (x,y,w,h) in rects:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow('Haar Cascade metodu ile Yuz Tespiti', img)
cv2.waitKey(0)