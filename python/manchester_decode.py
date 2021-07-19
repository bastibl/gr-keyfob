#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class manchester_decode(gr.basic_block):
    """
    docstring for block manchester_decode
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="manchester_decode",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte])
        self.symbol_now = False
        self.last_bit = 0 

    def general_work(self, input_items, output_items):
        i = 0
        o = 0
        while i < len(input_items[0]) and o < len(output_items[0]):
            sample = input_items[0][i]
            if sample == self.last_bit:
                self.symbol_now = False

            if self.symbol_now:
                if sample == 1:
                    output_items[0][o] = 1
                else:
                    output_items[0][o] = 0
                #print "wrote output_items[0][o] " + str(output_items[0][o])
                o += 1
            self.last_bit = sample
            self.symbol_now = not self.symbol_now
            i += 1
            
        self.consume(0, i)
        return o
