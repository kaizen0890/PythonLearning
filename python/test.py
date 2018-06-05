import os 

"""
import cv2 as cv
import numpy as np 
from sklearn import linear_model           # for logistic regression
from sklearn.metrics import accuracy_score # for evaluation
from scipy import misc                     # for loading image
"""


string_list = ["thanh", "cang", "dep", "trai"]

print (string_list[-2:])

for list in string_list[0:len(string_list) - 1]:
	print (list)


squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print squares 

dict = {'thanh':1, 'cang':2, 'dep':3, 'trai':4}

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:

	current_user = unconfirmed_users.pop()
	print ('We are verifying user: ' + current_user)
	confirmed_users.append(current_user)
#display confirmed_user
print ('List of Confirmed user: ')
for confirmed_user in confirmed_users:
	print (confirmed_user.title())


"""

##### Dictionary input()
active = True
team_members = {}


while active:
	name = raw_input("What's your name? ")
	job = raw_input("What's your dreamming job?")
	team_members[name] = job
	answer = raw_input("Would you like to become to our team member? (yes/no)")
	if answer == 'no':
		active = False

print ("Our team members in clude: \n")
for name,job in team_members.items():
	print(name.title() + " want to do" + job)


"""

class farmer(object):
	cost = 50
	health = 25;
	speed = 100;
	#list ability = ["fammer", "build", "attack"]
	#ability=[]
	
	speedWorking = 1
	attack = 3
	armor = 0
	#dict working = {"working_meat":10, "working_wood":10, "working_coin":10, "working_stone":10 }
	country = ""
	level = 0
	test = 1
	def __init__(self,cost, health, speed,speedWorking, attack, armor, country, level):
			self.cost = cost
			self.health = health
			self.speed = speed
			self.abilities = []
			self.workingIndex_dict = {}
			self.speedWorking = speedWorking
			self.attack = attack
			self.armor = 0
			self.country = country
			self.level = level
	def create_ability(self,*nameOfAbility):
		self.abilities.append(nameOfAbility)
	def create_workingIndex(self,workingIndex):
		self.workingIndex_list = workingIndex

palmyran_farmer = farmer(75,40,100,1,3,0,"Palmyran",0)
palmyran_farmer.create_ability('farmer','build', 'attack')
palmyran_farmer.create_workingIndex({'workingMeat':12,'workingWood':12,'workingCoin':12,'workingStone':12})
palmyran_farmer.speedWorking = 1.5

print "Palmyran farmer abilities is:"
for ability in palmyran_farmer.abilities:
	print ability
	
print "Palmyran workingIndex is"
for k,v in palmyran_farmer.workingIndex_list.items():
	print str(k) + ":" + str(v)
print "Palmyran farmer speedWorking:" , palmyran_farmer.speedWorking
#palmyran_farmer.create_working_index('workingMeat',10,'workingWood',10,'workingCoin',10,'workingStone', 10)



print "Palmyran farmer cost:", str(palmyran_farmer.cost) + " meat" 
print "Palmyran farmer's health is:", str(palmyran_farmer.health)

assyrian_farmer = farmer(50,25,130,1,3,0,"Assyrian",0)


class melee_chariot(farmer,object):
	def __init__(self,cost, health, speed,speedWorking, attack, armor, country, level):
		super(melee_chariot,self).__init__(cost, health, speed,speedWorking, attack, armor, country, level)
		self.distance = 50

class archer_chariot(farmer,object):
	def __init__(self,cost, health, speed,speedWorking, attack, armor, country, level):
		super(archer_chariot,self).__init__(cost, health, speed,speedWorking, attack, armor, country, level)
		self.archer_distance = 100
		self.horseLevel = 1
	def create_ability(self,*nameOfAbility):
		self.abilities.append("asd")

"""
myTest1 = melee_chariot(50,60,130,1,6,0,"Assyrian",0)
myTest2 = archer_chariot(50,60,130,1,4,0,"Assyrian",0)
myTest3 = archer_chariot(50,60,130,1,2,0,"Assyrian",0)
myTest3.create_ability('attack')


myTest2.create_ability('attack')

print "myTest2 abilities is:"
for ability in myTest2.abilities:
	print ability
print "myTest3 abilities is:"
for ability in myTest3.abilities:
	print ability

"""

class shield ():
	def __init__(self, archery_sheld = 0):
		self.archery_shield = archery_sheld
	def upgrade_shield(self):
		self.archery_shield += 1
		


class horse_chariot(farmer,object):
	def __init__(self,cost, health, speed,speedWorking, attack, armor, country, level):
		super(horse_chariot,self).__init__(cost, health, speed,speedWorking, attack, armor, country, level)
		self.distance = 120
		self.shield = shield()
		self.horseLevel = 1
	def upgrade_level(self):
		self.horseLevel = 2

myTest = horse_chariot(50,60,130,1,6,0,"Hittite",0)
print myTest.horseLevel
myTest.shield.upgrade_shield()
print myTest.shield.archery_shield


