import numpy as np
import scipy as sp
import scipy.signal as sig
import scipy.io.wavfile as wav

from Analyzer import Analyzer
from Synthesizer import Synthesizer

def main():
    signal = wav.read("allain.wav")
    analyzer = Analyzer(signal[1], 10e-3, signal[0])
    lpc_frame_array = analyzer.encode()
    synthesizer = Synthesizer(lpc_frame_array)
    arr = synthesizer.decode()
    wav.write("allain_out.wav", signal[0], arr)


if __name__ == "__main__":
    main()
