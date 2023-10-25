import struct
import numpy as np
import keyboard
from audio_driver import AudioDriver
from plotter import Plotter
from stream import Stream


class Engine:
    def __init__(self) -> None:
        self.frames = []
        self.driver = AudioDriver()
        self.stream = Stream()
        self.plotter = Plotter()

    def run(self):
        while True:
            data = self.stream.stream.read(self.stream.chunk, exception_on_overflow=False)
            data_int = struct.unpack(str(self.stream.chunk) + 'h', data)
            fft_data = np.abs(np.fft.fft(data_int)) * 2 / (11000 * self.stream.chunk)
            if len(fft_data) == 0:
                continue

            self.plotter.update_plot(data_int, fft_data)

            if keyboard.is_pressed("r"):
                print("Recording... Press SPACEBAR to stop.")
                self.frames.append(data)

            if keyboard.is_pressed(" "):
                self.plotter.plot_record(self.frames)
                print("Recording finished.")

if __name__ == "__main__":
    e = Engine()
    e.run()
