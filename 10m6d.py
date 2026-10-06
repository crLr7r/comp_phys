import numpy as np
import matplotlib.pyplot as plt
import os

theta = np.linspace(0., np.pi*1, 100)

f = lambda th: np.sin(th)*np.cos(th)
# plt.polar(theta, f(theta), c='k')
# plt.title('Polar plot of sin(x)*cos(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# 이차함수 피팅
def sign(x):
    if x > 0: return "+"
    else: return ""

def make_eq(coefficients):
    eq = []
    deg = len(coefficients) - 1
    for i, c in enumerate(coefficients):
        if i != 0 and i != deg:
            eq.append(f" {sign(c)} {c:.2f}x^{deg - i}")
        elif i == 0: eq.append(f"{c:.2f}x^{deg - i}")
        elif i == deg: eq.append(f"{sign(c)} {c:.2f}")

    return "".join(eq)

HOME = os.path.abspath(os.path.dirname(__file__))
os.chdir(HOME)

x = []
y = []

with open("input.csv", "r") as f:
    for line in f.readlines():
        _x, _y = [float(i) for i in line.split(" ")]
        x.append(_x)
        y.append(_y)
coefficients = np.polyfit(x, y, 2)  # 2차 다항식에 피팅하겠다는 의미
print(coefficients)
poly_eq = np.poly1d(coefficients)   # 다항식 생성

# 피팅된 함수에 따라 y값을계산
y_fit = poly_eq(x)

# 원래 데이터와 피팅된 함수를 그래프로 표현
# plt.scatter(x, y, label="Original data", color="b")
# plt.plot(x, y_fit, label="Fitted line", color="r")
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.title(f"Polynomial Fit (Degree: 2)\nEquation: " + make_eq(coefficients))
# plt.grid(True)
#
# plt.show()
# plt.close()

x = np.asarray(x)
y = np.asarray(y)

degs = [1,2,3,4,5,8,14,18]
new_x = np.linspace(0, 1)
# plt.figure(figsize = (8,10))
# for idx, deg in enumerate(degs):
#     coef = np.polyfit(x, y, deg)
#     fit = np.poly1d(coef)
#     sst = np.sum(np.power(y - np.average(y), 2))
#     sse = np.sum(np.power(y - fit(x), 2))
#     sqr = 1 - (sse / sst)
#     print(f"======== DEG: {deg}, R^2:{sqr:.3f}=======")
#     print(coef)
#
#     ax = plt.subplot(4,2,idx+1)
#     ax.set_xlim(0,1)
#     ax.set_ylim(-1,1)
#     #ax.set_title(make_eq(coef), fontsize=5)
#     ax.text(0.05, -0.9, f"DEG: {deg}, $R^2$:{sqr:.3f}", fontsize=10)
#     ax.plot(x, y, ".k")
#     ax.plot(new_x, fit(new_x), "--r", label="DEG: {}".format(deg))
# plt.savefig("01_data_fitting.png", bbox_inches="tight")
# plt.show()
# plt.close()

def f(x):
    return 3 * x ** 2 + 2 * x + 6

def sin(x):
    return np.sin(x)

def g(func, x):
    y = []
    h = 0.01
    for _x in x:
        y.append((func(_x + h) - func(_x)) / h)
    return np.array(y)

def draw_diff(func):
    x = np.linspace(0, 10)
    ax1 = plt.subplot(2,1,1)
    ax1.set_title("Original function")
    ax1.set_xlim(0, 10)
    #ax1.set_ylim(0, 400)
    ax1.axes.xaxis.set_ticklabels([])   # tick을 쓰지 말라는 뜻
    ax1.plot(x, func(x), color="blue")
    ax1.grid(True)
    ax2 = plt.subplot(2,1,2)
    ax2.set_title("Differential function")
    ax2.set_xlim(0, 10)
    #ax2.set_ylim(0, 200)
    ax2.plot(x, g(func, x), color="red")
    ax2.grid(True)
    plt.show()

def draw_diff_overlap(func, xlim=None, xticks=None, name="Original"):
    if xlim is None:
        xlim = [0.0, 32.0, 0.1]

    x = np.arange(*xlim)

    plt.figure(figsize=(10,5))
    plt.plot(x, func(x), color="black", linestyle="dashed", label=name)
    plt.plot(x, g(func, x), color="red", label=f"Derivative of {name}")
    if xticks is not None: plt.xticks(xticks[0], xticks[1])
    plt.grid(True)
    plt.legend()
    plt.show()

def get_pi_ticks(xmax):
    xticks = np.arange(0, xmax, np.pi/2)
    xlabels = []
    for i in range(len(xticks)):
        if i % 2 == 0:
            if i == 0: xlabels.append("0")
            elif i == 2: xlabels.append(r"$\pi$")
            else: xlabels.append(fr"{i // 2}$\pi$")
        if i % 2 == 1:
            if i == 1: xlabels.append(r"$\pi$/2")
            else: xlabels.append(fr"{i}$\pi$/2")

    return xticks, xlabels

draw_diff(f)
draw_diff_overlap(sin, name="sin(x)", xlim=[0,10*np.pi + 0.1,0.1], xticks=get_pi_ticks(10*np.pi))

x = []
y = []

with open("input.csv", "r") as f:
    for line in f.readlines():
        _x, _y = [float(i) for i in line.split(" ")]
        x.append(_x)
        y.append(_y)

def g(x, y, draw=True, ax=None):
    new_x = []
    new_y = []
    for idx in range(len(x) - 1):
        _new_x = (x[idx] + x[idx + 1]) / 2
        new_x.append(_new_x)
        _new_y = (y[idx + 1] - y[idx]) / (x[idx + 1] - x[idx])

        if draw:
            if ax is None:
                fig, ax = plt.subplots()
            def f(x): return _new_y * (x - x[idx]) + y[idx]
            tempx = np.linspace(x[idx], x[idx + 1], 100)
            ax.plot(tempx, f(tempx), color="black", linestyle="dashed")
            ax.text(_new_x, (y[idx] + y[idx + 1]) / 2 - 0.3, f"{_new_y:.1f}", fontsize=10)

        new_y.append(_new_y)
    return new_x, new_y

fit = np.poly1d(np.polyfit(x, y, 2))
fit_x = np.linspace(0, 1)
fit_y = fit(fit_x)

ax1 = plt.subplot(2,1,1)
ax1.set_title("Original function")
ax1.set_xlim(0, 1)
ax1.set_ylim(-2, 2)
ax1.axes.xaxis.set_ticklabels([])
ax1.plot(fit_x, fit_y, color="red", alpha=0.5)
ax1.scatter(x, y)
ax1.grid(True)
new_x, new_y = g(x, y, ax=ax1)

ax2 = plt.subplot(2,1,2)
ax2.set_title("Differential function")
ax2.set_xlim(0, 1)
ax2.set_ylim(-20, 20)
ax2.plot(fit_x[:-1], np.diff(fit_y) / (fit_x[1] - fit_x[0]), "k--")
ax2.scatter(new_x, new_y)
ax2.grid(True)

plt.show()