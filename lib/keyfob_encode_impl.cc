/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "keyfob_encode_impl.h"

#include <algorithm>

namespace gr {
  namespace keyfob {

    keyfob_encode::sptr
    keyfob_encode::make()
    {
      return gnuradio::get_initial_sptr
        (new keyfob_encode_impl());
    }

    keyfob_encode_impl::keyfob_encode_impl()
      : gr::sync_block("keyfob_encode",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(uint8_t))),
        index(0)
    {
        message_port_register_in(pmt::mp("in"));
        set_msg_handler(pmt::mp("in"), boost::bind(&keyfob_encode_impl::in, this, boost::placeholders::_1));
    }

    keyfob_encode_impl::~keyfob_encode_impl()
    {
    }

    void keyfob_encode_impl::in(pmt::pmt_t msg) {

        if(pmt::is_symbol(msg)) {
            str = pmt::symbol_to_string(msg);

        } else if(pmt::is_pair(msg)) {
            str = std::string(reinterpret_cast<const char *>(pmt::blob_data(pmt::cdr(msg))), pmt::blob_length(pmt::cdr(msg)));

        } else {
            std::cout << "keyfob_encode: expecting PDU or string" << std::endl;
            return;
        }

        str.erase(std::remove(str.begin(), str.end(), ' '), str.end());
        str.erase(std::remove(str.begin(), str.end(), '\n'), str.end());

        if(str.length() != 64 + 9) {
            std::cout << "keyfob_encode: input string has to span 64 + 9 characters" << std::endl;;
            return;
        }


        std::string preamble = "000000000000000000000000001010100001110001100000000";
        str.insert(0, preamble);

        index = 0;
    }

    int
    keyfob_encode_impl::work(int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items)
    {
        uint8_t *out = (uint8_t *) output_items[0];

        int samples = std::min(noutput_items, int(str.length() - index));

        for(int i = 0; i < samples; i++) {
            if(str[index] == '0') {
                *out = 0;
            } else {
                *out = 1;
            }
            out++;
            index++;
        }

        return samples;
    }

  } /* namespace keyfob */
} /* namespace gr */

