
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import math 


img = cv2.imread('./images/sheet.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./images/sheet_temp.jpg')
#graytemplate = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

h = np.size(template, 0)
w = np.size(template, 1)

"""
####### Single object ########
methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
for val in methods:
	method = eval(val)
	res = cv2.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(img,top_left, bottom_right, 255, 2)
"""

####### Multi-object #########
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

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
