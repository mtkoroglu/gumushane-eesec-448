# EESEC 448
Merhaba arkadaşlar. Bu sayfada **OpenCV**'nin **OpenCV for Beginners** isimli resmi kursunu referans olacağız. Bu kursa 

https://opencv.org/course-opencv-for-beginners/

bağlantısından ulaşabilirsiniz. Kursa kayıt ücreti $117. Ben bu kursa  

https://www.kickstarter.com/projects/opencv/opencv-for-beginners

bağlantısından çok önce kayıt olup $57 ödemiştim. Ayrıca **Adrian Rosebrock** tarafından kurulan **PyImageSearch University** diğer büyük bir referansımız.

https://www.pyimagesearch.com/pyimagesearch-university/

Bu plana yaklaşık olarak $300 gibi bir ücretle kaydolabiliyorsunuz. Adrian'ın **PyImageSearch university** planında **OpenCV 101 — OpenCV Basics** kursunda öğretilen konuların hepsini EEM 448'de işleyeceğiz. Sizlerin bu kurs ve planlara kaydolmanız zorunlu değil. DBS ve bu sayfayı takip ederseniz yeterli olacaktır.

Bu sayfadaki projelerde **Python 3.9.6** ve **OpenCV 4.5.5** kullanacağız. Aşağıda açıklamalarını/sonuçlarını gördüğünüz projelerin **py** uzantılı **Python** kodlarını yukarıda **project** isimli dosyada bulabilirsiniz. Bilgisayarınıza **Python** yüklemek için aşağıdaki resime tıkladığınızda açılan videoyu takip edebilirsiniz. Bu videoda ayrıca **OpenCV** yüklemeye de başlıyoruz ama bir hata ile karşılaşınca yarıda kalıyor.

