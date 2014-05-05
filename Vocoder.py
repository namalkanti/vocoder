
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
        wav_array = self.get_array_from_wav(wav_file)
        analyzer = Analyzer(wav_array, frame_size, self.get_fs())
        return analyzer.encode()

    def decode(self, lpc_frame_array, output_file="decoded_signal.wav"):
        """
        Takes in an lpcframe array and returns a wave file.
        """
        synthesizer = Synthesizer(lpc_frame_array)
        wav_array = synthesizer.decode()
        self._write_array_to_wav_file(output_file)

    def get_array_from_wav_file(self, wav_file):
        """
        Reads a wav file and gets an array from it.
        """
        pass

    def write_array_to_wav_file(self, outpu_name):
        """
        Writes and array to a wave file.
        """
        pass

    #Accessor methods
    def get_fs(self):
        return self._fs
