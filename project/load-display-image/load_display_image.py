import cv2
resim = cv2.imread('IMG_20210616_202539.jpg')
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0], resim.shape[1], resim.shape[2]))
# puttext() fonksiyonunun argümanlarını oluştur
org = (300, 300)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 7 # yazının büyüklüğü
color = (255, 255, 255)
thickness = 12 # yazının kalınlığı
yaziliResim = cv2.putText(resim, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
# resmi yeniden boyutlandır, dosyaya kaydet ve ekranda görüntüle
s = 0.2 # scale - ölçek
dim = (int(s*resim.shape[1]), int(s*resim.shape[0]))
kucukResim = cv2.resize(yaziliResim, dim, interpolation = cv2.INTER_AREA)
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(kucukResim.shape[0], kucukResim.shape[1], kucukResim.shape[2]))
cv2.imwrite('Gumushane.jpg', kucukResim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("Uzerine yazi yazilmis ve yeniden boyutlandirilmis resim", kucukResim)
cv2.waitKey(0) # klavyede herhangi bir tuşa basana kadar ekranda görüntüle