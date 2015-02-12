#!/usr/bin/env python

import sys

f = open("~/bits.bin", 'rb')

try:
	byte = f.read(1)
	while byte != "":
		sys.stdout.write(str(ord(byte)))
		byte = f.read(1)

finally:
	f.close()

print

