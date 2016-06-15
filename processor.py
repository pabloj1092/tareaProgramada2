#!/usr/bin/python
import sys
import math
import cache
from cache import Cache

class processor(object):
	# def __init__(self):

	def read_p(self, read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3):
		tag_readed,state = cache_m.read_c(read_index)
		tag_readed_s,state_s = cache_s.read_c(read_index)
		tag_readedL3,state_L3 = cacheL3.read_c(read_indexL3)
		####### MESI PROTOCOL ########
		##### M=0, E=1, S=2, I=3 #####
		##############################
		if(tag_readed == tag and ((state == 0) or (state == 1) or (state == 2))):
			return 'hit_local','hit_global', state
		elif(tag_readed == tag and state == 3):
			if(tag_readed_s == tag and ((state_s == 0) or (state_s == 1) or (state_s == 2))):
				cache_m[read_index][0] = tag_readed_s
				cache_m[read_index][1] = 2
				cache_s[read_index][1] = 2
				state = 2
				return 'miss_local','hit_global', state
			else:
				if(tag_readedL3 == tagL3 and ((state_L3 == 0) or (state_L3 == 1) or (state_L3 == 2))):
					cache_m[read_index][0] = tag
					cache_m[read_index][1] = 1
					cacheL3[read_indexL3][1] = 1
					state = 1
					return 'miss_local','hit_global', state
				else:
					cache_m[read_index][0] = tag
					cache_m[read_index][1] = 1
					cacheL3[read_indexL3][0] = tagL3
					cacheL3[read_indexL3][1] = 1
					state = 1
					return 'miss_local', 'miss_global', state
		else:
			if(tag_readedL3 == tagL3 and ((state_L3 == 0) or (state_L3 == 1) or (state_L3 == 2))):
					cache_m[read_index][0] = tag
					cache_m[read_index][1] = 1
					cacheL3[read_indexL3][1] = 1
					state = 1
					return 'miss_local', 'hit_global', state
			else:
				cache_m[read_index][0] = tag
				cache_m[read_index][1] = 1
				cacheL3[read_indexL3][0] = tagL3
				cacheL3[read_indexL3][1] = 1
				state = 1
				return 'miss_local', 'miss_global', state

	def write_p(self, read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3):
		local,glob,state = self.read_p(read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3)
		if(state == 0):
			cache_m.write_c(read_index, tag, 0)
		elif(state == 1):
			cache_m.write_c(read_index, tag, 0)
			cacheL3.write_c(read_indexL3, tagL3, 3)
		else: #(state == 2):
			cache_m.write_c(read_index, tag, 0)
			cache_s.write_c(read_index, tag, 3)
			cacheL3.write_c(read_indexL3, tagL3, 3)
		return local,glob,state
