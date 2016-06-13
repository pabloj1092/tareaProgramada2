#!/usr/bin/python
import sys
import math
from processor import processor
from cache import Cache

#Processors 1 and 2
P1 = processor()
P2 = processor()

#Cache L1 to P1, L2 to P2 and L3 shared
b_size = 8*1024
b_sizeL3 = 64*1024
L1 = Cache(8)
L2 = Cache(8)
L3 = Cache(64)


index = int(math.log(float(b_size),2))
indexL3 = int(math.log(float(b_sizeL3),2))

miss_local_L1 = 0
miss_local_L2 = 0
hit_local_L1 = 0
hit_local_L2 = 0
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
	tag = int(data[0], 16) #still not the tag
	read_index = tag & mask 
	for i in range (index):
		tag = (tag / 2) #now we have only the tag in $tag
	
	tagL3 = int(data[0], 16) #still not the tag
	read_indexL3 = tagL3 & maskL3     #extract the index
	for i in range (indexL3): #delete the index from the read
		tagL3 = (tagL3 / 2) #now we have only the tag in $tag
	if(number_line%2 == 0):
		if(instruction == 'L'):
			local_L2,glob,state = P2.read_p(read_index, tag, read_indexL3, tagL3, L2, L1, L3)
			if(local_L2 == 'miss_local'):
				miss_local_L2 = miss_local_L2 + 1
			else:
				hit_local_L2 = hit_local_L2 + 1
			if(glob == 'miss_global'):
				miss = miss + 1
			else:
				hit = hit + 1
		else:
			local_L2,glob,state = P2.write_p(read_index, tag, read_indexL3, tagL3, L2, L1, L3)
			if(local_L2 == 'miss_local'):
				miss_local_L2 = miss_local_L2 + 1
			else:
				hit_local_L2 = hit_local_L2 + 1
			if(glob == 'miss_global'):
				miss = miss + 1
			else:
				hit = hit + 1
	else:
		if(instruction == 'L'):
			local_L1,glob,state = P1.read_p(read_index, tag, read_indexL3, tagL3, L1, L2, L3)
			if(local_L1 == 'miss_local'):
				miss_local_L1 = miss_local_L1 + 1
			else:
				hit_local_L1 = hit_local_L1 + 1
			if(glob == 'miss_global'):
				miss = miss + 1
			else:
				hit = hit + 1
		else:
			local_L1,glob,state = P1.write_p(read_index, tag, read_indexL3, tagL3, L1, L2, L3)
			if(local_L1 == 'miss_local'):
				miss_local_L1 = miss_local_L1 + 1
			else:
				hit_local_L1 = hit_local_L1 + 1
			if(glob == 'miss_global'):
				miss = miss + 1
			else:
				hit = hit + 1
	number_line = number_line +1