import cv2 
import numpy as np 

a=cv2.imread('Thecropped.jpg',0)
cv2.namedWindow("image")

def empty(x):
	pass

cv2.createTrackbar("track","image",128,255,empty)

print(a[123,120])
while True:
	value_threshold=cv2.getTrackbarPos("track","image")
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_BINARY)
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_BINARY_INV)
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_TRUNC)
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_TOZERO)
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_TOZERO_INV)
	_,thres=cv2.threshold(a,value_threshold,255,cv2.THRESH_BINARY)


	cv2.imshow("win",thres)
	cv2.waitKey(0)


cv2.destroyAllWindows()
