#Draws a black canvas and gives the bars of blue , gren and red color
#for you to create various hues combinations our of the BGR combination 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


def empty():
	pass

def main():
	screen=np.zeros((512,512,3),np.uint8)
	window="Trackbar hai ye"

	cv2.namedWindow(window)

	cv2.createTrackbar("B",window,0,255,empty)
	cv2.createTrackbar("G",window,0,255,empty)
	cv2.createTrackbar("R",window,0,255,empty)



	while True:

		cv2.imshow(window,screen)

		b=cv2.getTrackbarPos("B",window)
		g=cv2.getTrackbarPos("G",window)
		r=cv2. getTrackbarPos("R",window)

		screen[:]=[b,g,r]
		print(b,g,r)

		cv2.waitKey(1)
	cv2.destroyAllWindows()



if __name__=="__main__":
	main()





