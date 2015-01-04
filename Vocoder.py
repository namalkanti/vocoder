import numpy as np
import scipy as sp
import scipy.io.wavfile as wav

from Analyzer import Analyzer
from Synthesizer import Synthesizer

from Mic import Mic

from Local import Local

class Vocoder():
    """
    Vocoder to do real time synthesis of an audio signal. 
    Links to a VocoderInput and VocoderOutput object to provide 
    I/O for the audio signal.
    """

    def __init__(self, vocoder_in=Mic, vocoder_out=Local, fs=44100):
        """
        Creates a vocoder at a specified sampling rate.
        """
        self._fs = fs
        self._in = vocoder_in
        self._out = vocoder_out
        self._callback = self.generate_callback()

    def generate_callback(self):
        """
        Generates the callback function for the audio stream
        """
        def callback(in_data, frame_count, time_info, flag):
            """
            Generated callback 
            """
            pass

    #Accessor methods
    def get_fs(self):
        return self._fs
