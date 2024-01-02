import numpy as np
import math
import matplotlib.pyplot as plt
import colorsys as clrsys
# define wave
amp   = 1                                                              # Amplitude
freq  = 1                                                              # Frequency [Hz]
omega = 2*math.pi*freq                                                 # Angular freq. [rad/s]
time  = 1                                                              # Time [sec]
fs    = 880                                                            # Sampling frequency [Hz]
tv    = np.linspace(0,omega*time,time*fs)                              # time vector
y     = amp*np.sin(tv)                                                 # sin wave
# define graph area
width  = 10                                                            # width  of figure
height = 5                                                             # height of figure
fig,ax = plt.subplots(figsize=(width,height))                          # add figure, axes
# color
h,l,s =   5/255, 200/255,   0/255                                      # hue,luminance,saturation
rgb1  = clrsys.hls_to_rgb(h, l, s)                                     # convert HLS to RGB
h,l,s =   5/255, 160/255, 160/255                                      # hue,luminance,saturation
rgb2  = clrsys.hls_to_rgb(h, l, s)                                     # convert HLS to RGB
# plot
ax.plot(tv,y,color=rgb2)                                               # plot sin wave
ax.set_xlim(tv[0],tv[-1])                                              # set xlimit
ax.set_ylim(-1*amp*1.1, amp*1.1)                                       # set ylimit
plt.xlabel('Phase [rad]', fontsize=9)                                  # xlabel
plt.ylabel('y', fontsize=9)                                            # ylabel
plt.hlines([amp,-1*amp],0,omega*time,colors=rgb1,linestyles='dashed')  # amp line
ax.text(0,amp,"Amplitude",size=10.5,color=rgb1)                        # add text
plt.show()                                                             # show
fig.savefig('./sin.jpg')                                               # save figure