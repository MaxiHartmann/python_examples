import numpy as np
from math import pi
from matplotlib import pyplot as plt


samples=300
freq_1 = 5
freq_2 = 40
amp_1 = 10
amp_2 = 5
t = np.linspace(-1.5, 1.5, samples, endpoint=False)
signal = (amp_1 * np.cos(2 * pi * (freq_1 * t)) + (amp_2 * np.cos(2 * pi * (freq_2 * t)))) * np.exp(-pi * t * t)

plt.subplot(211)
plt.plot(t, signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

fft = np.fft.fft(signal)

# for i in range(2):
#     print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))


T = t[1] - t[0] # sampling interval
N=t.size

# 1/T = frequency
f = np.linspace(0, 1/ T, N)

plt.subplot(212)
plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=0.5)  # 1 / N is a normalization factor
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 45)
plt.show()
