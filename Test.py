import unittest

import numpy as np

from numpy.testing import assert_array_almost_equal

from segmentaxis import segment_axis

from Analyzer import Analyzer
from Synthesizer import Synthesizer
from LPCStructures import LPCFrameArray

class AnalyzerTest(unittest.TestCase):
    """
    Tests for Analyzer class.
    """

    def test_window_signal(self):
        """
        Tests functionality of window signal method.
        """
        test_signal_one = np.arange(0, 11)
        test_signal_two = np.arange(1, 11)
        test_one = Analyzer(np.copy(test_signal_one), 1, 1) 
        test_two = Analyzer(np.copy(test_signal_two), 1, 1)
        test_three = Analyzer(np.copy(test_signal_one), 2, 1) 
        windows_one = test_one.window_signal()
        windows_two = test_two.window_signal()
        windows_three = test_three.window_signal()
        arr = np.asarray([0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10])
        expected_one = np.reshape(arr, (5, 3))        
        arr2 = np.asarray([1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 0])
        expected_two = np.reshape(arr2, (5, 3))
        arr3 = np.asarray([0, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 0, 0, 0])
        expected_three = np.reshape(arr3, (3, 6)) 
        assert_array_almost_equal(expected_one, windows_one)
        assert_array_almost_equal(expected_two, windows_two)
        assert_array_almost_equal(expected_three, windows_three)

class SynthesizerTest(unittest.TestCase):
    """
    Tests for Synthesizer class.
    """

    def test_merge_frames(self):
        """
        Merges frames back into a single array presenting a reconstructed audio signal.
        """
        expected_array = np.array([0, 1, 2, 3, 3.4, 4.25, 6, 7, 6.8, 7.65, 10, 11, 10.2, 11.05, 14, 15, 0, 0])
        input_array = segment_axis(np.arange(0, 16), 6, 2, end="pad")
        fake_lpc_frame_array = LPCFrameArray(1, 2, input_array)
        fake_synthesizer = Synthesizer(fake_lpc_frame_array)
        result_array = fake_synthesizer._merge_frames(input_array)
        assert_array_almost_equal(expected_array, result_array)

class VocoderTest(unittest.TestCase):
    """
    Tests for vocoder class.
    """
    pass


if __name__ == "__main__":
    unittest.main()
