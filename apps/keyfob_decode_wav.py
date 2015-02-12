#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Keyfob Decode Wav
# Generated: Tue Jun 23 11:31:31 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import keyfob
import wx

class keyfob_decode_wav(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Keyfob Decode Wav")

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 5
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=3400,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=3400 * 5,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
        	  3400.0*sps/48000,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.keyfob_parse_packet_0 = keyfob.parse_packet()
        self.keyfob_manchester_decode_0 = keyfob.manchester_decode()
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb("10101000", 0, "packet_start")
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(5*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.05)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_wavfile_source_0 = blocks.wavfile_source("../gqrx_20150306_154200_434400000.wav", False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate*3,True)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(sps, 1, 4000)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_moving_average_xx_1, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.keyfob_manchester_decode_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.wxgui_scopesink2_1, 0))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.keyfob_parse_packet_0, 0))    
        self.connect((self.keyfob_manchester_decode_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_moving_average_xx_1, 0))    


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.blocks_moving_average_xx_1.set_length_and_scale(self.sps, 1)
        self.pfb_arb_resampler_xxx_0.set_rate(3400.0*self.sps/48000)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*3)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = keyfob_decode_wav()
    tb.Start(True)
    tb.Wait()
