import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid
import random
from colorsys import hsv_to_rgb

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

    def is_peak(i):  # 앞 뒤 xscale개를 보고 peak인지 아닌지 판단한다

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

def get_params(*params):
    n = len(params) // 3

    a = params[:n]
    mu = params[n:2 * n]
    sigma = params[2 * n:]

    return a, mu, sigma

# 여러 gaussian을 더한 함수 반환
def fit_func(x, *params):
    a, mu, sigma = get_params(*params)
    result = np.zeros_like(x, dtype=float)

    for i in range(len(a)):
        result += particle(x, a[i], mu[i], sigma[i])

    return result

x_peaks = get_peak(bins, count)
peak_count = len(x_peaks)
print("peak의 x값들 = ", x_peaks)
basic_param = np.ones(peak_count)

p0 = np.concatenate([
    800 * basic_param,
    x_peaks,
    basic_param
])

lower_bound = [0, 0, 0.6, 1.5, 0.05, 0.05]
upper_bound = [1500, 1500, 3, 3, 3, 3]

params, _ = curve_fit(
                fit_func,
                bins, count,
                p0=p0,
                bounds=(lower_bound, upper_bound)
             )

a_fit, mu_fit, sigma_fit = get_params(*params)

particle_counts = [particle(bins, a_fit[i], mu_fit[i], sigma_fit[i]) for i in range(peak_count)]
print("(peak count, data count) =", np.shape(particle_counts))  # (peak count, data 개수)

N = [trapezoid(pcount, x=bins) for pcount in particle_counts]   # 각 particle에 대한 fitting curve 전체 적분

N_text = " : ".join([f"{N_i:.3f}" for N_i in N])
N_ratio_text = " : ".join([f"{N_i/N[0]:.3f}" for N_i in N])
N_symbol_text = " : ".join([fr"$N_{i + 1}$" for i in range(peak_count)])

result_text = f"{N_symbol_text} = {N_text} = {N_ratio_text}"
print(result_text)

plt.figure(figsize=(8,2))
plt.axis("off")
plt.text(0.5, 0.5,
         result_text,
         fontsize=20,
         ha="center",
         va="center",
         linespacing=1.8)
plt.show()

# 그림 그리는 부분 ---------------------------------------------------------------------
prev_h = None
for i in range(peak_count):
    h = None    # 색깔
    while True: # 비슷한 색 방지
        h = random.random()
        if prev_h is None or min(abs(h - prev_h), 1 - abs(h - prev_h)) > 0.3:
            break
    s = random.uniform(0.8, 1.0)    # 채도
    v = random.uniform(0.5, 0.7)    # 명도

    color = hsv_to_rgb(h, s, v)
    prev_h = h
    plt.plot(bins, particle_counts[i],
             label=fr"$\mu$={mu_fit[i]:.3f}, $\sigma$={sigma_fit[i]:.3f}",
             color=color,
             linestyle="dashdot")

plt.plot(bins, fit_func(bins, *params), color="red", linestyle="dashed", label="fit_curve(sum)")
plt.scatter(bins, count, c="k" , s=15, label="Raw data", zorder=10)
plt.xlabel("Energy")
plt.ylabel("Count")
plt.legend()
plt.show()