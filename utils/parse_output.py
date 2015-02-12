#!/usr/bin/env python

import sys
import re


if(len(sys.argv) < 2):
    print "missing argument: input file"
    

output_format = "binary" # "csv" "readable" "debug" "binary"
output_base = 2
infile = sys.argv[1]

f = open(infile, "r")
lines = f.readlines()
f.close()

reg = re.compile('([a-z,0-9]{10})  ([0,1]{16})  ([a-z,0-9]{16})  ([0,1]{64})  ([0,1]{9})  ([A-Z]*)\n')
for l in lines:
    tmp = reg.match(l)
    if tmp:

        if output_format == "debug":
            print "sample: " + tmp.group(1) + "  id: " + tmp.group(2) + "  hex: " + tmp.group(3) + "  bin: " + tmp.group(4) + "  cmd: " + tmp.group(5) + "  " + tmp.group(6)

        if output_format == "csv":
            if output_base == 2:
                a = re.sub(r'([0,1])', r'\1,', tmp.group(4))[:-1]
                print a
            if output_base == 16:
                a = re.sub(r'([a-z,0-9])', r'\1,', tmp.group(3))[:-1]
                print a

        if output_format == "readable":
            if output_base == 2:
                a = re.sub(r'([0,1]{4})', r'\1 ', tmp.group(4))[:-1]
                print a
            if output_base == 16:
                a = re.sub(r'([0-9,a-z]{2})', r'\1 ', tmp.group(3))[:-1]
                print a
        if output_format == "binary":
            if output_base ==2:
                print tmp.group(4)
    else:
        print "WARNING: lines did not match -- " + l[:-1]


def next_combination(x):
    a, b = x
    if b < 63:
        return (a, b + 1)
    if a < 63:
        return (a + 1, 0)
    return None

# make binary lines
blist = []
for l in lines:
    binlist = []
    tmp = reg.match(l)
    for c in tmp.group(4):
        binlist.append(False if c == '0' else True)
    blist.append(list(binlist))


### does one bit correspond to a previous
p = (0, 0)
while p:
    works = True
    for i in range(1, len(blist)):
        if blist[i-1][p[0]] == blist[i][p[1]]:
            works = False
            break
    if works:
        print "yeah " + str(p)

    works = True
    for i in range(1, len(blist)):
        if blist[i-1][p[0]] != blist[i][p[1]]:
            works = False
            break
    if works:
        print "yeah " + str(p)

    p = next_combination(p)



### is one bit the xor'd value of a pair
p = (0, 0)
while p:
    for k in range(64):
        works = True
        for i in range(1, len(blist)):
            if (blist[i-1][p[0]] != blist[i-1][p[1]]) == blist[i][k]:
                works = False
                break
        if works:
            print "yeah " + str(p)

        works = True
        for i in range(1, len(blist)):
            if (blist[i-1][p[0]] != blist[i-1][p[1]]) != blist[i][k]:
                works = False
                break
        if works:
            print "yeah " + str(p)

    p = next_combination(p)


