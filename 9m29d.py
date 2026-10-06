import os
import pandas as pd
import numpy as np

HOME = os.path.abspath(os.path.dirname(__file__))
os.chdir(HOME)

import matplotlib.pyplot as plt

x = []
y = []

'''
url = "https://raw.githubusercontent.com/nicesw77/com_phys2024/main/input.csv"
df = pd.read_csv(url, header=None)

x = df[0]
y = df[1]
'''

with open("input.csv", "r") as f:
    for line in f.readlines():
        items = line.split(" ")
        x.append(float(items[0]))
        y.append(float(items[1]))

year, nspots, sd, n1, n2 = np.loadtxt("SN_y_tot_V2.0.csv", delimiter=';', unpack=True)

df = pd.read_csv(f'{HOME}/seoul_temp.csv')
temp = df["temp"]

if __name__ == "__main__":
    plt.scatter(x,y, marker='s', c='b', edgecolors='r' )
    plt.xlim(0, 1)
    plt.ylim(-1.5, 1.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig("data_plot.png", bbox_inches="tight")
    plt.show()

    x = np.linspace(0,5)
    f = lambda x: np.cos(x)*np.cosh(x)-1
    plt.plot(x,f(x), color = 'r', linestyle = '--', linewidth = '2.5')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of cos(x)*cosh(x) - 1')
    plt.show()

    plt.plot(year, nspots)
    plt.show()

    x=[1, 2, 3]
    y=[3, 1, 4]
    plt.plot(x, y, marker='s', markeredgecolor='r', markerfacecolor='g')
    plt.show()

    print("2026년 9월 평균 기온 : ", np.sum(temp)/len(temp))
