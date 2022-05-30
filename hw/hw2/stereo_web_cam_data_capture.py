import cv2
import time

cap1 = cv2.VideoCapture(0) # web kamerası 1'i aç
cap2 = cv2.VideoCapture(1) # web kamerası 2'yi aç
i = 0 # resmi kaydetme index'i
(recordTimeStart, recordTimeStop) = (6.0, 10.0)
initialTime = time.time()
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()    
    cv2.imshow('stereo cam-01', frame1)
    cv2.imshow('stereo cam-02', frame2)
    currentTime = time.time()
    elapsedTime = currentTime - initialTime
    if (elapsedTime > recordTimeStart) & (elapsedTime < recordTimeStop): # 5<t<10 boyunca dosyaya kaydet
        text1 = 'left cam %i.jpg' %i
        text2 = 'right cam %i.jpg' %i
        cv2.imwrite(text1, frame1, [cv2.IMWRITE_JPEG_QUALITY, 100])
        cv2.imwrite(text2, frame2, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('%s ve %s resimleri dosyaya kaydedildi.' %(text1, text2))
        i = i+1
    elif cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile c'ye basarsa:
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()