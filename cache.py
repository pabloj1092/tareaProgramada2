#! /usr/bin/python
import sys
import math

class Cache(object):
	def __init__(self, c_size):
		self.c_size = int(c_size) * 1024
		b_size = 16

		if((c_size & (c_size -1)) != 0):
	    	print "Invalid cache size, use a base 2 number"
	    	sys.exit()

    	if((b_size & (b_size -1)) != 0):
	    	print "Invalid block size, use a base 2 number"
	    	sys.exit()	

	    b_num = c_size/b_size	
	    cache = [[0 for x in range(b_num)] for x in range(0,2)]

		def read_c(read_index):
			data_cache = cache[read_index][0]
			state_c = cache[read_index][1]
			return data_cache,state_c

		def write_c(read_index, tag, state_c):
			cache[read_index][0] = tag
			cache[read_index][1] = state_c