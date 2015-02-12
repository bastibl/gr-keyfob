#!/usr/bin/env python

from revutils import *
from Crypto.Cipher import DES

bin1 = "0111111110001011111011110101110010101111101011101011101010100011"
bin2 = "0111111110001011111011110101110010101111101011101011101010111101"

hex1 = bin_to_string(bin1)
hex2 = bin_to_string(bin2)

key = "".join([chr(2*ord(c)) for c in "secret!!"])
print key
print " ".join(hex(ord(c)) for c in key)

cipher = DES.new(key, DES.MODE_ECB)
d1 = cipher.encrypt(hex1)
d2 = cipher.encrypt(hex2)
n1 = "".join(["0x{0:02x}, ".format(ord(x)) for x in d1])
n2 = "".join(["0x{0:02x}, ".format(ord(x)) for x in d2])

print "static char seq1[8] = {" + n1
print "static char seq2[8] = {" + n2


tmp = " ".join(str(ord(c)) for c in "secret!!")
print tmp



