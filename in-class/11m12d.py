from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1, 11).reshape(10,1)
y = np.array([7,8,7,13,16,15,19,23,18,21]).reshape(10,1)
# plt.plot(x,y, 'ro')
# plt.ylim(0,30)
# plt.show()

# 1차원 regression --------------------------------------------
reg = LinearRegression()
reg.fit(x, y)
w0 = reg.intercept_
w1 = reg.coef_

print('w0: ', w0)
print('w1: ', w1)

y_pred = reg.predict(x)

# plt.plot(x, y, 'ro')
# plt.plot(x, y_pred)
# plt.title('1D regression')
# axes = plt.gca()
# axes.set_xlim(0,11)
# axes.set_ylim(0, 30)
# plt.show()

# 2차원 regression---------------------------------------------
x_2 = np.c_[x, x**2]    # 각 요소를 열벡터로 취급함
reg.fit(x_2, y)
w0 = reg.intercept_
w = reg.coef_
print('w0: ', w0, 'w: ', w)

y_pred = reg.predict(x_2)

# plt.plot(x, y, 'ro')
# plt.plot(x, y_pred)
# plt.title('2D regression')
# axes = plt.gca()
# axes.set_xlim(0,11)
# axes.set_ylim(0, 30)
# plt.show()

# 3차원 regression --------------------------------------------
x_3 = np.c_[x, x**2, x**3]
# 또는(라이브러리 내장 함수 이용)
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3, include_bias=False)
x_3 = poly.fit_transform(x)

reg.fit(x_3, y)
w0 = reg.intercept_
w = reg.coef_
print('w0: ', w0, 'w: ', w)
y_pred = reg.predict(x_3)

# plt.plot(x, y, 'ro')
# plt.plot(x, y_pred)
# plt.title('3D regression')
# axes = plt.gca()
# axes.set_xlim(0,11)
# axes.set_ylim(0, 30)
# plt.show()

x_temp = np.array([2,4,8])
print(w.reshape(-1,1))  # -1: 행의 개수를 자동으로 계산
print(w.T)  # 위랑 같은 값
y_temp = x_temp @ w.reshape(-1,1) + w0
print(y_temp)
y_temp = w @ x_temp.T + w0
print(y_temp)

# fitting curve 예쁘게 그리기----------------------------------------------
x_line = np.arange(-5, 15, 0.01).reshape(-1, 1)
poly = PolynomialFeatures(degree=3, include_bias=False)
x_line_3 = poly.fit_transform(x_line)
y_line_pred = x_line_3 @ w.reshape(-1,1) + w0
print(x_line_3.shape)
print(y_line_pred.shape)

plt.plot(x, y, 'ro')
plt.plot(x_line, y_line_pred, color='orange')
plt.title("smooth fit curve")
axes = plt.gca()
axes.set_xlim(0,11)
axes.set_ylim(0, 30)
plt.show()
