/*
 * Copyright 2021 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(parse_packet.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(eced159df2a648081d326db9a47d4013)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <keyfob/parse_packet.h>
// pydoc.h is automatically generated in the build directory
#include <parse_packet_pydoc.h>

void bind_parse_packet(py::module& m)
{

    using parse_packet    = ::gr::keyfob::parse_packet;


    py::class_<parse_packet, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<parse_packet>>(m, "parse_packet", D(parse_packet))

        .def(py::init(&parse_packet::make),
           D(parse_packet,make)
        )
        



        ;




}








