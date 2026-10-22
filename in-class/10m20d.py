import numpy as np
import matplotlib.pyplot as plt
from Euler_m_function import eulerm

g = 9.801
m = 10
b = 5
k1 = 1
k2 = 1
x1eq = 0
x2eq = 0
v0 = 0
x0 = 1

def f(t, y):
    v = y[0]
    x = y[1]
    dy = np.zeros(2)
    dy[0] = 1/m * (-b*v - k1*(x-x1eq)) - k2 * (x - x2eq)
    dy[1] = v
    return dy

t0 = 0
tf = 20
y0 = np.array([v0, x0])
h = 0.01
t, y = eulerm(f, y0, t0, tf, h)

plt.plot(t, y[:, 1], c='k', label='displacement [m]')
plt.plot(t, y[:, 0], c='k', ls='--', label='velocity [m/s]')
plt.grid()
plt.title('Eulerm to solve the 2nd order diff eqs')
plt.xlabel('time [s]')
plt.ylabel('displacement & velocity')
plt.legend()
plt.show()

m = 50/1000
cd = 4.3e-4

def f(t, yy):
    vx = yy[2]
    vy = yy[3]
    dy = np.zeros(4)
    dy[0] = vx
    dy[1] = vy
    dy[2] = -cd * vx * np.sqrt(vx**2 + vy**2)/2/m
    dy[3] = - g - cd * vy * np.sqrt(vx**2 + vy**2)/2/m
    return dy

t0 = 0
tf = 10
v0 = 67
theta = 30 * np.pi / 180
y0 = 10
yy0 = np.array([0, y0, v0 * np.cos(theta), v0 * np.sin(theta)])
h = 0.01
t, y = eulerm(f, yy0, t0, tf, h)
xp = y[:, 0]

yp = np.tan(theta) * xp - g / 2/ v0**2/ np.cos(theta)**2 * xp**2 + y0
plt.plot(y[:, 0], y[:, 1], c='k', label='drag')
plt.plot(xp, yp, c='k', ls='--', label='no drag')
plt.grid()
plt.title('2D trajectory')
plt.xlabel('range - m')
plt.ylabel('elevation - m')
plt.legend()
plt.show()

a = 3
b = 2
c = 1
d = 2

def lveq(t, y):
    dydt0 = a * y[0] - b * y[0] * y[1]
    dydt1 = -c * y[1] + d * y[0] * y[1]
    return np.array([dydt0, dydt1])

def RK4(f, h, t0, tmax, y0):
    n = int((tmax - t0) / h)
    t = t0
    y = y0
    m = len(y0)
    tsol = np.zeros(n+1)
    ysol = np.zeros([n+1, m])
    tsol[0] = t
    ysol[0, :] = y
    for i in range(n):
        k1 = f(t, y)
        k2 = f(t + 0.5*h, y + 0.5*h*k1)
        k3 = f(t + 0.5*h, y + 0.5*h*k2)
        k4 = f(t + h, y + h*k3)
        y = y + h * ( k1 + 2*k2 + 2*k3 + k4)/6
        t += h
        tsol[i + 1] = t
        ysol[i + 1, :] = y
    return tsol, ysol

h = 0.01
t0, tmax = 0, 20
y0 = np.array([1.9, 1.7])
t, y = RK4(lveq, h, t0, tmax, y0)
plt.plot(t, y[:, 0], label = r'$x$ (prey)')
plt.plot(t, y[:, 1], label = r'$y$ (predator)')
plt.xlabel(r'$t')
plt.ylabel(r'$x, y$ (population)')
plt.legend()
plt.title("Lotka-Volterra Equation")
plt.show()
