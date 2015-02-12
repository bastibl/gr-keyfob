/* -*- c++ -*- */

#define KEYFOB_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "keyfob_swig_doc.i"

%{
#include "keyfob/parse_packet.h"
#include "keyfob/keyfob_encode.h"
%}


%include "keyfob/parse_packet.h"
GR_SWIG_BLOCK_MAGIC2(keyfob, parse_packet);
%include "keyfob/keyfob_encode.h"
GR_SWIG_BLOCK_MAGIC2(keyfob, keyfob_encode);
