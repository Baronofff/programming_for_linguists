from abc import ABC

from mixins_using.mixins import LoggingMixin


class ConnectionError(ABC, Exception, LoggingMixin):
    def __str__(self):
        pass

class SpeakerConnectionError(ConnectionError):
    def __str__(self):
        self.log(f"Speaker connection error occurred")
        return "Speaker connection error"

class LightConnectionError(ConnectionError):
    def __str__(self):
        self.log(f"Light connection error occurred")
        return "Light connection error"