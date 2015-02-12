#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Keyfob Rx
# Generated: Tue Jun 23 11:31:30 2015
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
import osmosdr
import time
import wx

class keyfob_rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Keyfob Rx")

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
        	  3393.75*sps/1000000.026491,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(1000000)
        self.osmosdr_source_0.set_center_freq(434400000, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(2, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.keyfob_parse_packet_0 = keyfob.parse_packet()
        self.keyfob_manchester_decode_0 = keyfob.manchester_decode()
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb("10101000", 0, "packet_start")
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(sps*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.05)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(sps, 1.0/sps, 4000)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10000, 1.0/10000, 4000)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.keyfob_manchester_decode_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.wxgui_scopesink2_1, 0))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.keyfob_parse_packet_0, 0))    
        self.connect((self.keyfob_manchester_decode_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_moving_average_xx_1, 0))    


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.blocks_moving_average_xx_1.set_length_and_scale(self.sps, 1.0/self.sps)
        self.pfb_arb_resampler_xxx_0.set_rate(3393.75*self.sps/1000000.026491)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps*(1+0.0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = keyfob_rx()
    tb.Start(True)
    tb.Wait()
