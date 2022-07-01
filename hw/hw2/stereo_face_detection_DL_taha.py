import cv2
import numpy as np
import imageio

print("[BİLGİ] Yüz tespiti için derin öğrenme modeli olan ResNet Caffe'den yükleniyor...")
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')
conf = 0.45 # minimum probability to filter weak detections

img1 = cv2.imread('taha-data/CAM0_image_0000.jpg')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('taha face detection DL.avi', fourcc, 10, (2*img1.shape[1], img1.shape[0]), True)
writerGIF = imageio.get_writer('taha face detection DL.gif', mode='I')

for i in range (66): # furkan-data-1 için 66, furkan-data-2 için 47,114,1
    if i<10:
        img1 = cv2.imread('taha-data/CAM0_image_000%i.jpg' %i)
        img2 = cv2.imread('taha-data/CAM1_image_000%i.jpg' %i)
    else:
        img1 = cv2.imread('taha-data/CAM0_image_00%i.jpg' %i)
        img2 = cv2.imread('taha-data/CAM1_image_00%i.jpg' %i)
    (h,w,c) = img1.shape
    stereo = np.zeros((h,2*w,c), np.uint8)
    blob1 = cv2.dnn.blobFromImage(cv2.resize(img1, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
    blob2 = cv2.dnn.blobFromImage(cv2.resize(img2, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
	# pass the blob through the network and obtain the detections and predictions
    net.setInput(blob1)
    detections1 = net.forward()
    net.setInput(blob2)
    detections2 = net.forward()
	# loop over the detections
    for j in range(0, detections1.shape[2]):
		# extract the confidence (i.e., probability) associated with the prediction
        confidence = detections1[0, 0, j, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
        if confidence < conf:
            continue
		# compute the (x,y)-coordinates of the bounding box for the object
        box = detections1[0, 0, j, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
		# draw the bounding box of the face along with the associated probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(img1, (startX,startY), (endX,endY), (0, 255, 0), 8)
        cv2.putText(img1, text, (startX,y), cv2.FONT_HERSHEY_SIMPLEX, 1.15, (0, 255, 0), 4)
    for j in range(0, detections2.shape[2]):
		# extract the confidence (i.e., probability) associated with the prediction
        confidence = detections2[0, 0, j, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
        if confidence < conf:
            continue
		# compute the (x,y)-coordinates of the bounding box for the object
        box = detections2[0, 0, j, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
		# draw the bounding box of the face along with the associated probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(img2, (startX,startY), (endX,endY), (0, 255, 0), 8)
        cv2.putText(img2, text, (startX,y), cv2.FONT_HERSHEY_SIMPLEX, 1.15, (0, 255, 0), 4)
    stereo[:,0:w,:] = img1
    stereo[:,w:2*w,:] = img2
    writer.write(stereo)
    s = 0.3
    rstereo = cv2.resize(stereo, (int(s*stereo.shape[1]), int(s*stereo.shape[0])), cv2.INTER_LINEAR)
    if i>30:
        writerGIF.append_data(rstereo)
    cv2.imshow('Derin ogrenme ile yuz tespiti', rstereo)
    #cv2.waitKey()
    if cv2.waitKey(1) == 27:
        break
writer.release()
cv2.destroyAllWindows()