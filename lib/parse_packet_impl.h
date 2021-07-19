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

#ifndef INCLUDED_KEYFOB_PARSE_PACKET_IMPL_H
#define INCLUDED_KEYFOB_PARSE_PACKET_IMPL_H

#include <keyfob/parse_packet.h>

namespace gr {
namespace keyfob {

enum packet_type_t {
    DATA_OPEN,
    DATA_CLOSE,
    DATA_TRUNK,
    SHORT_OPEN,
    SHORT_CLOSE,
    SHORT_TRUNK,
    PACKET_UNKNOWN
};

class parse_packet_impl : public parse_packet
{
private:
    std::vector<tag_t> d_tags;
    packet_type_t get_type(const uint8_t* in);
    void parse_long(const uint8_t* in, packet_type_t type);
    void parse_short(const uint8_t* in, packet_type_t type);
    bool match(const uint8_t* in, uint8_t* seq, size_t len);

public:
    parse_packet_impl();
    ~parse_packet_impl();

    // Where all the action really happens
    int work(int noutput_items,
             gr_vector_const_void_star& input_items,
             gr_vector_void_star& output_items);
    void forecast(int noutput_items, gr_vector_int& ninput_items_required);
};

} // namespace keyfob
} // namespace gr

#endif /* INCLUDED_KEYFOB_PARSE_PACKET_IMPL_H */
