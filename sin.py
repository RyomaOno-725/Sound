# Library
import numpy as np
import matplotlib.pyplot as plt
import tkinter

import matplotlib
matplotlib.use('TkAgg')

# define graph area
width  = 10
height = 5
fig, ax = plt.subplots(figsize=(width,height))

t = np.linspace(0, 100, 1000)  # x: time
amp = np.sin(t)                # y: amplitude
ax.plot(t,amp, color="red")   # plot
plt.show()