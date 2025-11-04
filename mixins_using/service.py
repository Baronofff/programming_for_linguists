import random

from mixins_using.errors import LightConnectionError

class Speaker:
    def __init__(self, speaker_id, speaker_name):
        self.id = speaker_id
        self.name = speaker_name
        self.connection = self.check_connection()

    def check_connection(self):
        if random.choice([200, 400]) == 200:
            return
        raise LightConnectionError()