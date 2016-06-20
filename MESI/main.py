#!/usr/bin/python

import sys
import math
from processor import processor
from cache import Cache
file1 = open('log_p1', 'w')
file2 = open('log_p2', 'w')

#Processors 1 and 2
P1 = processor()
P2 = processor()

#Cache L1 to P1, L2 to P2 and L3 shared
b_size = 16
L_size = 8*1024
L3_size = 64*1024
L1 = Cache(8)
L2 = Cache(8)
L3 = Cache(64)

index = int(math.log(float(L_size/b_size),2))
indexL3 = int(math.log(float(L3_size/b_size),2))

mask = 0
maskL3 = 0

for i in range(index):
	mask = 1 + mask*2

for x in range(indexL3):
	maskL3 = 1  + maskL3*2

line_number = 1

file = open('aligned.trace', 'r')
for line in file:
	row = line.split()
	data, instruction = row
	tag = int(row[0], 16) #still not the 
	read_index = tag & mask
	for i in range (index):
		tag = (tag / 2) #now we have only the tag in $tag
	tagL3 = int(data[0], 16) #still not the tag
	read_indexL3 = tagL3 & maskL3     #extract the index
	for k in range (indexL3): #delete the index from the read
		tagL3 = (tagL3 / 2) #now we have only the tag in $tag
	if(line_number%2 == 0):
		if(instruction == 'L'):
			local,other,state = P2.read_p(read_index, tag, read_indexL3, tagL3, L2, L1, L3)
		else:
			local,other,state = P2.write_p(read_index, tag, read_indexL3, tagL3, L2, L1, L3)

		if(line_number >= 980):
			state_cache1 = L1.cache[read_index][1]
			state_cache2 = L2.cache[read_index][1]
			file2.write("Processor1: " + state_cache1 + " " + "Processor2: " + state_cache2 + " " + str(line_number))
			file2.write("\n")
	else:
		if(instruction == 'L'):
			local,other,state = P1.read_p(read_index, tag, read_indexL3, tagL3, L1, L2, L3)
		else:
			local,other,state = P1.write_p(read_index, tag, read_indexL3, tagL3, L1, L2, L3)
		if(line_number >= 980):
			state_cache1 = L1.cache[read_index][1]
			state_cache2 = L2.cache[read_index][1]
			file1.write("Processor1: " + state_cache1 + " " + "Processor2: " + state_cache2 + " " + str(line_number))
			file1.write("\n")
	line_number = line_number + 1
print line_number
file1.close()
file2.close()