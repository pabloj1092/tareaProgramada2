#!/usr/bin/python
import sys
import math
from cache import read_c, write_c

class processor(object):
	def __init__(self):
		def read(read_index, tag, cache_name):
			tag_readed,state = cache_name.read_c(read_index)
			####### MESI PROTOCOL ########
			##### M=0, E=1, S=2, I=3 #####
			##############################
			if(tag_readed == tag and ((state == 0) or (state == 1) or (state == 2))):
				return state,'hit_local'
			else:
				return 'miss_local'

		def write(read_index, tag, state, cache_name):
			cache_name.write_c(read_index, tag, state)






