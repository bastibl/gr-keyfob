# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT keyfob_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT keyfob_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND keyfob_python_files
    keyfob_encode_python.cc
    parse_packet_python.cc
    python_bindings.cc
    )

GR_PYBIND_MAKE_OOT(keyfob 
   ../..
   gr::keyfob
   "${keyfob_python_files}")

install(TARGETS keyfob_python DESTINATION ${GR_PYTHON_DIR}/keyfob COMPONENT pythonapi)
