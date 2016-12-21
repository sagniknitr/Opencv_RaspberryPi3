from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 380)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 380))
 
# allow the camera to warmup
time.sleep(0.5)
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')

def nothing():
        pass

def initiate_script():
        print 'initiating Smart Vision'

def color_detect():


                hh='Hue High'
                hl='Hue Low'
                sh='Saturation High'
                sl='Saturation Low'
                vh='Value High'
                vl='Value Low'
                wnd ='Colorbars'
                cv2.namedWindow(wnd)
                print 'Now entering the trackbar'
                #Begin Creating trackbars for each
                cv2.createTrackbar(hl, wnd,0,179,nothing)
                cv2.createTrackbar(hh, wnd,0,179,nothing)
                cv2.createTrackbar(sl, wnd,0,255,nothing)
                cv2.createTrackbar(sh, wnd,0,255,nothing)
                cv2.createTrackbar(vl, wnd,0,255,nothing)
                cv2.createTrackbar(vh, wnd,0,255,nothing)
                print 'Now entering image capture loop'

                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=False):
                        # grab the raw NumPy array representing the image, then initialize the timestamp
                        # and occupied/unoccupied text
                            #read the streamed frames (we previously named this cap)
                    #_,frame=cap.read()
                        print 'Uptill now everything is okay'
                        image=frame.array
                        frame=cv2.GaussianBlur(image,(5,5),0)

                        print 'Lets convert the color'



                        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        hul=cv2.getTrackbarPos(hl, wnd)
                        huh=cv2.getTrackbarPos(hh, wnd)
                        sal=cv2.getTrackbarPos(sl, wnd)
                        sah=cv2.getTrackbarPos(sh, wnd)
                        val=cv2.getTrackbarPos(vl, wnd)
                        vah=cv2.getTrackbarPos(vh, wnd)
                 

                    #it is common to apply a blur to the frame 
                    #frame=cv2.GaussianBlur(image,(5,5),0)
                 
                    #convert from a BGR stream to an HSV stream
                        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                        #read trackbar positions for each trackbar
                    #make array for final values
                        HSVLOW=np.array([hul,sal,val])
                        HSVHIGH=np.array([huh,sah,vah])
                        mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
                        res = cv2.bitwise_and(frame,frame, mask =mask)
                        #cv2.imshow(wnd, res)
                        cv2.imshow(wnd,mask)
                        cv2.imshow("raw",image)
                        k = cv2.waitKey(5)
                        rawCapture.truncate(0)  # very important while using RPI Cam
                        if k == ord('q'):
                          break
        

def main():

                initiate_script()
                print 'Now starting python script color detect'
                color_detect()


if __name__ == "__main__": main()

                                        

                        
                        
                
