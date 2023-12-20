import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# define graph area
width  = 10
height = 5
fig, ax = plt.subplots(figsize=(width,height))

# define circle
radius = 1
theta  = [np.radians(t) for t in range(0,360+1,10)]

# circle
x1 = radius*np.cos(theta) - 2
y1 = radius*np.sin(theta)
# sin wave
x2 = theta
y2 = radius*np.sin(theta)

ax.plot(x1,y1,color="red",linestyle='dashed')

# plot
ims = []
for i in range(0,len(theta),1):
    im = ax.plot(x1,y1,color="gray",linestyle='dashed')
    im = ax.plot(x1[i],y1[i],'x')
    im = ax.plot(x2,y2,color="gray",linestyle='dashed')
    im = ax.plot(x2[i],y2[i],'x')
    im = ax.plot([x1[i],x2[i]],[y1[i],y2[i]],color="red")
    ims.append(im)

interval = 10
ani = animation.ArtistAnimation(fig, ims, interval=interval)
plt.show()
ani.save("output.gif",writer="imagemagick")
plt.clf()