import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import colorsys as clrsys

# define graph area
width  = 20
height = 2.2
fig = plt.figure(figsize=[width,height])
# ax = fig.add_axes([0,0,1,1])
ax = fig.add_subplot(111)

# define
radius = 1
theta  = [np.radians(t) for t in range(0,720+1,10)]
center = [-2,0]
circle_x = np.cos(theta)               # x coordinate of unit-circle
circle_y = np.sin(theta)               # y coordinate of unit-circle
x1 = radius*circle_x + center[0]       # x coordinate of circle
y1 = radius*circle_y                   # y coordinate of circle
x2 = theta                             # x coordinate of sin wave
y2 = y1                                # y coordinate of sin wave
x3 = 0.3*circle_x + center[0]          # x coordinate of circle
y3 = 0.3*circle_y                      # y coordinate of circle

# color settings
h, l, s = 5/255, 200/255, 0/255        # hue,luminance,saturation
rgb1 = clrsys.hls_to_rgb(h, l, s)      # convert HLS to RGB
h, l, s = 5/255, 160/255, 160/255      # hue,luminance,saturation
rgb2 = clrsys.hls_to_rgb(h, l, s)      # convert HLS to RGB

# plot
ims = []
# tile = 331
for i in range(0,len(theta),1):
    # ax = fig.add_subplot(tile)
    im = None
    im = ax.plot(x1,y1,marker='o',color=rgb1,zorder=1)       # plot circle
    im = ax.plot(x2,y2,marker='o',color=rgb1,zorder=2)       # plot sin wave
    # im = ax.plot([center[0],x1[0]], [center[1],y1[0]], color=rgb1,zorder=3)   # start line
    # im = ax.plot(x3[0:i],y3[0:i],color=rgb1,zorder=4)                         # plot circle2
    # im = ax.plot([center[0],x1[i]], [center[1],y1[i]], color=rgb2,zorder=5)   # theta
    im = ax.plot([x1[i],x2[i]],[y1[i],y2[i]],marker='o',color=rgb2,zorder=6)  # plot line
    ims.append(im)
    # tile += 1
ims = [ims[0]]*100 + ims + [ims[-1]]*100

interval = 10  # [ms], fps=1/10x10^-3=100
ani = animation.ArtistAnimation(fig, ims, interval=interval)
# plt.show()
ani.save("output.gif",writer="imagemagick")
# plt.clf()