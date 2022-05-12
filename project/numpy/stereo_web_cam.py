import cv2
import numpy as np

cap1 = cv2.VideoCapture(0) # web kamerası 1'i aç
cap2 = cv2.VideoCapture(1) # web kamerası 2'yi aç
i = 1 # resmi kaydetme index'i
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    (h,w,c) = frame1.shape
    frame1 = cv2.putText(frame1, 'CAM-00', (30,50), 1, 2, (0, 0, 255), 2, 1)
    frame2 = cv2.putText(frame2, 'CAM-01', (30,50), 1, 2, (0, 0, 255), 2, 1)
    # numpy kullanarak stereo resmi birleştirelim
    frame = np.zeros((h,2*w,c), np.uint8)
    frame[0:h,0:w,:] = frame1
    frame[0:h,w:2*w,:] = frame2
    s = 0.5
    rframe = cv2.resize(frame, (int(s*frame.shape[1]), int(s*frame.shape[0])), interpolation=cv2.INTER_AREA)
    cv2.imshow('web kamerasi stereo', rframe)
    if cv2.waitKey(1) & 0xFF == ord('c'): # eğer bir an bile c'ye basarsa
        text = 'stereo resim %i.jpg' %i
        cv2.imwrite(text, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('Web kameraları stereo resmi %s ismiyle dosyaya kaydedildi.' %text)
        i = i+1
    elif cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile c'ye basarsa:
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()