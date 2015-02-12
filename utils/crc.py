#!/usr/bin/env python

from revutils import *
import crcmod

crcs =  [0x1D5, 0x1AB, 0x1EA, 0x107, 0x1E0, 0x183, 0x131, 0x18C, 0x198, 0x11D, 0x1B8, 0x18E, 0x19B, 0x1D9, 0x1CD]

crcs = [0x12F15,  0x1A8F4,  0x1978B, 0x1A02B,  0x1D405,  0x1D015, 0x11021,  0x18408,  0x18810, 0x1C867,  0x1E613,  0x1E433, 0x10589,  0x191A0,  0x182C4, 0x18BB7,  0x1EDD1,  0x1C5DB, 0x13D65,  0x1A6BC,  0x19EB2, 0x18005,  0x1A001,  0x1C002]

seqs = [
    "0110111111001100110000001110001110011111010001000001011000111010",
    "1000101011101001001010111111110010101101111110010100000111001111",
    "1101011111000101010010010010110000011101100001010100010100001010",
    "0100110011001000001001010111010010011011111001100101011101101011",
    "1001010010001111010010111010000100110111000001101011000100101011",
    "0011111111110001100001011111111000110011100011001100010110101100"
]

s1 = bin_to_string(seqs[0][0:48])
o1 = bin_to_int(seqs[0][48:64])

#for seq in seqs:
#    string = hex(bin_to_int(seq))[:-1]
#    n = 0
#    for i in range(2, len(string)):
#        n ^= int(string[i], 16)
#    print "{0:04b}".format(n)
#assert(False)

for seq in seqs:
    string = hex(bin_to_int(seq))[:-1]
    n = 0
    for i in range(2, len(string), 2):
        n ^= int(string[i:i+2], 16)
    print "{0:08b}".format(n)
assert(False)

#print "S1 " + "".join([hex(ord(s)) for s in s1]) + "   " + o1
print "o1        " + "{0:#x}".format(o1)
print "----------------"

for crc in crcs:
    c = crcmod.mkCrcFun(crc, rev=True, xorOut=0xFFFF)
    print "{0:#x}   {1:#x}".format(crc, c(s1))
    c = crcmod.mkCrcFun(crc, rev=True, initCrc=0, xorOut=0xFFFF)
    print "{0:#x}   {1:#x}".format(crc, c(s1))
    c = crcmod.mkCrcFun(crc, rev=True, xorOut=0)
    print "{0:#x}   {1:#x}".format(crc, c(s1))

    c = crcmod.mkCrcFun(crc, rev=False, xorOut=0xFFFF)
    print "{0:#x}   {1:#x}".format(crc, c(s1))
    c = crcmod.mkCrcFun(crc, rev=False, initCrc=0, xorOut=0xFFFF)
    print "{0:#x}   {1:#x}".format(crc, c(s1))
    c = crcmod.mkCrcFun(crc, rev=False, xorOut=0)
    print "{0:#x}   {1:#x}".format(crc, c(s1))
