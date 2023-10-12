import struct
import numpy as np
import keyboard
from audio_driver import AudioDriver
from plotter import Plotter
from stream import Stream


class Engine:
    frames = []
    driver = AudioDriver()
    stream = Stream()
    plotter = Plotter()

    # Main Loop
    while True:
        # read data from input and calculate the FFT
        data = stream.stream.read(stream.chunk, exception_on_overflow=False)
        data_int = struct.unpack(str(stream.chunk) + 'h', data)
        fft_data = np.abs(np.fft.fft(data_int)) * 2 / (11000 * stream.chunk)
        if len(fft_data) == 0:
            continue

        # update the plot
        plotter.update_plot(data_int, fft_data)

        # command line for recording
        if keyboard.is_pressed("r"):
            print("Recording... Press SPACEBAR to stop.")
            frames.append(data)

        if keyboard.is_pressed(" "):
            plotter.plot_record(frames)
            print("Recording finished.")


if __name__ == "__main__":
    Engine()
