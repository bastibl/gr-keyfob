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


#ifndef INCLUDED_KEYFOB_KEYFOB_ENCODE_H
#define INCLUDED_KEYFOB_KEYFOB_ENCODE_H

#include <gnuradio/sync_block.h>
#include <keyfob/api.h>

namespace gr {
namespace keyfob {

/*!
 * \brief <+description of block+>
 * \ingroup keyfob
 *
 */
class KEYFOB_API keyfob_encode : virtual public gr::sync_block
{
public:
    typedef std::shared_ptr<keyfob_encode> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of keyfob::keyfob_encode.
     *
     * To avoid accidental use of raw pointers, keyfob::keyfob_encode's
     * constructor is in a private implementation
     * class. keyfob::keyfob_encode::make is the public interface for
     * creating new instances.
     */
    static sptr make();
};

} // namespace keyfob
} // namespace gr

#endif /* INCLUDED_KEYFOB_KEYFOB_ENCODE_H */
