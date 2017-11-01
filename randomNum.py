#!/usr/bin/python3
import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def lcg(n, m, a, c, seed):
	numberList = []
	duplicateCount = 0
	Xn = float(seed)
	for i in range(n):
		Xn = (a*Xn + c) % m
		if round(Xn % 10000) in numberList:
			duplicateCount += 1
		numberList.append(round(Xn%10000)) 
	return numberList
	#print duplicateCount 

def lcg1(n, m, a, c, seed):
	numberList = []
	duplicateCount = 0
	Xn = float(seed)
	for i in range(n):
		Xn = (a*Xn + c) % m
		if round(Xn % 1000) in numberList:
			duplicateCount += 1
		numberList.append(round(Xn%1000)) 
	return numberList

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
		if r in numberList:
			r = int(r) + c
		if int(r) in numberList:
			duplicateCount += 1
		numberList.append(int(r))
	return numberList

#Also a good seed 
#datetime.now().microsecond

numberList = []
duplicateCount = 0
x0 = []
y0 = []#

for x in range(0,20000):
	random1 = random.randint(1,9999)
	if x % 2 == 0:
		x0.append(random1)
	else:
		y0.append(random1)

semicerc = 0
for i in range(10000):
	if (x0[i] ** 2) + (y0[i] ** 2) <= 100000000:
		semicerc += 1
print semicerc
print float(semicerc)/float(2500)
print

x1 = lcg(10000, 35371397137, 81, 19, 469314327.131197933)
y1 = lcg(10000, 35371397137, 81, 19, 347013719.177331533)#

semicerc = 0
for i in range(10000):
	if (x1[i] ** 2) + (y1[i] ** 2) <= 100000000:
		semicerc += 1
print semicerc
print float(semicerc)/float(2500)
print

x2 = midSquare(10000,113,2500)   
y2 = midSquare(10000,113,1475)

semicerc = 0
for i in range(10000):
	if (x2[i] ** 2) + (y2[i] ** 2) <= 100000000:
		semicerc += 1
print semicerc
print float(semicerc)/float(2500)
print

cercx = [0]
cercy = [10000]

for i in range(10000):
	for j in range(10000):
		if (i ** 2) + (j ** 2) == 100000000:
			cercx.append(i)
			cercy.append(j)

cercx.append(10000)
cercy.append(0)

plt.plot(x0, y0, ".", color="green")
plt.plot(cercx,cercy, color="black")
plt.show()

plt.plot(x1, y1, ".", color="blue")
plt.plot(cercx,cercy, color="black")
plt.show()

plt.plot(x2, y2, ".", color="red")
plt.plot(cercx,cercy, color="black")

aprVect = [0,]
Vect = []

for random_num in range(0,1000):
	Vect.append(random.randint(1,1000))
	aprVect.append(0)

for part in Vect:
	aprVect[part] += 1

ox = []

for nr in range (1,1001):
	ox.append(nr)

x = np.arange(1001)

fig, ax = plt.subplots()
plt.bar(x, aprVect)
plt.xticks(x, ox)
plt.show()


aprVect = [0,]
Vect = []

for random_num in range(0,1000):
	aprVect.append(0)

Vect = lcg1(10000, 35371397137, 81, 19, 469314327.131197933)

for part in Vect:
	aprVect[int(part)] += 1

ox = []

for nr in range (1,1001):
	ox.append(nr)

#x = np.arange(1000)

fig, ax = plt.subplots()
plt.bar(x, aprVect)
plt.xticks(x, ox)
plt.show()

aprVect = [0,]
Vect = []

for random_num in range(0,1000):
	aprVect.append(0)

Vect = midSquare(1000,113,1475)

for part in Vect:
	aprVect[part%1001] += 1

ox = []

for nr in range (1,1001):
	ox.append(nr)

#x = np.arange(1000)

fig, ax = plt.subplots()
plt.bar(x, aprVect)
plt.xticks(x, ox)
plt.show()