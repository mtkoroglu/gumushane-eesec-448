import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print('Web kamerasına erişimde sorun!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv2.CAP_PROP_FPS))
while cap.isOpened() == True:
    ret, frame = cap.read()
    k = 15 # kernel size - pencere boyutu
    filtered = cv2.blur(frame, (k,k))
    # filtered = cv2.GaussianBlur(frame, (k,k), 0)
    # filtered = cv2.medianFilter(frame, k)
    # filtered = cv2.bilateralFilter(frame, k, 69, 39)
    windowText = '(%i x %i) pencere boyutu filtrelenmis video' %(k,k)
    if ret == True: # eğer kareyi yakaladıysak
        cv2.imshow('web kamerasi', frame)
        cv2.imshow(windowText, filtered)
        if cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ya basarsa
            cv2.imwrite('web kamerasi.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('web kamerasi filtrelenmis.jpg', filtered, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else: # eğer kareyi yakalayamadıysak
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()