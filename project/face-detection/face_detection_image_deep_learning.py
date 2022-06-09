import numpy as np
import cv2

# load our serialized model from disk
print("[INFO] loading model...")
# dnn deep neural network
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')
conf = 0.12 # minimum probability to filter weak detections


# IMG_20220522_145111.jpg IMG_20220605_150433.jpg IMG_20220604_135426.jpg IMG_20220604_140145.jpg
# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
image = cv2.imread('image/IMG_20220604_140145.jpg') # iron_chic.jpg rooster.jpg
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
	(300, 300), (104.0, 177.0, 123.0))

# pass the blob through the network and obtain the detections and
# predictions
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

# loop over the detections
for i in range(0, detections.shape[2]):
	# extract the confidence (i.e., probability) associated with the
	# prediction
	confidence = detections[0, 0, i, 2]

	# filter out weak detections by ensuring the `confidence` is
	# greater than the minimum confidence
	if confidence > conf:
		# compute the (x, y)-coordinates of the bounding box for the
		# object
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
 
		# draw the bounding box of the face along with the associated
		# probability
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY),
			(0, 0, 255), 9)
		cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

# show the output image
s = 0.2
rimage = cv2.resize(image, (int(s*image.shape[1]), int(s*image.shape[0])), cv2.INTER_LINEAR)
cv2.imshow("Face detection with deep learning", rimage)
cv2.waitKey(0)