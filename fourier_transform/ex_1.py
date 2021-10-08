import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100     # Hertz
DURATION = 5            # Seconds
AMPLITUDE = 0.01

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

base_note=440
_, nice_tone = generate_sine_wave(440, SAMPLE_RATE, DURATION)
mixed_tone = nice_tone

for i in range(1,9):
    _, noise_tone = generate_sine_wave(base_note*i, SAMPLE_RATE, DURATION)
    noise_tone = noise_tone / i
    mixed_tone += noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)
normalized_tone = normalized_tone/max(normalized_tone) * AMPLITUDE

plt.plot(normalized_tone[:1000])
plt.show()

from scipy.io.wavfile import write

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)


# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION
# yf contains complex numbers

from scipy.fftpack import rfft, rfftfreq

# Note the extra 'r' at the front
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()
