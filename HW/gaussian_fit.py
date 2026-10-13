import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

HOME = os.path.abspath(os.path.dirname(__file__))

# 데이터 읽어들이기
bins, count = [], []
with open("hist2.csv", "r") as f:
    for line in f.readlines():
        _b, _c = [float(i) for i in line.split(",")]
        bins.append(_b)
        count.append(_c)
bins = np.asarray(bins)
count = np.asarray(count)

# 모델 함수
def particle(x, a, mu, sigma):
    return a * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# 주어진 함수에서 peak에 대응하는 x값, y값을 저장한 list 반환
def get_peak(x, ylist, xscale=5):
    ylist_len = len(ylist)
    yscale = max(ylist) - min(ylist)

    def idx(i):
        if i < 0:
            return 0
        elif i >= ylist_len:
            return ylist_len - 1
        else:
            return i

    def is_decrease(i, j):
        i, j = idx(i), idx(j)
        if i == j: return 1  # j가 실제 인덱스가 아닐 때 --> 그래프가 끝까지 증가할 시 끝점도 peak으로 인정
        if ylist[i] - ylist[j] > yscale / 50:
            return 1  # 의미 있는 감소를 했을 때
        elif ylist[i] > ylist[j]:
            return 0.5  # 작지만 감소는 했을 때
        else:
            return -1  # 감소도 안 했을 때

    def is_peak(i):  # 앞 뒤 3개를 보고 peak인지 아닌지 판단한다

        is_left_decrease = 0
        is_right_decrease = 0

        for j in range(xscale):
            is_left_decrease += is_decrease(i, i - (j+1))
            is_right_decrease += is_decrease(i, i + (j+1))

        is_left_decrease = is_left_decrease > xscale - 1
        is_right_decrease = is_right_decrease > xscale - 1

        return is_left_decrease and is_right_decrease

    x_peaks = []

    for i in range(ylist_len):
        if is_peak(i): x_peaks.append(x[i])

    return x_peaks

# 여러 gaussian을 더한 함수 반환
def fit_func(x, *params):
    n = len(params) // 3

    a = params[:n]
    mu = params[n:2*n]
    sigma = params[2*n:]

    result = np.zeros_like(x, dtype=float)

    for i in range(n):
        result += particle(x, a[i], mu[i], sigma[i])

    return result

x_peaks = get_peak(bins, count)
peak_count = len(x_peaks)
print(x_peaks)
basic_param = np.ones(peak_count)
p0 = np.concatenate([
    basic_param,
    x_peaks,
    basic_param
])

params, _ = curve_fit(
                fit_func,
                bins, count,
                p0=p0
            )

plt.plot(bins, fit_func(bins, *params), color="red", linestyle="dashed")
plt.scatter(bins, count, c="k")
plt.show()