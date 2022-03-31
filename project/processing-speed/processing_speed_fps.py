import cv2
import time
cap = cv2.VideoCapture(1)
timePrevious = time.time()
while True:
    ret, frame = cap.read()
    filtered = cv2.bilateralFilter(frame, 27, 75, 85)
    timeCurrent = time.time() # şu anki zaman
    elapsedTime = timeCurrent - timePrevious # geçen zaman
    FPS = 1 / elapsedTime
    text = 'FPS = %.2f' %FPS
    filtered = cv2.putText(filtered, text, (30, 50), 0, 1, (0, 0, 0), 1, 1)
    cv2.imshow('bilateral filtre', filtered)
    print('Bilateral filtre %.5fs\'de koştu.' %elapsedTime)
    timePrevious = timeCurrent
    if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa -->
        break # --> programı sonlandır
cap.release()
cv2.destroyAllWindows()