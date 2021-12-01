# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import soundfile as sf

signal, fm = sf.read('rl002.wav') # Usamos señal rl002
t = np.arange(0, len(signal)) / fm 

t_ms = 30                 # 30 ms
l = int((fm * t_ms)/1e3)  # 'l' muestras

def autocorrelacion(vector):
    autocorrelation = np.correlate(vector, vector, mode = 'full')
    return autocorrelation[autocorrelation.size//2:]

# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)

plt.figure()
ax = plt.subplot(gs[0, 0]) # row 0, col 0
plt.plot(t, signal)
plt.title('Señal completa (rl002)', fontweight = 'bold')
plt.xlabel('s', fontsize = 10)
plt.ylabel('Amplitud', fontsize = 10)

ax = plt.subplot(gs[0, 1]) # row 0, col 1
plt.plot(t[fm:fm+l], signal[fm:fm+l])
plt.title('Señal recortada (30ms)', fontweight = 'bold')
plt.xlabel('Muestras', fontsize = 10)
plt.ylabel('Amplitud', fontsize = 10)

ax = plt.subplot(gs[1, :]) # row 1, span all columns
plt.plot(t[:l]*1000, autocorrelacion(signal[fm:fm+l]))
plt.title('Autocorrelación', fontweight = 'bold')
plt.xlabel('n', fontsize = 10)
plt.ylabel('Amplitud', fontsize = 10)

plt.tight_layout()
plt.show()
