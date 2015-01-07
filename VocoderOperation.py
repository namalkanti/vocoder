from abc import ABCMeta

class VocoderIO():
    """
    Abstract base class for IO to a vocoder module.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_callback_operation(self):
        """
        Returns callback operation for VocoderIO. Will vary by subclass.

        """
        return None

