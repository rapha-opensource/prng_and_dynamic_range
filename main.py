#!/usr/bin/env python3.3

import random
import zlib
import matplotlib.pyplot as plt

def prng(size, dynamic_range_in_bits):
    c=0
    dynamic_range = (2**dynamic_range_in_bits) - 1
    while c<size:
        yield random.randint(0, dynamic_range)
        c+=1

#n = int.from_bytes(bytearray(prng(200, 0)), 'big')
#b = bytearray(prng(200, 3))

x = [ i for i in range(8) ]
r = []
size = 20000
for i in range(8):
    b = bytearray(prng(size, i))
    r.append( 100*len(zlib.compress(b,9))/size )

print(x)
print(r)
plt.plot(r, 'ro')
plt.show()