[![IMAGE ALT TEXT HERE](figure/install-python.jpg)](https://www.youtube.com/watch?v=HwQ46b3KmUw)

Karşılaşılan hatayı çözüp **OpenCV** yüklemeyi tamamladığımız video için aşağıdaki resme tıklayabilirsiniz.

[![IMAGE ALT TEXT HERE](figure/opencv-python-resized.jpg)](https://www.youtube.com/watch?v=9DwK0K8UcAw)
#### Kullandığımız Komutlar
Masaüstünde **EESEC 448** isimli klasörü oluşturduktan sonra **Windows PowerShell**'de gerekli **cd** komutlarıyla bu klasörün içine girin. Sonra sanal ortam (İng. virtual environment) oluşturmak için 

```
python -m venv opencv-env
```

yazın. Ardından bulunduğunuz dizinde 

```
.\opencv-env\Scripts\activate
```

komutunu girerek sanal ortamı aktif hale getirin. Bunu müteakiben sırasıyla 

```
pip install opencv-contrib-python streamlit jupyter moviepy ipykernel matplotlib
```

ve

```
pip install pyautogui mediapipe mime
```

yazıp çalıştırarak bilgisayarımızda OpenCV koşturabilmek için gerekli olan bütün paket ve kütüphaneleri yükleyin. Bilgisayarımıza Python ve OpenCV yükledikten sonra opencv-env isimli bir sanal ortam oluşturup içerisine OpenCV ve bağımlı olduğu kütüphaneleri yüledik. Derste kullanacağımız Visual Studio Code editöründe kod yazarken kullanacağımız OpenCV fonksiyonları hakkında yardım alabilmek için Visual Studio Code'a sanal ortamımızı kaydetmemiz lazım. Bu işlem için aşağıdaki resme tıklayınca açılan videoyu izleyin.

[![IMAGE ALT TEXT HERE](figure/opencv_env_VSC.jpg)](https://youtu.be/6Z5lM1WqBXU)

## Proje 1: Resim Yükleme
### Yüklenen Resmin Üzerine Yazı Yazma, Resmi Yeniden Boyutlandırma, Ekranda Görüntüleme ve Dosyaya Kaydetme
Bu egzersizde OpenCV kütüphanesinden **imread()**, **putText()**, **resize()**, **imshow()** ve **imwrite()** fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız fonksiyon olan **imread()** argüman olarak uzantısıyla beraber resim/fotoğraf ismi kabul ediyor. Yani fonksiyona *string* veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi **IMG_20210616_202539.jpg** olduğundan **imread('IMG_20210616_202539.jpg')** şeklinde fonksiyonu çağırdığımızda resmi bizim ismini verdiğimiz değişkene atıyor. Bu arada gözden kaçırmayın, bütün fonksiyonları her zaman **cv2** anahtar kelimemizin sonuna **nokta** koyup çağırıyoruz, çünkü **cv2** yazdığımız kodda OpenCV kütüphanesini temsil ediyor. Zaten bu yüzden her kodumuzun başında **import cv2** diye bir komutla OpenCV'yi aktif hale getirmiş oluyoruz. Burada yazdıklarımızın kısa bir özeti: Eğer **IMG_20210616_202539.jpg** isimli bir resmi OpenCV'de Python ile okuyup **resim** isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.

```
import cv2
resim = cv2.imread('IMG_20210616_202539.jpg')
```

Aşağıdaki kod resmin **yüksekliğini** (height), **genişliğini** (width) ve BGR (Blue-Green-Red yani Mavi-Yeşil-Kırmızı) kanal sayısını (channels) **print** komutuyla ekrana basıyor. Burada yükseklik satır sayısına, genişlik sütun sayısına eşit. Aşağıdaki kod satırında **resim.shape[0]** ve **resim.shape[1]** komutları sırasıyla resmin yükseklik ve genişliğini piksel cinsinden bir sayı olarak ekrana basıyor.

```
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0], resim.shape[1], resim.shape[2]))
```

Aşağıdaki videoyu izleyerek yukarıda bir kısmı açıklanan ve tamamı aşağıda verilen kodu gerçekleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/imread_puttext_resize_imwrite.jpg)](https://youtu.be/622veo4_lDw)

```
import cv2 # OpenCV kütüphanesine erişim
resim = cv2.imread('IMG_20210616_202539.jpg') # resim yükle
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0],resim.shape[1],resim.shape[2]))
# resmin üzerine yazı yazalım
font = cv2.FONT_HERSHEY_SIMPLEX # font tipi
org = (300, 300) # yazının içinde bulunduğu dikdörtgenin sol alt köşesi
fontScale = 7 # font büyüklüğü
color = (0, 0, 0) # BGR sırasında yazının renk kodu
thickness = 12 # yazının kalınlığı
yaziliResim = cv2.putText(resim, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
# resmi yeniden boyutlandır, dosyaya kaydet ve ekranda görüntüle
s = 0.2 # scale - ölçek
dim = (int(s*resim.shape[1]), int(s*resim.shape[0])) # boyut
kucukResim = cv2.resize(yaziliResim, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Gumushane.jpg', kucukResim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("Uzerine yazi yazilmis ve yeniden boyutlandirilmis resim", kucukResim)
cv2.waitKey(0) # klavyede herhangi bir tuşa basana kadar ekranda görüntüle
```

## Proje 2: Web Kamerasına Erişim
Video dediğimiz şey ard arda yakalanan (İng. capture) resimlerin ekranda seri halde görüntülenmesinden başka birşey değil. Burada **FPS** kavramı karşımıza çıkıyor. Yani **Frame per Second**, Türkçesi **saniyedeki kare sayısı**. Aşağıdaki animasyonda [2] aynı hareketin değişik FPS değerlerinde yakalanmış halini izleyebilirsiniz. Animasyonda da görüldüğü gibi yüksek FPS değerleri ayrıntıları gözlemleyebilmeyi artırsa da daha fazla işlem yapıldığından dolayı bilgisayarı yoracaktır. Karşımıza çıkan FPS kavramını Sinyaller-Sistemler ve Haberleşme derslerinde gördüğünüz **örnekleme frekansı** (İng. sampling frequency) olarak düşünebilirsiniz.

<img src="https://www.productioncrate.com/news/wp-content/uploads/2019/08/ezgif-1-e18c2f9c89ad.gif" alt="FPS simulation" height="200"/>

Genelde FPS değeri standart web kameraları için 30. Bilgisayarımızın web kamerasını OpenCV kullanarak aşağıdaki gibi açabiliriz.

```
cap = cv2.VideoCapture(0)
```

Burada **VideoCapture** web kamerasına erişmek için bizim kullanımımıza sunulmuş OpenCV'nin **videoio** ana modülünde yer alan bir sınıf (class). Bu komuta 0 girişini verdik çünkü bilgisayarımızda eğer bir web kamerası varsa OpenCV o kameraya 0 kodunu atamış. Eğer birden fazla kamera varsa, o zaman argüman olarak 0 değil de 1, 2, ... girebiliriz. Bu arada **VideoCapture()** komutunun bize döndürdüğü değişkene **capture** kelimesinin kısaltması olan **cap** ismini uygun bulduk zira **capture** yakalamak demek ki web kamerası da saniyede otuz kez görüntüyü yakalayarak bize video sağlamış oluyor. OpenCV'de **VideoCapture** sınıfı web kamerası başarıyla açıldı mı açılmadı mı kontrol etmemiz için Türkçesi **acildi mi?** olarak tercüme edilebileek bir fonksiyon kullanımımıza sunuyor: **isOpened()**. Yukarıda **VideoCapture()** komutunun bize döndürdüğü **cap** değişkenini kullanarak kamera açıldı mı açılmadı mı aşağıdaki gibi kontrol edelim.

```
if (cap.isOpened() == False): ## eğer açılmadıysa
    print('Web kamerasına erişimde sorun yaşandı!')
else: ## eğer açıldıysa
    print('Kameranın FPS değeri %i.' %cap.get(cv2.CAP_PROP_FPS))
```

Eğer kamera yoksa veya erişimde (veya bağlantıda) bir sıkıntı yaşandıysa o zaman ekrana **Web kamerasına erişimde sorun yaşandı!** yazılacak. Aksi durumda kameradan kareler (İng. frame) sürekli geliyor olacak ve web kamerasının FPS değerini ekrana basacağız. Kameraya başarıyla eriştiğimizi kabul ederek devam ediyoruz. Şimdi görüntü sürekli gelmeye devam edeceğinden, web kamerası kare yakaladığı müddetçe aktif olacak bir döngü oluşturalım. Bu döngü içine her girişte web kamerasından resmi alıp **frame** isimli bir değişkene atayalım. Döngüden çıkmadan yakalanan renkli resmi ekranda **imshow()** komutu ile görüntüleyelim ve eğer kullanıcı **'q'** tuşuna bir an bile basarsa (imlecin görüntülediğimiz video ekranı üzerine tıklı olması lazım) o zaman o anda **frame** değişkeninde RAM hafızadaki resmi hard diskte dosyaya yazıp hem döngüden çıkalım hem de programı sonlandıralım.

```
import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print('Web kamerasına erişimde sorun!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv2.CAP_PROP_FPS))
while cap.isOpened() == True:
    ret, frame = cap.read() # web kamerası ile kare yakala
    if ret == True: # eğer kareyi yakaladıysak
        cv2.imshow('web kamerasi renkli resim', frame) # yakalanan kareyi ekranda görüntüle
        if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa
            cv2.imwrite('web kamerasi resim.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # dosyaya yaz 
            break # ve döngüden çık
    else: # eğer kareyi yakalayamadıysak
        print('Kare yakalanamadı!') # ekrana uyarı mesajı yaz
        break # ve döngüden çık
cap.release() # release serbest bırak demek
cv2.destroyAllWindows() # bütün pencereleri kapat ve programı sonlandır
```

Video için aşağıdaki resme tıklayınız.
[![IMAGE ALT TEXT HERE](https://www.manmade2.com/wp-content/uploads/2016/10/webCm1.png)](https://youtu.be/0LjEFyVVs0g)

## Proje 3: Filtreleme

## Proje 4: Piksel Değerlerine Erişim, RGB - Gri Tonlu - Siyah Beyaz Uzay, Eşikleme ve Görüntü İşleme Hızımızı Hesaplama
En son videoda **VideoCapture()** komutuyla aktif hale getirdiğimiz web kamerasından yakaladığımız kareleri gerçek-zamanda (İng. real-time) ekranda görüntülemiştik. Ard arda ekrana koyduğumuz kareler video gibi gözükmüştü. Şimdi ise RGB yani renkli resim formatında yakalayıp görüntülediğimiz resmi ilk önce gri tonlu (İng. gray scale) resme çevireceğiz. Bu işlemle artık bir piksele ait üç şiddet değeri değil de tek bir şiddet değeri olacak. İlk yaptığımız projedeki kodu (başka bir resim için) Python konsoluna aşağıdaki gibi girersek 

bahsettiğimiz üç şiddet değerini görmüş oluruz.

### Referanslar
[1] OpenCV 4.5.5 Dökümantasyonu - https://docs.opencv.org/4.5.5/</br>
[2] FPS animasyonu - https://news.productioncrate.com/tag/fps/</br>
[3] Standard Kütüphane ve **numpy** ile Rasgele Sayı, Dizi ve Matris Üretme - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/</br>
[4] OpenCV'de Eşikleme (Thresholding) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/</br>
[5] OpenCV'de Görüntü Filtreleme (Bulandırma) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/</br>
[6] OpenCV'de **Haar Cascade** Metodu ile Yüz Tespiti [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/05/opencv-face-detection-with-haar-cascades/</br>
[7] Raspberry Pi ve OpenCV kullanarak Pan-Tilt Kamera ile Yüz Takibi [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2019/04/01/pan-tilt-face-tracking-with-a-raspberry-pi-and-opencv/</br>
[8] Haar Cascade ile Yüz ve Göz Tespiti (OpenCV tutorial) - https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html</br>
[9] OpenCV'de Renk Uzayları Arasında Dönüşüm - https://www.pyimagesearch.com/2021/04/28/opencv-color-spaces-cv2-cvtcolor/</br>
[10] OpenCV ile Yeşil Top Tespiti (Takibi) - https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/</br>
[11] OpenCV'de **time** paketi kullanılarak FPS hesaplanması - https://www.geeksforgeeks.org/python-displaying-real-time-fps-at-which-webcam-video-file-is-processed-using-opencv/
