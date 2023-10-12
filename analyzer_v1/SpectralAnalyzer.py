import pyaudio
import keyboard
import matplotlib.pyplot as plt
import struct
import numpy as np
from scipy.fftpack import fft
plt.style.use('dark_background')


class AudioStream:

    # ================================================== INITIALIZE AUDIO PARAMETERS
    # ==============================================================

    def __init__(self):

        # stream const
        self.CHUNK = 2048
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000

        # stream object

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,

        )

        # start functions
        self.init_plots()
        self.start_plot()

    # ================================================== CREATE PLOT FIGURES TO MAP DATA
    # ==========================================================

    def init_plots(self):

        # create matplotlib figures and axes
        self.fig, (ax, ax1) = plt.subplots(2, 1, figsize=(10, 7))
        
        # x vars for plotting 
        x = np.arange(0, 2 * self.CHUNK, 2)
        xf = np.linspace(0, self.RATE, self.CHUNK)
       
        # create a linear object with random data
        self.line, = ax.plot(x, np.random.rand(self.CHUNK), 'w')

        # create logarithmic line for spectrum
        self.line_fft, = ax1.loglog(xf, np.random.rand(self.CHUNK), 'y')
        
        # format waveform axes
        ax.set_title('Audio Waveform')
        ax.set_xlabel('Samples')
        ax.set_ylabel('Volume')
        ax.set_ylim(-30000, 30000)
        ax.set_xlim(0, self.CHUNK)
        ax.grid('y', color = 'w', linestyle = '-', linewidth = '0.2')

        # format spectrum axes 
        ax1.set_title('Audio Spectrum')
        ax1.set_ylabel("dBFs")
        ax1.set_xlabel("Hz")  
        ax1.set_yscale("logit")                                   
        ax1.set_ylim(0.000001, 1000)
        ax1.set_xlim(20, self.RATE / 2)
        ax1.grid('y', color = 'w', linestyle = '-', linewidth = '0.2')
        
        # show axes
        self.fig.tight_layout()
        self.fig.show()
    
    # ====================================================== RECORD INPUT && CALCULATE LOUDNESS
    # ====================================================
    
    def plot_record(self, frames):

        # calculate the fft data  
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        liny = np.abs(np.fft.fft(audio_data) * 2 / (11000 * self.CHUNK))
        linx = np.linspace(0, self.RATE, len(liny))
            
        # plot the recorded data
        plt.figure(figsize=(10, 7))
        plt.loglog(linx, liny)
        plt.title('Audio Spectrum')
        plt.ylabel("dB")
        plt.xlabel("Hz")
        plt.yscale('logit')
        plt.ylim(1e-9, 1)
        plt.xlim(20, self.RATE / 2)
        plt.grid('y', color='w', linestyle='-', linewidth='0.2')
        plt.show()

    # ================================================== MAIN LOOP ====================================================

    def start_plot(self):

        frames = []

        # Main Loop
        while True:

            # read data from input and calculate the FFT 
            
            data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            dataInt = struct.unpack(str(self.CHUNK) + 'h', data)
            fft_data = np.abs(np.fft.fft(dataInt)) * 2 / (11000 * self.CHUNK)     
            if len(fft_data) == 0:
                continue
            
            # set data parameters 
            self.line.set_ydata(dataInt)
            self.line_fft.set_ydata(fft_data)
            
            # update the plot
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            # command line for recording
            
            if keyboard.is_pressed("r"):
                print("Recording... Press SPACEBAR to stop.")
                frames.append(data)
                
            if keyboard.is_pressed(" "):
                self.plot_record(frames)                
                print("Recording finished.")
                

if __name__ == "__main__":
    AudioStream()
