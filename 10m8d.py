import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

# 적분: 직접 함수 작성 vs scipy모듈 사용--------------------------------
h = 0.01
min_x = 1
max_x = 5

def f(x):
    return 3 * x ** 2 + 2 * x + 6

def int_f(func, x_min, x_max, h):
    output = 0
    x = np.arange(x_min, x_max + h, h)
    for idx in range(len(x) - 1):
        output += (func(x[idx]) + func(x[idx + 1])) * h / 2
    return output

x = np.linspace(0, 8)
x_inf = np.arange(min_x, max_x + h, h)
y_inf = f(x_inf)

x_inf = np.concatenate(([x_inf[0]], x_inf, [x_inf[-1]]))
y_inf = np.concatenate(([0], y_inf, [0]))

I_1 = int_f(f, min_x, max_x, h)
I_2 = trapezoid(f(x_inf), x_inf, h)
print(type(I_1))
print(type(I_2))

plt.plot(x, f(x))
plt.fill(x_inf, y_inf, "r", alpha=0.5)
plt.text(0.1, 55, f"TZ int: {I_1:.3f}")
plt.text(0.1, 65, f"SCIPY: {I_2:.3f}")
plt.grid(True)
plt.xlim(0, 8)
plt.ylim(0, 200)
plt.show()

# concatenate 개념 배우기 --------------------------------------------
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.concatenate((arr1, arr2))
print(result)

arr3 = np.array([[1,2], [3,4]])
arr4 = np.array([[5,6], [7,8]])
result_axis0 = np.concatenate((arr3, arr4), axis=0)
result_axis1 = np.concatenate((arr3, arr4), axis=1)
print(f"concatenate_axis0: \n{result_axis0}")
print(f"concatenate_axis1: \n{result_axis1}")

# 직접 모듈 만들기 ----------------------------------------------------
from Trap1_function import trap1

def f(t):
    return t * np.cos(t)

t, y = trap1(f, 0., 50)#4*np.pi)

plt.plot(t, y, label="Integral of f(t)")
plt.plot(t, f(t), label="f(t)", linestyle="--")
plt.legend()
plt.xlabel("t")
plt.ylabel("Value")
plt.title("Plot of f(t) and its integral over time")
plt.grid(True)
plt.show()

