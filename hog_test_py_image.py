from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import imutils

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 380)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 380))

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def initiate_script():
	print 'Welcome user to SMART HELMET program'


def HOG_process():

	print 'Now entering the capture loop'

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=False):

		print 'image captured'
		image=frame.array
		image=imutils.resize(image,width=min(400,image.shape[1]))
		orig=image.copy()
		#detect people in images
		(rects,weights)=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.05)

		#draw the original bounding boxes

		for (x,y,w,h) in rects :
			cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)

		#apply non-maxima compression
		rects=np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
		#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

		#store image in numpy array
		#im_np=np.float32(image)
		#scale the image
		#im_sc=np.float32(image)/255;

		# Calculate gradient 
		#gx = cv2.Sobel(im_sc, cv2.CV_32F, 1, 0, ksize=1)
		#gy = cv2.Sobel(im_sc, cv2.CV_32F, 0, 1, ksize=1)

		#print 'Gradient Calculation initiate'

		#mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)



		cv2.imshow('Original',image)
		cv2.imshow('No NMS',orig)
		#cv2.imshow('GrayScale',gray)
		#cv2.imshow('GX',gx)
		#cv2.imshow('GY',gy)

                k = cv2.waitKey(5)
                rawCapture.truncate(0)  # very important while using RPI Cam
                if k == ord('q'):
                  break
            
        


def main():

                initiate_script()
                print 'Now starting python script color detect'
                HOG_process()


if __name__ == "__main__": main()
