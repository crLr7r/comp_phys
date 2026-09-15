import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 50, 500)

fig, ax = plt.subplots(figsize=(15, 5))

line, = ax.plot([], [], color="red")
line1, line2, line3 = [ax.plot([], [], color="black")[0] for _ in range(3)]

ax.set_xlim(0, 50)
ax.set_ylim(-2, 2)

def sin(x, t, k=1.0, w=1.0,A=1.0):
    return np.sin(k * x + w * t)

def func(x, t):
    return sin(x,t) + sin(x,t,k=np.pi,w=np.pi) #+ sin(x,t,k=3)

def update(frame):
    y = func(x, frame)
    line.set_data(x, y)
    line1.set_data(x, sin(x, frame))
    line2.set_data(x, sin(x,frame,k=2,w=3))
    #line3.set_data(x, sin(x,frame,k=3))
    return line,line1,line2


ani = FuncAnimation(
    fig,
    update,
    frames=10000,
    interval=100
)

plt.show()
