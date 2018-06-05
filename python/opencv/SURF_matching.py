import cv2
import sys
import os.path
import numpy as np

MIN_MATCH_COUNT=20

img1 = cv2.imread('./images/adidas.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('./images/logos.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(400)
## Pass dictionary parametter to FLANN library
FLANN_INDEX_KDITREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})

# find the keypoints and descriptors with SIFT
kp1, des1 = surf.detectAndCompute(gray1,None)
kp2, des2 = surf.detectAndCompute(gray2,None)

## using KNN match to find matches between two descriptors of query and train.
## Note: Query des is first parametter of this function
matches=flann.knnMatch(des2,des1,k=2)

## Create goodMatch to store satisfied matches point 
goodMatch=[]
for m,n in matches:
	if m.distance < 0.7*n.distance:
		goodMatch.append(m)
if len(goodMatch) > MIN_MATCH_COUNT:
	trainPoint=[]
	queryPoint=[]
	## Add train & query Kp to trainPoint, queryPoint
	for m in goodMatch: 
		trainPoint.append(kp1[m.trainIdx].pt)
		queryPoint.append(kp2[m.queryIdx].pt)

	trainPoint, queryPoint = np.float32((trainPoint, queryPoint))
	## cv2.findHomography will find locations of some parts of an object in another cluttered image
	H,status=cv2.findHomography(trainPoint,queryPoint,cv2.RANSAC,3.0)
	h = np.size(img1, 0)
	w = np.size(img1, 1)
	img1Border=np.float32([[[0,0],[0,h-20],[w-1,h-20],[w-1,0]]])
	### find the object
	img2Border=cv2.perspectiveTransform(img1Border,H)
	cv2.polylines(img2,[np.int32(img2Border)],True,(0,255,0),5)
else:
	print "Not Enough match found- %d/%d"%(len(goodMatch),MIN_MATCH_COUNT)
	
cv2.imshow('result',img2)
cv2.waitKey(0)
