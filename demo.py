import argparse
import pyaudio
import sys
import threading,time

import numpy as np
import scipy as sp
import scipy.signal as sig
import scipy.io.wavfile as wav

from Analyzer import Analyzer
from Synthesizer import Synthesizer

def play_audio( data, p, fs):
    # play_audio plays audio with sampling rate = fs
    # data - audio data array
    # p    - pyAudio object
    # fs    - sampling rate
    # 
    # Example:
    # fs = 44100
    # p = pyaudio.PyAudio() #instantiate PyAudio
    # play_audio( data, p, fs ) # play audio
    # p.terminate() # terminate pyAudio
    
    # open output stream
    ostream = p.open(format=pyaudio.paFloat32, channels=1, rate=int(fs),output=True)
    # play audio
    ostream.write( data.astype(np.float32).tostring() )
    
    
def record_audio( odata, p, fs, record_seconds ):
    # record_audio records audio with sampling rate = fs
    # odata - output data
    # p     - pyAudio object
    # fs    - sampling rate
    # record_seconds - record seconds
    #tsio
    # Example:
    # fs = 44100
    # record_seconds = 5
    # odata = zeros( fs * record_seconds ) # initialize odata
    # p = pyaudio.PyAudio() #instantiate PyAudio
    # record_audio( odata, p, fs, record_seconds ) # play audio
    # p.terminate() # terminate pyAudio
    
    # open input stream
    chunk = 1024
    istream = p.open(format=pyaudio.paFloat32, channels=1, rate=int(fs),input=True,frames_per_buffer=chunk)

    # record audio in chunks and append to frames
    frames = [];
    for i in range(0, int(fs / chunk * record_seconds)):
        data_str = istream.read(chunk) # read a chunk of data
        data_flt = np.fromstring( data_str, 'float32' ) # convert string to float
        frames.append( data_flt ) # append to list
        
    # flatten list to array
    data = np.concatenate( frames )
    # copy to output
    np.copyto(odata[0:len(data)], data)

def main():
    signal = wav.read("allain.wav")
    analyzer = Analyzer(signal[1], 10e-3, signal[0])
    lpc_frame_array = analyzer.encode()
    synthesizer = Synthesizer(lpc_frame_array)
    arr = synthesizer.decode()
    wav.write("allain_out.wav", signal[0], arr)


if __name__ == "__main__":
    main()
