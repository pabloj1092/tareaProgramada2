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
		b_num = self.c_size/b_size
		self.cache = [[0, 'I'] for x in range(b_num)]

	def read_c(self, read_index):
		data_cache = self.cache[read_index][0]
		state_c = self.cache[read_index][1]
		return data_cache,state_c
	def write_c(self, read_index, tag, state_c):
		self.cache[read_index][0] = tag
		self.cache[read_index][1] = state_c