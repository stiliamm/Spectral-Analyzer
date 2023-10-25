# Spectral-Analyzer


This code provides an audio visualization and recording tool that uses Python and various libraries to capture and display audio waveforms and spectrums in real-time. You can also initiate audio recordings and visualize their frequency spectra.
Prerequisites

Before using this code, make sure you have the following prerequisites:

    Python: You need Python installed on your system.

    Required Python Libraries:
        pyaudio: To capture audio data.
        numpy: For numerical operations and array manipulation.
        matplotlib: For plotting audio waveforms and spectra.
        keyboard: For handling keyboard input to start and stop audio recording.

You can install these libraries using pip:

bash

pip install pyaudio numpy matplotlib keyboard

Code Structure

The code is organized into the following components:

    audio_driver.py: This module contains the AudioDriver class, which defines the audio configuration, such as chunk size, format, channels, and sampling rate.

    stream.py: The Stream class is an extension of AudioDriver that manages the audio stream, allowing audio input and output.

    plotter.py: The Plotter class provides methods for creating and updating audio waveform and spectrum plots.

    engine.py: The main script, Engine, combines these components to capture audio, display real-time visualizations, and record audio.

Usage

To use this audio visualization and recording tool, follow these steps:

    Run the engine.py script:

bash

python engine.py

    The script will start capturing audio data and display real-time audio waveform and spectrum visualizations.

    To initiate audio recording, press the "r" key. The script will start recording audio data until you press the spacebar to stop.

    After stopping the recording, the script will display a frequency spectrum plot of the recorded audio.

Keyboard Controls

    Press "r" to start audio recording.
    Press the spacebar to stop audio recording.

Note

    The code is set up to work with a default audio configuration (16-bit, mono channel, 48 kHz). You can modify these settings in the AudioDriver class in audio_driver.py to match your specific audio input device and requirements.

    The code captures and plots audio data in real-time using matplotlib. You can further customize the visualization by adjusting the plot settings in the Plotter class in plotter.py.

    The audio recording function stores recorded audio frames in memory. Depending on the recording duration, this can consume a significant amount of memory. Consider modifying the code to save the audio data to a file for long recordings.

    Remember to handle exceptions, error handling, and resource cleanup for a more robust implementation.

Feel free to modify and extend the code to suit your specific audio visualization and recording needs.
