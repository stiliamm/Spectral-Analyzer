import matplotlib.pyplot as plt
import numpy as np
from stream import Stream

plt.style.use('dark_background')


class Plotter:
    def __init__(self):
        stream = Stream()
        self.chunk = stream.chunk
        self.rate = stream.rate

        self.fig, (self.ax_waveform, self.ax_spectrum) = plt.subplots(2, 1, figsize=(10, 7))

        self.x = np.arange(0, 2 * self.chunk, 2)
        self.xf = np.linspace(0, self.rate, self.chunk)

        # create a linear object with random data
        self.line_waveform, = self.ax_waveform.plot(self.x, np.random.rand(stream.chunk), 'w')

        # create logarithmic line for spectrum
        self.line_spectrum, = self.ax_spectrum.loglog(self.xf, np.random.rand(stream.chunk), 'y')

        # format waveform axes
        self.ax_waveform.set_title('Audio Waveform')
        self.ax_waveform.set_xlabel('Samples')
        self.ax_waveform.set_ylabel('Volume')
        self.ax_waveform.set_ylim(-30000, 30000)
        self.ax_waveform.set_xlim(0, stream.chunk)
        self.ax_waveform.grid('y', color='w', linestyle='-', linewidth='0.2')

        # format spectrum axes
        self.ax_spectrum.set_title('Audio Spectrum')
        self.ax_spectrum.set_ylabel("dBFs")
        self.ax_spectrum.set_xlabel("Hz")
        self.ax_spectrum.set_yscale("logit")
        self.ax_spectrum.set_ylim(1e-9, 1)
        self.ax_spectrum.set_xlim(20, stream.rate / 2)
        self.ax_spectrum.grid('y', color='w', linestyle='-', linewidth='0.2')

        # show axes
        self.fig.tight_layout()
        self.fig.show()

    def update_plot(self, waveform_data, spectrum_data):
        # update waveform and spectrum data
        self.line_waveform.set_ydata(waveform_data)
        self.line_spectrum.set_ydata(spectrum_data)

        # update the plot
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def plot_record(self, frames):
        # calculate the fft data
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        lin_y = np.abs(np.fft.fft(audio_data) * 2 / (11000 * len(frames)))
        lin_x = np.linspace(0, len(frames), len(lin_y))

        # plot the recorded data
        plt.figure(figsize=(10, 7))
        plt.loglog(lin_x, lin_y)
        plt.title('Audio Spectrum')
        plt.ylabel("dB")
        plt.xlabel("Hz")
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-9, 1)
        plt.xlim(20, len(frames) / 2)
        plt.grid('y', color='w', linestyle='-', linewidth='0.2')
        plt.show()
