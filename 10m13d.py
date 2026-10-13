import numpy as np
import scipy.stats as st
import sys

from matplotlib import pyplot as plt

from Trap1_function import trap2

stdnormdens = lambda z: 1 / np.sqrt(2 * np.pi) * np.exp(-1 / 2 * z ** 2)
a = -1e5
b = 1e5
#b = -0.3
P = trap2(stdnormdens, a, b)
print('probability = {0:6.1f}%'.format(P * 100))

print(st.norm(0,1).cdf(0.32))

print(st.norm(0, 1).ppf(0.6255158347233201))

mu = 100
sigma = 10
a = 75
b = 95

f = st.norm.pdf(b, mu, sigma)
print('normal density at {0} = {1:6.4f}%'.format(b, f))

cp1 = st.norm.cdf(b, mu, sigma)
cp2 = st.norm.cdf(a, loc=mu, scale=sigma)   # 두 코드의 의미는 a,b제외 같음
p = cp1 - cp2   # a에서 b사이에 있을 확률
print('probability between {0} and {1} = {2:5.1f}%'.format(a, b, p * 100))

x = np.concatenate((np.arange(-5*sigma, 0, 0.1), np.arange(0, 5*sigma, 0.1)))
x += mu
y = st.norm.pdf(x, mu, sigma)
plt.plot(x, y)
plt.grid(True)
plt.show()

G = 9.81
m = 1
c = 0.1

def terminal_velocity(t, v):
    dvdt = (m*G-c*(v**2))/m
    return dvdt

def euler(f, x0, xmax, y0, h):
    x = x0
    y = y0
    xsol = np.array([x])
    ysol = np.array([y])
    n = int((xmax - x0)/h)
    for i in range(n):
        y += h*f(x,y)
        x += h
        xsol = np.append(xsol, x)
        ysol = np.append(ysol, y)
    return xsol, ysol

h = [0.5, 0.1, 0.01]
x1, y1 = euler(terminal_velocity, 0, 5, 0, h[0])
x2, y2 = euler(terminal_velocity, 0, 5, 0, h[1])
x3, y3 = euler(terminal_velocity, 0, 5, 0, h[2])
plt.plot(x1, y1, c='red', linestyle = 'dotted', label=r'h=0.5')
plt.plot(x2, y2, c='blue', linestyle = '--', label=r'h=0.1')
plt.plot(x3, y3, c='green', linestyle = '-', label=r'h=0.01')
plt.xlabel(r'$t$')
plt.ylabel(r'velocity')
plt.ylim((-0.5, 12))
plt.title("Terminal Velocity")
plt.legend()
plt.show()

def euler(f, y0, t0, tf, h):
    t = []
    t.append(t0)
    y = []
    y.append(y0)
    i = 0
    while True:
        i += 1
        t.append(t[i - 1] + h)
        if t[i] > tf:
            t[i] = tf
            h = t[i] - t[i - 1]
        y.append(y[i-1] + f(t[i-1], y[i-1])*h)
        if t[i] >= tf: break
    return t, y

def f(t, y):
    dy = -0.05 * y + 2
    return dy

t0 = 0
tf = 80
y0 = 0
h = 10
t, y = euler(f, y0, t0, tf, h)

def fa(t):
    return 40 * ( 1- np.exp(-0.05 * t))

ta = np.linspace(t0, tf)
plt.scatter(t, y, c='k', marker='o', label='Euler Method')
plt.plot(ta, fa(ta), c='k', ls='--', label="True Solution")
plt.grid()
plt.title('Comparison of True solution and quadrature by Euler method')
plt.xlabel(r'$t$')
plt.ylabel(r'$y$')
plt.legend()
plt.show()

def f(x):
    return 3 * x - np.cos(x)
def df(x):
    return 3 * np.sin(x)
def newton_method(x0, f, df):
    return x0 - (f(x0) / df(x0)) * 0.2

x = np.linspace(0, 1)
solution_0 = 0.5
solutions = []
for idx in range(11):
    solution_0 = newton_method(solution_0, f, df)
    solutions.append(solution_0)
plt.figure()
plt.stem(
    solutions,
    np.cos(np.array(solutions)),
    linefmt='k--',
    markerfmt='ko',
    basefmt=" ",
    label=f"[{idx: 2d}] Newton method",
)
plt.plot(x, 3 * x, label="$3x$")
plt.plot(x, np.cos(x), label="$cos(x)$")
plt.xlim(0, 1)
plt.ylim(0, 2.5)
plt.grid(True)
plt.legend()
plt.savefig(f"newton_method_1.png", bbox_inches='tight')
plt.show()