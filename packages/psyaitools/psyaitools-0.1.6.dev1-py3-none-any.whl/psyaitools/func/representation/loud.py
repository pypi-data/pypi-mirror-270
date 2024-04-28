# -*- coding: utf-8 -*-
import pyloudnorm as pyln

def loudness(sig, fs):
    meter = pyln.Meter(fs)  # create BS.1770 meter
    return meter.integrated_loudness(sig)