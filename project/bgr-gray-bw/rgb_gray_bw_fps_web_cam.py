import cv2
import time
from collections import deque
import numpy as np

cap = cv2.VideoCapture(0)
T = 60 # threshold value
k = 0 # frame index
fps = deque(maxlen=100)
timePrevious = time.time() # initialize previous time
while True:
    ret, frame = cap.read()
    k += 1
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    T, frameBW = cv2.threshold(frameGray, T, 255, cv2.THRESH_BINARY)
    timeCurrent = time.time()
    fpsCurrent = 1 / (timeCurrent - timePrevious)
    fps.appendleft(fpsCurrent)
    fpsAvg = np.mean(fps)
    # cv2.imshow('renkli', frame)
    # cv2.imshow('gri tonlu', frameGray)
    frameBWbgr = cv2.cvtColor(frameBW, cv2.COLOR_GRAY2BGR)
    frameBWbgr = cv2.putText(frameBWbgr, 'Avg FPS = %.2f' %fpsAvg, (30,50), 1, 2, (0,255,0), 2, 0)
    s = 0.5
    frame = cv2.resize(frame, (int(s*frame.shape[1]), int(s*frame.shape[0])), 0)
    frameGray = cv2.resize(frameGray, (int(s*frameGray.shape[1]), int(s*frameGray.shape[0])), 0)
    frameBWbgr = cv2.resize(frameBWbgr, (int(s*frameBW.shape[1]), int(s*frameBW.shape[0])), 0)
    cv2.imshow('renkli', frame)
    cv2.imshow('gri tonlu', frameGray)
    cv2.imshow('siyah beyaz (T=%i)' %T, frameBWbgr)
    print('Frame #%i    FPS = %.2f    avg FPS = %.2f' %(k,fpsCurrent, fpsAvg))
    timePrevious = timeCurrent
    if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa
        break
cap.release()
cv2.destroyAllWindows()