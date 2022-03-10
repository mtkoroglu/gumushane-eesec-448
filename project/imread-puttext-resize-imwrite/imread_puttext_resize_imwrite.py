import cv2
resim = cv2.imread('IMG_20210616_202539.jpg')
# puttext() fonksiyonunun argümanlarını oluştur
org = (300, 300)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 7 # yazının büyüklüğü
color = (255, 255, 255)
thickness = 12 # yazının kalınlığı
yaziliResim = cv2.putText(resim, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imwrite('Gumushane.jpg', yaziliResim, [cv2.IMWRITE_JPEG_QUALITY, 100])