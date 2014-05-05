
class LPCFrame():
    """
    Contains residue data, gain, and lpc coefficients for frame of signal. 
    """

    def __init(self, residue, gain, coefficients, overlap):
        """
        Creates an LPC frame from a residue, gain, and coeffcients.
        """
        self._residue = residue
        self._gain = gain
        self._coefficients = coefficients

    #Accessor methods
    def get_residue(self):
        return self._residue

    def get_gain(self):
        return self._gain

    def get_coefficients(self):
        return self._coefficients

import numpy as np

class LPCFrameArrayBuilder():
    """
    Builder design pattern for LPCFrameArray class.
    """

    def __init__(self):
        """
        Constructor for LPCFrameBuilder.
        """
        self._fs = 44100
        self._frame_size = 0
        self._frames = None

    #Mutator methods
    def set_fs(self, fs):
        self._fs = fs

    def set_frame_size(self, frame_size):
        self._frame_size = frame_size

    def add_frames(self, *args):
        if self._frames == None:
            self._frames = np.array(*args)
        else:
            self._frames = np.concatenate((self._frames, np.array(*args)))

    def build(self):
        return LPCFrameArray(self._fs, self._frame_size, self._overlap, self._frames)

class LPCFrameArray():
    """
    Contains a numpy array of LPC frames along with additional information about the signal.
    DO NOT CALL THIS DIRECTLY. Use the builder instead.
    """

    def __init__(self, fs, frame_size, frames):
        self._fs =fs 
        self._frame_size = frame_size
        self._frames = frames

    #Accessor methods
    def get_fs(self):
        return self._fs

    def get_frame_size(self):
        return self._frame_size

    def get_frames(self):
        return np.copy(self._frames)

