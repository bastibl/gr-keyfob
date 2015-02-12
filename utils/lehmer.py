#!/usr/bin/env python

import math
import md5
import sys

def code_from_int(size, num):
    code = []
    for i in range(size):
        num, j = divmod(num, size - i)
        code.append(j)
 
    return code

def perm_from_code(base, code):
    perm = list(base)
    for i in range(len(base) - 1):
        j = code[i]
        perm[i], perm[i+j] = perm[i+j], perm[i]
 
    return perm
 
def perm_from_int(base, num):
    code = code_from_int(len(base), num)
    return perm_from_code(base, code)

def bin_to_hex_string(s):
    assert(len(s) == 64)

    ret = ""
    for i in range(8):
        ret +=  chr(int(s[i * 8:((i+1)*8)], 2))
    return ret



bin_in  = "0111010100010110110101000000001101010010000001101011111000110000"
bin_out = "1101011111000101010010010010110000011101100001010100010100001010"

inlist = [x for x in bin_in]
output = bin_to_hex_string(bin_out)

n = 0
while n < 2**64:
    if not (n % 10000): print float(n) / 2**64
    s = perm_from_int(inlist, n)
    s = "".join(s)
    s = bin_to_hex_string(s)
    
    h = md5.md5(s).hexdigest()
    if output == h:
        print "yeah!"
        print n
        break

    n += 1
