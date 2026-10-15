import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

HOME = os.path.abspath(os.path.dirname(__file__))
os.chdir(HOME)
#print(HOME)



# data = np.loadtxt("hist.csv")
# n, bins, p, = plt.hist(data, bins=40, color="k")
# plt.xlim(0, 12)
# plt.title("Energy Spectrum")
# plt.xlabel("Energy(keV)")
# plt.ylabel("Intensity")
# plt.grid()
# plt.show()


country = ["China", "America", "Germany", "India", "Spain",
            "UK", "France", "Brazil", "Canada", "Italy"]
GW = [221.0, 96.4, 59.3, 35.0, 23.0, 21.7, 15.3, 14.5, 12.8, 10.0]
x = np.arange(len(GW))

idx = np.argsort(GW)[::-1]

country_sorted = []
GW_sorted = []
for i in idx:
    country_sorted.append(country[i])
    GW_sorted.append(GW[i])

plt.bar(x, GW_sorted, edgecolor="k", facecolor="yellow")
plt.xticks(x, country_sorted, rotation="vertical")
plt.xlabel("country")
plt.ylabel("GW")
plt.grid(axis="y")
plt.title("Wind Power Capacity by Country in 2021")
plt.tight_layout()
plt.show()

size = 100000
x_rand = np.random.normal(scale=0.5, size=size)
y_rand = np.random.normal(scale=0.5, size=size)
print(x_rand.mean(), y_rand.mean())
print(x_rand.std(), y_rand.std())
df = pd.DataFrame({
    'x': x_rand,
    'y': y_rand
})
print(df.head())

x = df['x']
y = df['y']

plt.hist2d(x, y, bins=(100, 100), cmap='plasma')#plt.cm.jet)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.title("2D Histogram")
plt.xlabel("x")
plt.ylabel("y")
plt.show()




