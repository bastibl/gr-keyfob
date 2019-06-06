# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of gr-keyfob
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

list(APPEND keyfob_sources
    parse_packet_impl.cc
    keyfob_encode_impl.cc
)

set(keyfob_sources "${keyfob_sources}" PARENT_SCOPE)
if(NOT keyfob_sources)
    MESSAGE(STATUS "No C++ sources... skipping lib/")
    return()
endif(NOT keyfob_sources)

add_library(gnuradio-keyfob SHARED ${keyfob_sources})
target_link_libraries(gnuradio-keyfob gnuradio::gnuradio-runtime)
target_include_directories(gnuradio-keyfob
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>
    PUBLIC $<INSTALL_INTERFACE:include>
  )
set_target_properties(gnuradio-keyfob PROPERTIES DEFINE_SYMBOL "gnuradio_keyfob_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-keyfob PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-keyfob)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

# If your unit tests require special include paths, add them here
#include_directories()
# List all files that contain Boost.UTF unit tests here
list(APPEND test_keyfob_sources
)
