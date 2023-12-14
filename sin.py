import numpy as np
import math
import matplotlib.pyplot as plt

# define wave
amp  = 1    # Amplitude
freq = 1    # Frequency [Hz(=回/sec)]
time = 1    # Time [sec]
fs   = 880  # Sampling frequency [Samples/sec]

tr   = [0, 2*math.pi*freq*time]                    # time range
tv   = np.linspace(0,2*math.pi*freq*time,time*fs)  # time vector
yr   = [-1*amp, amp]
y    = amp*np.sin(tv)

# define graph area
width  = 10
height = 5
fig, ax = plt.subplots(figsize=(width,height))

# plot
ax.plot(tv,y,color="red")   # sin

ax.set_xlim(tr[0], tr[1])
ax.set_ylim(yr[0]*1.1, yr[1]*1.1)
plt.xlabel('time', fontsize=9)
plt.ylabel('y', fontsize=9)

ax.text(0,amp,"Amplitude",size=10.5,color='gray')
plt.hlines(yr,0,2*math.pi*freq*time,'gray',linestyles='dashed')

plt.show()