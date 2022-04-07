import cv2
cap = cv2.VideoCapture(0)
T = 60 # threshold value
while True:
    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    T, frameBW = cv2.threshold(frameGray, T, 255, cv2.THRESH_BINARY)
    s = 0.5
    frame = cv2.resize(frame, (int(s*frame.shape[1]), int(s*frame.shape[0])), 0)
    frameGray = cv2.resize(frameGray, (int(s*frameGray.shape[1]), int(s*frameGray.shape[0])), 0)
    frameBW = cv2.resize(frameBW, (int(s*frameBW.shape[1]), int(s*frameBW.shape[0])), 0)
    cv2.imshow('renkli', frame)
    cv2.imshow('gri tonlu', frameGray)
    cv2.imshow('siyah beyaz (T=%i)' %T, frameBW)
    if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basılırsa
        break # programı sonlandır
cap.release()
cv2.destroyAllWindows()