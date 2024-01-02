import numpy as np
import matplotlib.pyplot as plt
import colorsys as clrsys
from PIL import Image
import os

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

# color
h, l, s = 5/255, 200/255, 0/255    # hue,luminance,saturation
rgb1 = clrsys.hls_to_rgb(h, l, s)  # convert HLS to RGB
h, l, s = 5/255, 160/255, 160/255  # hue,luminance,saturation
rgb2 = clrsys.hls_to_rgb(h, l, s)  # convert HLS to RGB

# define graph area
width  = 20
height = 2.2
fig = plt.figure(figsize=(width,height),linewidth=0)
l,b,w,h = 0,0,20/width,2.2/height # left,bottom,width,height
ax = fig.add_axes((l,b,w,h),)

# plot
fp = "./Picture/"
fn = "sinwave_ani"
ex = ".jpg"
fn_list = []
for i in range(len(theta)):
    plt.cla()
    ax.plot(x1,y1,linestyle='None',marker='o',color=rgb1)                # plot circle
    ax.plot(x2,y2,linestyle='None',marker='o',color=rgb1)                # plot sin wave
    ax.plot([center[0],x1[0]], [center[1],y1[0]], color=rgb1,zorder=3)   # start line
    ax.plot(x3[0:i],y3[0:i],color=rgb1,zorder=4)                         # plot circle2
    ax.plot([center[0],x1[i]], [center[1],y1[i]], color=rgb2,zorder=5)   # theta
    ax.plot([x1[i],x2[i]],[y1[i],y2[i]],marker='o',color=rgb2,zorder=6)  # plot line
    fn_list.append(fp+fn+str(i)+ex)
    fig.savefig(fp+fn+str(i)+ex)
fn_list = [fn_list[0]]*100 + fn_list + [fn_list[-1]]*100

# make animation
ratio = 1
rotate = 0
list_images = []
duration = 10    # [ms]
for n in fn_list:
    img = Image.open(n)
    resized_img = img.resize((int(img.width*ratio), int(img.height*ratio)))
    rotated_resized_img = resized_img.rotate(rotate)
    list_images.append(rotated_resized_img)
list_images[0].save('sinwave.gif',
                    save_all=True, 
                    append_images=list_images[1:],
                    optimize=True, 
                    duration=duration,
                    loop=0)
