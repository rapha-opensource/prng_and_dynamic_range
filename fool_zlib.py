#!/usr/bin/env python3.3

import random
import zlib
import matplotlib.pyplot as plt

# make a bytearray line with random data with n*kB
# copy the line 10 times
# compress
# shows that if line size is greater than zlib's compressor windows (default 32kB)
# then we get no compression at all

def prng(size, dynamic_range_in_bits):
	c=0
	dynamic_range = (2**dynamic_range_in_bits) - 1
	while c<size:
		yield random.randint(0, dynamic_range)
		c+=1

x = []
r = []
line_size = 4 # kB
kB = 1024
for i in range(6):
	b = bytearray(prng(line_size*kB, 8))
	for j in range(10):
		b.extend(b)
	x.append( line_size )
	r.append( 100*len(zlib.compress(b,9))/float(len(b)) )
	line_size *= 2

print(x)
print(r)
plt.plot(x, r, 'ro')
plt.axis([0, 128, 0, 110])
plt.show()

