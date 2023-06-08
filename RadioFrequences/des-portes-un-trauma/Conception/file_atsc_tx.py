#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: File Atsc Tx
# GNU Radio version: 3.10.6.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import pmt
from gnuradio import dtv
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import math



class file_atsc_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "File Atsc Tx", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("File Atsc Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "file_atsc_tx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 4500000.0 / 286 * 684
        self.pilot_freq = pilot_freq = (6000000.0 - (symbol_rate / 2)) / 2
        self.center_freq = center_freq = 429e6

        ##################################################
        # Blocks
        ##################################################

        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, firdes.root_raised_cosine(0.11, symbol_rate, symbol_rate/2, 0.1152, 200), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.dtv_dvbs2_modulator_bc_0 = dtv.dvbs2_modulator_bc(
            dtv.FECFRAME_NORMAL,
            dtv.C1_4,
            dtv.MOD_8VSB,
            dtv.INTERPOLATION_OFF)
        self.dtv_atsc_trellis_encoder_0 = dtv.atsc_trellis_encoder()
        self.dtv_atsc_rs_encoder_0 = dtv.atsc_rs_encoder()
        self.dtv_atsc_randomizer_0 = dtv.atsc_randomizer()
        self.dtv_atsc_pad_0 = dtv.atsc_pad()
        self.dtv_atsc_interleaver_0 = dtv.atsc_interleaver()
        self.dtv_atsc_field_sync_mux_0 = dtv.atsc_field_sync_mux()
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_char*1, 1024)
        self.blocks_rotator_cc_0 = blocks.rotator_cc((((-3000000.0 + pilot_freq) / symbol_rate) * (math.pi * 2)), False)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_char, 832, 1024, 4)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/run/media/rmoreau/SSD/tmp/RF/outry.ts', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/run/media/rmoreau/SSD/tmp/RF/final', False)
        self.blocks_file_sink_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_atsc_pad_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.dtv_dvbs2_modulator_bc_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.dtv_atsc_field_sync_mux_0, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.dtv_atsc_interleaver_0, 0), (self.dtv_atsc_trellis_encoder_0, 0))
        self.connect((self.dtv_atsc_pad_0, 0), (self.dtv_atsc_randomizer_0, 0))
        self.connect((self.dtv_atsc_randomizer_0, 0), (self.dtv_atsc_rs_encoder_0, 0))
        self.connect((self.dtv_atsc_rs_encoder_0, 0), (self.dtv_atsc_interleaver_0, 0))
        self.connect((self.dtv_atsc_trellis_encoder_0, 0), (self.dtv_atsc_field_sync_mux_0, 0))
        self.connect((self.dtv_dvbs2_modulator_bc_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "file_atsc_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_pilot_freq((6000000.0 - (self.symbol_rate / 2)) / 2)
        self.blocks_rotator_cc_0.set_phase_inc((((-3000000.0 + self.pilot_freq) / self.symbol_rate) * (math.pi * 2)))
        self.blocks_throttle2_0.set_sample_rate(self.symbol_rate)
        self.fft_filter_xxx_0.set_taps(firdes.root_raised_cosine(0.11, self.symbol_rate, self.symbol_rate/2, 0.1152, 200))

    def get_pilot_freq(self):
        return self.pilot_freq

    def set_pilot_freq(self, pilot_freq):
        self.pilot_freq = pilot_freq
        self.blocks_rotator_cc_0.set_phase_inc((((-3000000.0 + self.pilot_freq) / self.symbol_rate) * (math.pi * 2)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq




def main(top_block_cls=file_atsc_tx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
