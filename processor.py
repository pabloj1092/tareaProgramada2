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
		if((tag_readed == tag) and ((state == 'M') or (state == 'E') or (state == 'S'))): #Hit in local cache
			return 'hit_local','N/A', state
		#elif(tag_readed == tag and state == 'I'): 
		else: #Search in the other processor cache
			if((tag_readed_s == tag) and ((state_s == 'M') or (state_s == 'E') or (state_s == 'S'))): #Hit in parallel cache
				cache_m.write_c(read_index, tag, 'S')
				cache_s.write_c(read_index, tag, 'S')
				state = 'S'
				return 'miss_local','hit_s', state
			else: #Search in L3 cache
				if((tag_readedL3 == tagL3) and ((state_L3 == 'M') or (state_L3 == 'E') or (state_L3 == 'S'))): #Hit in L3 cache
					cache_m.write_c(read_index, tag,  'E')
					cache_s.write_c(read_index, tag, 'I')
					cacheL3.write_c(read_indexL3, tagL3, 'E')
					state = 'E'
					return 'miss_local','hit_L3', state
				else: #Miss in L3 cache
					cache_m.write_c(read_index, tag, 'E')
					cache_s.write_c(read_index, tag, 'I')
					cacheL3.write_c(read_indexL3, tagL3, 'E')
					
					state = 'E'
					return 'miss_local', 'miss_L3', state

	def write_p(self, read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3):
		local,other,state = self.read_p(read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3)
		if(state == 'M'):
			cache_m.write_c(read_index, tag, 'M')
		elif(state == 'E'):
			cache_m.write_c(read_index, tag, 'M')
			cache_s.write_c(read_index, tag, 'I')
			cacheL3.write_c(read_indexL3, tagL3, 'I')
		elif(state == 'S'):
			cache_m.write_c(read_index, tag, 'M')
			cache_s.write_c(read_index, tag, 'I')
			cacheL3.write_c(read_indexL3, tagL3, 'I')
		return local,other,state