#! /usr/bin/python

class Cache(object):
	def __init__(c_size):
		self.c_size = int(c_size)
		b_size = 16

		if((c_size & (c_size -1)) != 0):
	    	print "Invalid cache size, use a base 2 number"
	    	sys.exit()

    	if((b_size & (b_size -1)) != 0):
	    	print "Invalid block size, use a base 2 number"
	    	sys.exit()	

	    b_num = c_size/b_size	
	    cache = [[0 for x in range(b_num)] for x in range(0,2)]

	    offset = int(math.log(float(b_size),2))
    	index = int(math.log(float(sets),2))
    	hit_local = 0
    	miss_local = 0

		def read(tag, read_index):
			for way in range(b_num):
				if(cache[read_index][0] == tag && (cache[read_index][1] == M || cache[read_index][1] == E || cache[read_index][1] == S))
					hit_local = hit_local + 1
					break
				elif (way == b_num-1 || (cache[read_index][0] == tag && cache[read_index][1] == I]))
					miss_local = miss_local + 1
					#Implementar leer de otra cache

		def write(self):
			for way in range(b_num):
				if(cache[read_index][0] == tag && cache[read_index][1] == M)
					
