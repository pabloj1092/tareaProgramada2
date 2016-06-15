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
		if(tag_readed == tag and ((state == 'M') or (state == 'E') or (state == 'S'))): #Hit in local cache
			return 'hit_local','hit_global', state
		#elif(tag_readed == tag and state == 'I'): 
		else: #Miss in local cache
			if(tag_readed_s == tag and ((state_s == 'M') or (state_s == 'E') or (state_s == 'S'))): #Hit in parallel cache
				cache_m.cache[read_index][0] = tag_readed_s
				cache_m.cache[read_index][1] = 'S'
				cache_s.cache[read_index][1] = 'S'
				state = 'S'
				return 'miss_local','hit_global', state
			else: #Miss in parallel cache
				if(tag_readedL3 == tagL3 and ((state_L3 == 'M') or (state_L3 == 'E') or (state_L3 == 'S'))): #Hit in L3 cache
					cache_m.cache[read_index][0] = tag
					cache_m.cache[read_index][1] = 'E'
					cacheL3.cache[read_indexL3][1] = 'E'
					state = 'E'
					return 'miss_local','hit_global', state
				else: #Miss in L3 cache
					cache_m.cache[read_index][0] = tag
					cache_m.cache[read_index][1] = 'E'
					cacheL3.cache[read_indexL3][0] = tagL3
					cacheL3.cache[read_indexL3][1] = 'E'
					state = 'E'
					return 'miss_local', 'miss_global', state
		'''
		else:
			if(tag_readedL3 == tagL3 and ((state_L3 == 'M') or (state_L3 == 'E') or (state_L3 == 'S'))):
					cache_m[read_index][0] = tag
					cache_m[read_index][1] = 'E'
					cacheL3[read_indexL3][1] = 'E'
					state = 'E'
					return 'miss_local', 'hit_global', state
			else:
				cache_m[read_index][0] = tag
				cache_m[read_index][1] = 'E'
				cacheL3[read_indexL3][0] = tagL3
				cacheL3[read_indexL3][1] = 'E'
				state = 'E'
				return 'miss_local', 'miss_global', state
		'''

	def write_p(self, read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3):
		local,glob,state = self.read_p(read_index, tag, read_indexL3, tagL3, cache_m, cache_s, cacheL3)
		if(state == 'M'):
			cache_m.write_c(read_index, tag, 'M')
		elif(state == 'E'):
			cache_m.write_c(read_index, tag, 'M')
			cacheL3.write_c(read_indexL3, tagL3, 'I')
		else:
			cache_m.write_c(read_index, tag, 'M')
			cache_s.write_c(read_index, tag, 'I')
			cacheL3.write_c(read_index, tag, 'I')
		return local,glob,state