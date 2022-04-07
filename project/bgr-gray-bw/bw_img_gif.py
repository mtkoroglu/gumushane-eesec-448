import cv2
import imageio
img = cv2.imread('albert_einstein.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
writer = imageio.get_writer('black and white.gif', mode='I')
for T in range(256):
    (T, imgBW) = cv2.threshold(imgGray, T, 255, cv2.THRESH_BINARY)
    imgBW = cv2.cvtColor(imgBW, cv2.COLOR_GRAY2BGR)
    imgBW = cv2.putText(imgBW, 'T = %i' %T, (70,150), 0, 3, (0,255,0), 4, 0)
    s = 0.2
    imgBWResized = cv2.resize(imgBW, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
    cv2.imshow('siyah beyaz resim', imgBWResized)
    imgBWResized = cv2.cvtColor(imgBWResized, cv2.COLOR_BGR2RGB)
    writer.append_data(imgBWResized)
    cv2.waitKey(20)
cv2.destroyAllWindows()