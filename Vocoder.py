import numpy as np
import scipy as sp
import scipy.io.wavfile as wav

from Analyzer import Analyzer
from Synthesizer import Synthesizer

class Vocoder():
    """
    Can take in audio files and return lpc parameters, as well as 
    return audio files from lpc parameters. Also carries out sound alteration.
    """

    def __init__(self, fs=44100):
        """
        Creates a vocoder at a specified sampling rate.
        """
        self._fs = 441000

    def encode(self, wav_file, frame_size):
        """
        Takes in a wav file and returns an lpcframe array for transmission.
        """
        wav_info = self.get_array_from_wav_file(wav_file)
        self._fs = wav_info[0]
        wav_array = wav_info[1]
        analyzer = Analyzer(wav_array, frame_size, self.get_fs())
        return analyzer.encode()

    def decode(self, lpc_frame_array, output_file="decoded_signal.wav"):
        """
        Takes in an lpcframe array and returns a wave file.
        """
        synthesizer = Synthesizer(lpc_frame_array)
        if self.get_fs() != synthesizer.get_fs():
            raise ValueError, "lpc array has different sampling rate than vocoder"
        wav_array = synthesizer.decode()
        #self.write_array_to_wav_file(output_file, wav_array)
        return wav_array

    def get_array_from_wav_file(self, wav_file):
        """
        Reads a wav file and gets an array and sampling rate from it.
        """
        return wav.read(wav_file)

    def write_array_to_wav_file(self, output_name, data):
        """
        Writes and array to a wave file.
        """
        wav.write(output_name, self.get_fs(), data)

    #Accessor methods
    def get_fs(self):
        return self._fs
