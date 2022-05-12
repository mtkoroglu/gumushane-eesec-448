import cv2

def crop(img, x, y):
    return img[x[0]:x[1],y[0]:y[1],:]

img = cv2.imread('giraffe.jpg')
x = (380, 662)
y = (460, 730)
# croppedImg = img[x[0]:x[1],y[0]:y[1],:]
croppedImg = crop(img, x, y)
cv2.imshow('cropped image', croppedImg)
cv2.waitKey(0)
