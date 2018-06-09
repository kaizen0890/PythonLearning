import re
import shutil
import os
import cv2 
import numpy as np
import math
import csv


####### Functions which is used to sorting items in directory by sequence ########
def atoi(text):
	return int(text) if text.isdigit() else text

def natural_keys(text):
	'''
	alist.sort(key=natural_keys) sorts in human order
	http://nedbatchelder.com/blog/200712/human_sorting.html
	(See Toothy's implementation in the comments)
	'''
	return [ atoi(c) for c in re.split('(\d+)', text) ]


######## Define path of directories ########
path = (os.getcwd())
dataPath = (path+ "/CMU_PIE/")
path = (os.getcwd())
dataPath = (path+ "/CMU_PIE/")
testPath = (path + "/test/")
trainPath = (path + "/train/")
trainCSVPath = (path + "/csvfiles/train.csv")
testCSVPath = (path + "/csvfiles/test.csv")
originalCSVPath = (path + "/csvfiles/original.csv")
resultCSVpath = (path + "/csvfiles/result.csv")


####### Sorting image in directory by name #######
items = []
items = os.listdir(os.path.expanduser(dataPath))
items.sort(key=natural_keys)

####### Define data information #######
numberPerson = 68
numberImage = 45



faces = [] #Store face data in numpy array
labels = [] #Store label of face in numpy array
originals = [] #Store image path 
results = [] #Store recognition result (label)
count = 0 #Variable use to couting recognition rate

####### Create face recognizer ######## 

#recognizer1 = cv2.face.LBPHFaceRecognizer_create()
#recognizer1 = cv2.face.EigenFaceRecognizer_create()
recognizer1 = cv2.face.FisherFaceRecognizer_create()

####### Define program's functions ########

def seperate_data():
	testPath = (path + "/test/")
	trainPath = (path + "/train/")
	### Checking does directory exist, if existed, ignore this step
	if not os.path.exists(testPath):
		os.makedirs(testPath)
	if not os.path.exists(trainPath):
		os.makedirs(trainPath)

	### Seperate image to train and test parts. Then label each image by person number
	for i in range(0,numberPerson):
		for j in range(0,numberImage):
			fileName = dataPath + str(numberImage*i +j+1) +".bmp"
			label = str(i)
			if (j>=0 and j <= 14) or (j >= 20 and j <=34):
				testImagePath = testPath + str(numberImage*i +j+1) +".bmp"
				shutil.copy2(fileName, testImagePath) ## Copy image from src to dst 
			else:
				trainImagePath = trainPath + str(numberImage*i +j+1) +".bmp"
				label = str(i+1)
				shutil.copy2(fileName, trainImagePath)

####### Create train csv which stores absolute path of training image ########
def create_train_csv():
	csvPath = path + "/csvfiles/train.csv"
	imagePath = path + "/train/"
	with open(csvPath, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')
		for i in range(0,numberPerson):
			for j in range(0,numberImage):
				label = str(i+1)
				if (j>=0 and j <= 14) or (j >= 20 and j <=34):
					testImagePath = imagePath + str(numberImage*i +j+1) +".bmp"
				else:
					trainImagePath = imagePath + str(numberImage*i +j+1) +".bmp"
					writer.writerow([trainImagePath,label])

####### Create result csv which stores information of fail image ########
def create_result_csv():
	csvPath = path + "/csvfiles/result.csv"
	with open(csvPath, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')

####### Start to train data ########
def training_data(faces, labels):
	read_train_csv()
	recognizer1.train(faces, np.array(labels))


"""
####### Create test csv which store absolute path of testing image ########
def create_test_csv():
	csvPath = path + "/csvfiles/test.csv"
	imagePath = path + "/test/"
	items = []
	items = os.listdir(os.path.expanduser(imagePath))
	items.sort(key=natural_keys)
	with open(csvPath, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')
		for item in items:
			testImagePath = imagePath + item
			writer.writerow([testImagePath])

####### Create original csv which store absolute path of all data and their true label ########	
def create_original_csv():
	csvPath = path + "/csvfiles/original.csv"
	items = []
	items = os.listdir(os.path.expanduser(dataPath))
	items.sort(key=natural_keys)
	with open(csvPath, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')
		for i in range(0,numberPerson):
			for j in range(0,numberImage):
				label = str(i+1)
				imageNum = str(numberImage*i +j+1) + ".bmp"
				writer.writerow([str(imageNum),str(label)])
"""