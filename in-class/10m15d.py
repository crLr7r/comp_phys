import numpy as np
import matplotlib.pyplot as plt
from Heun_function import heun

def f(t, y):
    dy = -0.05 * y + 2
    return dy

t0 = 0
tf = 80
y0 = 0
h = 10
t, y = heun(f, y0, t0, tf, h)

def fa(t):
    return 40 * (1 - np.exp(-0.05*t))

ta = np.linspace(t0, tf)

plt.scatter(t, y, c='b', marker='o', label = "Heun Method", zorder = 10)
plt.plot(ta, fa(ta), c='k', ls='--', label = "True Solution")
plt.grid(True)
plt.title('Comparison of True solution and quadrature by Heun method')
plt.xlabel(r'$t$')
plt.ylabel(r'$y$')
plt.legend()
plt.show()

from Euler_m_function import eulerm

def f(t,y):
    dy = np.zeros(2)
    dy[0] = -2*y[0]**2 + 2*y[0] + y[1] - 1
    dy[1] = -y[0] - 3*y[1]**2 + 2*y[1] + 2
    return dy

t0 = 0
tf = 2
y0 = np.array([2.,0.])
h = 0.01
t, y = eulerm(f, y0, t0, tf, h)

plt.plot(t, y[:, 0], c='k', label=r'$x_1$')
plt.plot(t, y[:, 1], c='k', ls='--', label=r'$x_2$')
plt.grid(True)
plt.title('Modified Euler method to solve multi diff eqs')
plt.xlabel(r'$t$')
plt.ylabel(r'$x_1$ and $x_2$')
plt.legend()
plt.show()