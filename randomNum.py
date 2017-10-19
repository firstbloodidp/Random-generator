#!/usr/bin/python3
import random
from datetime import datetime
import matplotlib.pyplot as plt

def lcg(n, m, a, c, seed):
	numberList = []
	duplicateCount = 0
	Xn = int(seed)
	for i in range(n):
		Xn = int(Xn)
		Xn = (a*Xn + c) % m
		if len(str(int(Xn))) < 4:
			Xn = ((4 - len(str(int(Xn)))) * '1') + str(Xn)
			if int(Xn) in numberList:
				duplicateCount += 1
			numberList.append(int(Xn))
	print duplicateCount 

def midSquare(n,c,seed):
	numberList = []
	duplicateCount = 0
	r= int(seed)
	for i in range(n):
		x = str(int(r)*int(r)) 
		y = int((len(x))/2)
		r = x[y-2:y+2] 
		r = int(r)
		if r % 25 == 0:
			r += c
		if len(str(r)) < 4:
			r = str(r) + ((4 - len(str(int(r)))) * '0')
		if r in numberList:
			r = int(r) + c
		if r in numberList:
			duplicateCount += 1
		numberList.append(r)
	print duplicateCount 

#Also a good seed 
#datetime.now().microsecond
numberList = []
duplicateCount = 0

for x in range(0,10000):
	random1 = random.randint(1,9999)
	if random1 in numberList:
		duplicateCount += 1
	numberList.append(random1)

print duplicateCount
print

lcg(10000, 10000, 73, 89, 4693)
print 

midSquare(10000,113,2500)   
print

x = 5000
y_2 = 5000
plt.plot(x, y_2, "o", color="blue")
plt.show()