import re
import shutil
import os
import cv2 
import numpy as np
import math
import csv
import itertools
import time


##import python file
import prepare_data
execfile("/home/thomas/Thomas/git-thomas/PythonOpencv/python/opencv/face_recognition/prepare_data.py")


######## Read each image in training data then store to faces and label data #########
def read_train_csv():
	with open(trainCSVPath,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter=';')
		for row in reader:
			# Read the image and convert to grayscale
			img = cv2.imread(row[0])
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# Convert the image format into numpy array
			image = np.array(gray, 'uint8')
			faces.append(image)
			labels.append(int(row[1]))


"""
def recognition():
	with open(testCSVPath,'rb') as csv1, open(resultCSVpath,'wb') as csv2:
		reader = csv.reader(csv1,delimiter=';')
		writer = csv.writer(csv2,delimiter=';')
		for row in reader:
			img = cv2.imread(row[0])
			testImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			testImage = np.array(testImage, 'uint8')
			label, coefficience = recognizer1.predict(testImage)
			writer.writerow([row[0], label])
"""


def recognition():
	global count #### using to calculate recognition rate
	with open(resultCSVpath,'wb') as resultcsv:
		writer = csv.writer(resultcsv,delimiter=';')
		for i in range(0,numberPerson):
			for j in range(0,numberImage):
				if (j>=0 and j <= 14) or (j >= 20 and j <=34):
					imageNum = numberImage*i +j+1
					testlabel = i + 1
					testImagePath = testPath + str(numberImage*i +j+1) +".bmp"
					img = cv2.imread(testImagePath)
					testImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					testImage = np.array(testImage, 'uint8')
					resultlabel, coefficience = recognizer1.predict(testImage)
					print resultlabel
					if resultlabel != testlabel:  #### compare result and true label to calculate recognition rate
						writer.writerow([testImagePath, resultlabel,testlabel,coefficience])
						count +=1

def calculate_result():
	numberOfTestingImage = 30*numberPerson
	recogRate = 100 - ((float)(100*count)/(numberOfTestingImage))
	print "Recognition rate: " + str(recogRate) + "%"



start = time.time()

#seperate_data()
create_train_csv()
create_result_csv()
training_data(faces,labels)
recognition()
calculate_result()

stop = time.time()

timeProcess = float (stop - start)
print "start time :" + str(start)
print "stop time: " + str(stop)
print "Time processing: " + str(timeProcess)