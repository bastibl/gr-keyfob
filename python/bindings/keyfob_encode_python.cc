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
/* BINDTOOL_HEADER_FILE(keyfob_encode.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(e21fbdd5bb87ab286e606411166d728e)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <keyfob/keyfob_encode.h>
// pydoc.h is automatically generated in the build directory
#include <keyfob_encode_pydoc.h>

void bind_keyfob_encode(py::module& m)
{

    using keyfob_encode    = ::gr::keyfob::keyfob_encode;


    py::class_<keyfob_encode, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<keyfob_encode>>(m, "keyfob_encode", D(keyfob_encode))

        .def(py::init(&keyfob_encode::make),
           D(keyfob_encode,make)
        )
        



        ;




}







