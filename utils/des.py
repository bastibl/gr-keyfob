#!/usr/bin/env python

from subprocess import call
from revutils import *
import random
from Crypto.Cipher import DES

def key_to_hex(s):
    keystring = "{0:056b}".format(s)
    string = ""
    for i in range(8):
        string += chr(int(keystring[i*7:((i+1)*7)], 2))
    return string

bin1 = "0111111110001011111011110101110010101111101011101011101010100011"
bin2 = "1110101100111100100110000010000111101001010011110000111100010100"

hex1 = bin_to_string(bin1)
hex2 = bin_to_string(bin2)

hex1_inv = bin_to_string(bin_invert(bin1))
hex2_inv = bin_to_string(bin_invert(bin2))

while True:
    key = random.randint(0, 2**56 - 1)
    if not key % 10000: print float(key) / 2**56

    cipher = DES.new(key_to_hex(key), DES.MODE_ECB)
    d1 = cipher.decrypt(hex1)
    d2 = cipher.decrypt(hex2)
    n1 = "".join(["{0:08b}".format(ord(x)) for x in d1])
    n2 = "".join(["{0:08b}".format(ord(x)) for x in d2])

    xor = int(n1, 2) ^ int(n2, 2)
    if is_bit_group(bin(xor)):
        print "YEAH NORMAL"
        print key
        print n1
        print n2
        call("echo \"found something\n " + str(key) + "\n" + n1 + "\n" + n2 + "\" | mutt -s \"found something\" bloessl@ccs-labs.org", shell=True)

    cipher = DES.new(key_to_hex(key), DES.MODE_ECB)
    d1 = cipher.decrypt(hex1_inv)
    d2 = cipher.decrypt(hex2_inv)
    n1 = "".join(["{0:08b}".format(ord(x)) for x in d1])
    n2 = "".join(["{0:08b}".format(ord(x)) for x in d2])

    xor = int(n1, 2) ^ int(n2, 2)
    if is_bit_group(bin(xor)):
        print "YEAH INVERTED"
        print key
        print n1
        print n2
        call("echo \"found something\n " + str(key) + "\n" + n1 + "\n" + n2 + "\" | mutt -s \"found something\" bloessl@ccs-labs.org", shell=True)


