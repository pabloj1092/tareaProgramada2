#!/usr/bin/python
import sys
import math
import cache
import processor
from processor import read, write

#Processors 1 and 2
P1 = processor()
P2 = processor()

#Cache L1 to P1, L2 to P2 and L3 shared
b_size = 8*1024
b_sizeL3 = 64*1024
L1 = Cache(8)
L2 = Cache(8)
L3 = Cache(64)

offset = int(math.log(float(b_size),2))
index = int(math.log(float(b_size),2))
offsetL3 = int(math.log(float(b_sizeL3),2))
indexL3 = int(math.log(float(b_sizeL3),2))

miss_local_L1 = 0
miss_local_L2 = 0
miss_local_L3 = 0
hit_local_L1 = 0
hit_local_L2 = 0
hit_local_L3 = 0
hit = 0
miss = 0
mask = 0
maskL3 = 0

for i in range(index):
	mask = 1 + mask*2

for i in range(indexL3):
	maskL3 = 1  + maskL3*2

number_line = 1
for line in open('aligned.trace'):
	data = line.split()
	instruction = line.split(' ')[1]
	if(number_line%2 == 0):
		if(instruction == L):
			resultL1 = P1.read()
	else:
		P2

	number_line = number_line +1