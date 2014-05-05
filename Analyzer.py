import numpy as np
import scipy as sp
import scipy.signal as sig
import scipy.linalg as linalg

from segmentaxis import segment_axis

from LPCStructures import LPCFrameArrayBuilder

class Analyzer():
    """
    Speech analyzer for vocoder. 
    """

    def __init__(self, signal, frame_size, fs=44100.0, order=50):
        """
        Creates an analyzer from a signal, frame_size(in seconds), and sampling rate.
        """
        self._signal = signal
        self._fs = fs
        self._frame_size = frame_size 
        self._order = order

    def encode(self):
        """
        Returns a numpy array of LPC frames for the given signal.
        """
        signal_windows = self._window_signal()
        lpc_array = self._estimate_windows(signal_windows)
        return lpc_array

    def window_signal(self):
        """
        Takes the signal field, divides it into frames and creates a window with the frame and two adjacent frames to create a window.  
        Pads the end with zeros if the array size is not properly divisible.
        Does NOT modify original signal.
        """
        samples_per_frame = self.get_frame_size() * self.get_fs()
        window_length = samples_per_frame * 3
        return segment_axis(self.get_signal(), window_length, samples_per_frame, end="pad") 

    def estimate_windows(self, windows):
        """
        Takes in an array of windows and returns a corresponding LPCArray.
        """
        frame_array_builder = LPCFrameArrayBuilder()
        frame_array_builder.set_fs(self.get_fs())
        frame_array_builder.set_frame_size(self.get_frame_size())
        for window in windows:
            frame_array_builder.add_frames(self.estimate(window))
        return frame_array_builder.build()

    def estimate(self, window):
        """
        Runs an estimation on the window and returns an LPCFrame.
        """
        tapered_window = np.copy(window) * np.hamming(window.size)
        gain, coefficients = self._lpc(tapered_window, self.get_order())
        residue = self._inverse_filter(window, gain, coefficients)
        return LPCFrame(residue, gain, coefficients)

    def _lpc(self, signal, order):
        """
        Takes in a signal and determines lpc coefficients(through autocorrelation method) and gain for inverse filter.
        This is a naive implementation. Do not expect speed.
        Returns gain and lpc_coefficients as a tuple in that order.
        """
        length = signal.size
        autocorrelation = sig.fftconvolve(signal, signal[::-1])
        autocorr_coefficients = autocorrelation[autorcorrelation.size/2:][:(order + 1)]
        R = linalg.toeplitz(autocorr_coefficients)
        lpc_coefficients = np.dot(linalg.inv(R), autocor_coefficients[1:order+1])
        error_filter = np.insert(-1 * coefficients, 0, 1)
        gain = np.sqrt(sum(error_filter * lpc_coefficients))
        return gain, lpc_coefficients

    def _inverse_filter(self, window, gain, coefficients):
        """
        Uses the determined coeffcients to get acquire residue from a speech frame.
        """
        denominator = np.asarray([1])
        numerator = np.insert(coefficients, 0, 1)
        return sig.lfilter(numerator, denominator, window)/ gain


    #Accessor Methods
    def get_signal(self):
        return np.copy(self._signal)

    def get_fs(self):
        return self._fs

    def get_frame_size(self):
        return self._frame_size

    def get_order(self):
        return self._order

