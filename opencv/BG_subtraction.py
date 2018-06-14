import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import math 




cap = cv2.VideoCapture('./videos/traffic.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg = cv2.createBackgroundSubtractorGMG()

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
  	fgmask = fgbg.apply(frame)
  	## Using GMG need to add this line:
  	## fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) 
   	cv2.imshow('output_video',fgmask)
   	k = cv2.waitKey(30) & 0xff
   	if k == 27:
   		break

cap.release()
cv2.destroyAllWindows()
   






