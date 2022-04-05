import cv2
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('renkli', frame)
    cv2.imshow('gri tonlu', frameGray)
    if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa
        break
cap.release()
cv2.destroyAllWindows()