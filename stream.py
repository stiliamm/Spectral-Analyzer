import pyaudio
from audio_driver import AudioDriver


class Stream(AudioDriver):
    
    def __init__(self):
        super().__init__()

        self.driver = pyaudio.PyAudio()
        self.stream = self.driver.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            output=True,
            frames_per_buffer=self.chunk,
        )
