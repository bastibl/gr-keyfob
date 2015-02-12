#!/usr/bin/env python

import md5
from revutils import *

bin_in  = "0111010100010110110101000000001101010010000001101011111000110000"
bin_out = "1101011111000101010010010010110000011101100001010100010100001010"


hex_in = bin_to_string(bin_in)

n = 0
while n < 2**64:

    if not (n % 10000): print float(n) / 2**64


    rstring = bin_to_string('{0:064b}'.format(n))

    h = md5.md5(hex_in + rstring).hexdigest()
    output = ""
    for i in range(16):
        output +=  '{0:04b}'.format(int(h[i], 16))
    if output == bin_out:
        print "yeah!"
        print n
        break

    h = md5.md5(rstring + hex_in).hexdigest()
    output = ""
    for i in range(16):
        output +=  '{0:04b}'.format(int(h[i], 16))
    if output == bin_out:
        print "yeah!"
        print n
        break

    h = md5.md5(hex_in + rstring).hexdigest()
    output = ""
    for i in range(16):
        output +=  '{0:04b}'.format(int(h[i + 16], 16))
    if output == bin_out:
        print "yeah!"
        print n
        break

    h = md5.md5(rstring + hex_in).hexdigest()
    output = ""
    for i in range(16):
        output +=  '{0:04b}'.format(int(h[i + 16], 16))
    if output == bin_out:
        print "yeah!"
        print n
        break

    n += 1
