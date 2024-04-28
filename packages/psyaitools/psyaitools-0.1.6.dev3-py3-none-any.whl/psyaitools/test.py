from psyaitools.func.IOs.base64_xfccs import *
import numpy as np
from scipy.io.wavfile import read

# aaa = base64_xfccs('../../comDat/testBase64.csv', 33, '../../comDat/test.webm', feature_set="mfcc")
# aaa = wav_xfccs('../../comDat/test.wav')
aaa = getLoud('../../comDat/test.wav')