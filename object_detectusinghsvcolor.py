import cv2
import numpy as np

cam=cv2.VideoCapture(0)

def empty(x):
	pass

cv2.namedWindow("trackbar")
#trackbar creation to see various combination of colors 
cv2.createTrackbar("L-H","trackbar",0,179,empty)
cv2.createTrackbar("L-S","trackbar",0,255,empty)
cv2.createTrackbar("L-V","trackbar",0,255,empty)
cv2.createTrackbar("U-H","trackbar",179,179,empty)
cv2.createTrackbar("U-S","trackbar",255,255,empty)
cv2.createTrackbar("U-V","trackbar",255,255,empty)




while True:

	_,frame=cam.read()

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#get trackbar to respond to the to satidfy the min max range for detection 
	l_h=cv2.getTrackbarPos("L-H","trackbar")
	l_s=cv2.getTrackbarPos("L-S","trackbar")
	l_v=cv2.getTrackbarPos("L-V","trackbar")
	u_h=cv2.getTrackbarPos("U-H","trackbar")
	u_s=cv2.getTrackbarPos("U-S","trackbar")
	u_v=cv2.getTrackbarPos("U-V","trackbar")


	min=np.array([l_h,l_s,l_v])
	max=np.array([u_h,u_s,u_v])

	mask=cv2.inRange(hsv,min,max)

	final=cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow("frame",frame)
	cv2.imshow("mask",mask)
	cv2.imshow("res",final)

	k=cv2.waitKey(1)
	if k==27:
		break

cam.release()
cv2.destroyAllWindows()