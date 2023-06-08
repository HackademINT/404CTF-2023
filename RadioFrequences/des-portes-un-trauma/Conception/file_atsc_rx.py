#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Receive ATSC from UHD
# GNU Radio version: 3.10.6.0

from gnuradio import blocks
import pmt
from gnuradio import dtv
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class file_atsc_rx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Receive ATSC from UHD", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 1.1
        self.atsc_sym_rate = atsc_sym_rate = 4.5e6/286*684
        self.sample_rate = sample_rate = 4500000.0 / 286 * 684
        self.oversampled_rate = oversampled_rate = atsc_sym_rate*sps
        self.gain = gain = 18
        self.freq = freq = 605e6
        self.duration = duration = 30
        self.antenna = antenna = "TX/RX"

        ##################################################
        # Blocks
        ##################################################

        self.dtv_atsc_rx_0 = dtv.atsc_rx(sample_rate,1.5)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/run/media/rmoreau/SSD/tmp/RF/final', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/run/media/rmoreau/SSD/tmp/RF/videoRX.ts', False)
        self.blocks_file_sink_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_atsc_rx_0, 0))
        self.connect((self.dtv_atsc_rx_0, 0), (self.blocks_file_sink_0, 0))


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_oversampled_rate(self.atsc_sym_rate*self.sps)

    def get_atsc_sym_rate(self):
        return self.atsc_sym_rate

    def set_atsc_sym_rate(self, atsc_sym_rate):
        self.atsc_sym_rate = atsc_sym_rate
        self.set_oversampled_rate(self.atsc_sym_rate*self.sps)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_oversampled_rate(self):
        return self.oversampled_rate

    def set_oversampled_rate(self, oversampled_rate):
        self.oversampled_rate = oversampled_rate

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna




def main(top_block_cls=file_atsc_rx, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
