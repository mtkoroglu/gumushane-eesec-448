import cv2

print('[BİLGİ] Yüz Tespiti için Haar Cascade yükleniyor...')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# IMG_20220522_145111.jpg --> minNeighbors = 16
# IMG_20220605_150433.jpg --> minNeighbors = 21
# IMG_20220604_135426.jpg --> minNeighbors = 35 (3 yüz tespit ediyor)
# IMG_20220604_140145.jpg --> minNeighbors = 17 (1 yüz tespit edemiyor)
img = cv2.imread('image/IMG_20220604_140145.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print('[BİLGİ] yüz tespitini gerçekleştiriyoruz...')
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=17, 
                                minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
print('Toplam %i yüz tespit edildi.' %len(rects))
# tespit ettiğimiz yüzler rects değişkeni içinde bilgileri mevcut
# şimdi tespit edilen yüzleri resim üzerine çizdirelim ve kaydedelim
for (x,y,w,h) in rects:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 9)

s = 0.15
rimg = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), cv2.INTER_LINEAR)

cv2.imshow('Haar Cascade metodu ile Yuz Tespiti', rimg)
cv2.waitKey(0)