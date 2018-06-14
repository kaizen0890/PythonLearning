
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import math 


img = cv2.imread('./images/box.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,8,0.01,20)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('output',img)
cv2.waitKey(0)

"""
## Display result on matplot
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.show()
"""



"""
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

""" 
"""
cap = cv2.VideoCapture('720.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
   	# Display the resulting frame
    frameROI = frame[100:400, 200:500]
    cv2.putText(frameROI,'OpenCV',(10,150), cv2.FONT_HERSHEY_COMPLEX, 2,(255,255,255),2,255)

    edge = cv2.Canny(frameROI,100,200)
    cv2.imshow('Canny', edge)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

"""










