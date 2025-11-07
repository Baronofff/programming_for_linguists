import random

from seminars.mixins_using.errors import SpeakerConnectionError


class Speaker:
    def __init__(self, speaker_id, speaker_name):
        self.id = speaker_id
        self.name = speaker_name

    def check_light_connection(self):
        if random.choice([200, 400]) == 200:
            return
        raise SpeakerConnectionError()