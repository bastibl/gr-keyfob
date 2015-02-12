import re
import unittest

def to_diff_encoding(s):
    tmp = re.match(r'[01]+', s)
    if not tmp or tmp.group(0) != s:
        raise ValueError

    ret = ""
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            ret += "1"
        else:
            ret += "0"
    return ret

def bin_to_string(s, msb=True):
    if len(s) % 8:
        raise ValueError

    ret = ""
    for i in range(len(s) / 8):
        binary = s[i * 8: ((i + 1) * 8)]
        if msb:
            ret +=  chr(int(binary, 2))
        else:
            ret +=  chr(int(binary[::-1], 2))

    return ret


def bin_invert(s):
    tmp = re.match(r'[01]+', s)
    if not tmp or tmp.group(0) != s:
        raise ValueError

    ret = s
    ret = ret.replace("0", "X")
    ret = ret.replace("1", "0")
    ret = ret.replace("X", "1")
    return ret


def bin_to_int(s, msb=True):
    tmp = re.match(r'[01]+', s)
    if not tmp or tmp.group(0) != s:
        raise ValueError

    ret = 0
    for i in range(len(s)):
        if msb:
            ret += int(s[i]) * 2**(len(s) - i - 1)
        else:
            ret += int(s[i]) * 2**i
    return ret

def is_bit_group(s):
    tmp = re.match("^0*1*0*$", s)
    if tmp: return True

    tmp = re.match("^1*0*1*$", s)
    if tmp: return True

    return False


def change_bit_order(s):
    tmp = re.match(r'[01]+', s)
    if not tmp or tmp.group(0) != s:
        raise ValueError
    if len(s) % 8:
        raise ValueError

    ret = ""
    for i in range(len(s) / 8):
        binary = s[i * 8: ((i + 1) * 8)]
        ret +=  binary[::-1]

    return ret

class TestFunctions(unittest.TestCase):

    def test_bin_to_string(self):
        ### wrong characters
        binary = "01234567"
        self.assertRaises(ValueError, bin_to_string, binary)

        ### not multiple of 8 characters
        binary = "0" * 7
        self.assertRaises(ValueError, bin_to_string, binary)

        ### conversion
        binary = "0" * 8 + "1" * 8
        self.assertEqual("\x00\xff", bin_to_string(binary))

        ### conversion
        binary = "0101" + "1100" + "1010" + "1111"
        self.assertEqual("\x5c\xaf", bin_to_string(binary))

        ### conversion LSB
        binary = "0101" + "1100" + "1010" + "1111"
        self.assertEqual("\x3a\xf5", bin_to_string(binary, msb=False))
        
    def test_bin_invert(self):
        ### wrong characters
        binary = "017"
        self.assertRaises(ValueError, bin_invert, binary)
        binary = ""
        self.assertRaises(ValueError, bin_invert, binary)

        ### conversion
        binary = "00001111"
        self.assertEqual("11110000", bin_invert(binary))
        binary = "10101100"
        self.assertEqual("01010011", bin_invert(binary))

    def test_bin_to_int(self):
        ### wrong characters
        binary = "017"
        self.assertRaises(ValueError, bin_to_int, binary)
        binary = ""
        self.assertRaises(ValueError, bin_to_int, binary)

        ### conversion
        binary = "0011"
        self.assertEqual( 3, bin_to_int(binary))
        binary = "1010"
        self.assertEqual(10, bin_to_int(binary))
        binary = "1"
        self.assertEqual( 1, bin_to_int(binary))
        binary = "0"
        self.assertEqual( 0, bin_to_int(binary))

        ### conversion LSB
        binary = "0011"
        self.assertEqual(12, bin_to_int(binary, msb=False))
        binary = "1010"
        self.assertEqual( 5, bin_to_int(binary, msb=False))
        binary = "1"
        self.assertEqual( 1, bin_to_int(binary, msb=False))
        binary = "0"
        self.assertEqual( 0, bin_to_int(binary, msb=False))

    def test_change_bit_order(self):
        ### wrong characters
        binary = "017"
        self.assertRaises(ValueError, change_bit_order, binary)
        binary = ""
        self.assertRaises(ValueError, change_bit_order, binary)
        
        ### conversion
        binary = "00111010"
        self.assertEqual("01011100", change_bit_order(binary))
        binary = "11110000"
        self.assertEqual("00001111", change_bit_order(binary))
        binary = "1111000011110000"
        self.assertEqual("0000111100001111", change_bit_order(binary))

    def test_is_bit_group(self):
        binary = "0000111000"
        self.assertTrue(is_bit_group(binary))
        binary = "1000111000"
        self.assertFalse(is_bit_group(binary))
        binary = "1110000111"
        self.assertTrue(is_bit_group(binary))
        binary = "0000111"
        self.assertTrue(is_bit_group(binary))
        binary = "11110000"
        self.assertTrue(is_bit_group(binary))
        binary = "11110010"
        self.assertFalse(is_bit_group(binary))

    def test_to_diff_encoding(self):
        binary = "11"
        self.assertEqual("0", to_diff_encoding(binary))
        binary = "00"
        self.assertEqual("0", to_diff_encoding(binary))
        binary = "10"
        self.assertEqual("1", to_diff_encoding(binary))
        binary = "01"
        self.assertEqual("1", to_diff_encoding(binary))
        binary = "1001101"
        self.assertEqual("101011", to_diff_encoding(binary))


if __name__ == "__main__":
    unittest.main()

