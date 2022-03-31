import cv2
import time
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    timeStart = time.time() # başlangıç zamanını yakala
    filtered = cv2.bilateralFilter(frame, 27, 75, 85)
    timeStop = time.time() # bitiş zamanını yakala
    elapsedTime = timeStop - timeStart # geçen zamanı hesapladık
    cv2.imshow('bilateral filtre', filtered)
    print('Bilateral filtre %.5f s\'de koştu.' %elapsedTime)
    if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa -->
        break # --> programı sonlandır
cap.release()
cv2.destroyAllWindows()