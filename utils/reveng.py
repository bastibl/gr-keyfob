from subprocess import call
from revutils import *

reveng = "~/Downloads/reveng-1.2.0a/reveng"

seqs = [
    "0111010100010110110101000000001101010010000001101011111000110000",
    "1101011111000101010010010010110000011101100001010100010100001010",
    "0001010011110100111010011010010011100000011101001100110001010010"
    #"1111110011010100001101110011101100101000011100010100100101000100",
    #"0011111111110001100001011111111000110011100011001100010110101100",
    #"1000001101011110010111001101011100001111001001100000101011100101",
    #"1001010010001111010010111010000100110111000001101011000100101011",
    #"0100110011001000001001010111010010011011111001100101011101101011",
    #"0001010110000010111001001001100100000000001111010101101011000011",
    #"0010000111100100110000001001001101101101101101101011100110111101"
]

seqs = [
    "0011000010011101111000111000001000111110011001111001001010101110 00110000",
    "1001110101000100100001001001001100011111010011011100001010010110 10011101",
    "0000110010001111101010101000101000000100110111010100011000001011 00001100"
]

seqs = [
    to_diff_encoding("00011000010011101111000111000001000111110011001111001001010101110") + to_diff_encoding("000110000"),
    to_diff_encoding("01001110101000100100001001001001100011111010011011100001010010110") + to_diff_encoding("010011101"),
    to_diff_encoding("00000110010001111101010101000101000000100110111010100011000001011") + to_diff_encoding("000001100")
]

### lsb
seqstring = " ".join([change_bit_order(s) for s in seqs])
for i in range(1, 16):
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### lsb invertered
seqstring = " ".join([bin_invert(change_bit_order(s)) for s in seqs])
for i in range(1, 16):
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### crc in front lsb inverted
for i in range(1, 16):
    tmp = [bin_invert(change_bit_order(s)) for s in seqs]
    seqstring = " ".join([s[i:] + s[0:i] for s in tmp])
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### crc in front lsb
for i in range(1, 16):
    tmp = [change_bit_order(s) for s in seqs]
    seqstring = " ".join([s[i:] + s[0:i] for s in tmp])
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### crc in front inverted
for i in range(1, 16):
    seqstring = " ".join([bin_invert(s[i:] + s[0:i]) for s in seqs])
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### crc in front
for i in range(1, 16):
    seqstring = " ".join([s[i:] + s[0:i] for s in seqs])
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### normal
seqstring = " ".join(seqs)
for i in range(1, 16):
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

### inverted bit string
seqstring = " ".join([bin_invert(s) for s in seqs])
for i in range(1, 16):
    args = "-w {0:d} -a 1 -s {1:s}".format(i, seqstring)
    print args
    call(reveng + " " + args, shell=True)

