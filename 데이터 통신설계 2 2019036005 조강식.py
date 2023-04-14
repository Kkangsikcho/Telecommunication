import numpy as np
import matplotlib.pyplot as Plot

Bit = np.random.choice([0, 1], size=60, p=[0.5, 0.5])

def set_signal(Bit):
    signal = np.array([])
    for i in range(0, 60, 2):
        if Bit[i] == 0 and Bit[i+1] == 0:
            signal = np.concatenate((signal, np.array([-3, -3])))
        elif Bit[i] == 0 and Bit[i+1] == 1:
            signal = np.concatenate((signal, np.array([-1, -1])))
        elif Bit[i] == 1 and Bit[i+1] == 0:
            signal = np.concatenate((signal, np.array([1, 1])))
        else:
            signal = np.concatenate((signal, np.array([3, 3])))
    return signal
signal = set_signal(Bit)
time = np.arange(0, len(signal))


Plot.plot(time, signal)
Plot.xlabel('Time')
Plot.ylabel('Amplitude')
Plot.title('Digital Waveform')
Plot.grid(True)
Plot.show()
