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
#include "parse_packet_impl.h"

namespace gr {
  namespace keyfob {

    parse_packet::sptr
    parse_packet::make()
    {
      return gnuradio::get_initial_sptr
        (new parse_packet_impl());
    }

    parse_packet_impl::parse_packet_impl()
      : gr::sync_block("parse_packet",
              gr::io_signature::make(1, 1, sizeof(uint8_t)),
              gr::io_signature::make(0, 0, 0))
    {}

    void
    parse_packet_impl::forecast(int noutput_items, gr_vector_int &ninput_items_required) {
      ninput_items_required[0] = 104;
    }

    parse_packet_impl::~parse_packet_impl()
    {
    }

    bool
    parse_packet_impl::match(const uint8_t *in, uint8_t *seq, size_t len) {
      for(int i = 0; i < len; i++) {
        if(in[i] != seq[i]) {
          return false;
        }
      }
      return true;
    }

    packet_type_t
    parse_packet_impl::get_type(const uint8_t *in) {
      static uint8_t head_data[]  = {0, 1, 1, 1, 0, 0, 0, 1};
      static uint8_t head_short[] = {1, 1, 1, 1, 0, 0, 0, 1};
      static uint8_t tail_close[] = {0, 0, 1, 0, 1, 0, 1, 0};
      static uint8_t tail_open[]  = {0, 0, 0, 1, 1, 1, 0, 0};
      static uint8_t tail_trunk[] = {0, 1, 0, 0, 0, 1, 1, 0};
      static uint8_t tail_short[] = {0, 0, 0, 1, 1, 1, 0, 0};

      if(match(in, head_data, 8)) {
        if(match(in + 81, tail_close, 8)) {
          return DATA_CLOSE;
        } else if(match(in + 81, tail_open, 8)) {
          return DATA_OPEN;
        } else if(match(in + 81, tail_trunk, 8)) {
          return DATA_TRUNK;
        }
      } else if(match(in, head_short, 8)) {
        if(match(in + 25, tail_close, 8)) {
          return SHORT_CLOSE;
        } else if(match(in + 25, tail_open, 8)) {
          return SHORT_OPEN;
        } else if(match(in + 25, tail_trunk, 8)) {
          return SHORT_TRUNK;
        }
      }

      return PACKET_UNKNOWN;
    }

    void
    parse_packet_impl::parse_long(const uint8_t *in, packet_type_t type) {
      std::cout << std::setfill('0') << std::setw(10) << nitems_read(0) << "  ";

      // binary access code
      for(int i = 0; i < 17; i++) {
        if(in[i]) std::cout << "1";
        else std::cout << "0";
      }

      std::cout << "  ";

      // hex data
      uint8_t d = 0;
      for(int i = 0; i < 64; i++) {
        d |= in[i + 17] << (3 - (i % 4));
        if((i % 4) == 3) {
          std::cout << std::hex << (int)d;
          d = 0;
        }
      }

      std::cout << "  ";

      // binary data
      for(int i = 17; i < 81; i++) {
        if(in[i]) std::cout << "1";
        else std::cout << "0";
      }

      std::cout << "  ";

      // binary data
      for(int i = 81; i < 89; i++) {
        if(in[i]) std::cout << "1";
        else std::cout << "0";
      }

      std::cout << "  ";

      switch(type) {
      case DATA_OPEN:
        std::cout << "OPEN";
        break;
      case DATA_CLOSE:
        std::cout << "CLOSE";
        break;
      case DATA_TRUNK:
        std::cout << "TRUNK";
        break;
      default:
        break;
      }

      std::cout << std::endl;
    }

    void
    parse_packet_impl::parse_short(const uint8_t *in, packet_type_t type) {
      std::cout << std::setfill('0') << std::setw(10) << nitems_read(0) << "  ";

      // binary data
      for(int i = 0; i < 25; i++) {
        if(in[i]) std::cout << "1";
        else std::cout << "0";
      }

      std::cout << "  ";

      // binary data
      for(int i = 25; i < 33; i++) {
        if(in[i]) std::cout << "1";
        else std::cout << "0";
      }

      std::cout << "  ";

      switch(type) {
      case SHORT_OPEN:
        std::cout << "SHORT OPEN";
        break;
      case SHORT_CLOSE:
        std::cout << "SHORT CLOSE";
        break;
      case SHORT_TRUNK:
        std::cout << "SHORT TRUNK";
        break;
      default:
        break;
      }
      std::cout << std::endl;
    }

    int
    parse_packet_impl::work(int noutput,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const uint8_t *in = (const uint8_t*)input_items[0];

      // get tags
      const uint64_t samp0_count = nitems_read(0);
      get_tags_in_range(d_tags, 0, samp0_count, samp0_count + noutput, pmt::mp("packet_start"));

      // no tags -> no frame
      if(d_tags.empty()) return noutput;

      // check if frame starts at sample 0
      std::sort(d_tags.begin(), d_tags.end(), tag_t::offset_compare);
      uint64_t off = d_tags[0].offset;
      if(off != samp0_count) return off - samp0_count;

      // check for enough input data
      if(noutput < 104) return 0;

      long long unsigned int packet_size = 104;
      packet_type_t type = get_type(in);
      if(type == DATA_OPEN ||
          type == DATA_CLOSE ||
          type == DATA_TRUNK) {
        parse_long(in, type); 
        packet_size = 89;
      } else if(type == SHORT_OPEN ||
          type == SHORT_CLOSE ||
          type == SHORT_TRUNK) {
        parse_short(in, type);
        packet_size = 33;
      }

      if(d_tags.size() > 1) {
        return std::min((unsigned long long)d_tags[1].offset - samp0_count, packet_size);
      }
      return packet_size;
    }

  } /* namespace keyfob */
} /* namespace gr */

