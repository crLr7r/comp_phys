import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(0,2*np.pi,N).reshape(N,1)

np.random.seed(1)
y = np.sin(x)
y += 0.3*np.random.rand(N,1)

print(x.shape)
print(y.shape)

# plt.scatter(x,y)
# plt.plot(x, np.sin(x))
# plt.title("Sine wave noise data")
# plt.show()

# 데이터 전처리--------------------------------------------------------
np.random.seed(10)
idx = np.random.permutation(N)
# print(idx)

shuffle_x = x[idx]
shuffle_y = y[idx]

print(shuffle_x[:3])
print(shuffle_y[:3])

n = int(N * (3/4))

x_train = shuffle_x[:n]
y_train = shuffle_y[:n]

x_test = shuffle_x[n:]
y_test = shuffle_y[n:]

# plt.scatter(x_train, y_train, label='train')
# plt.legend()
# plt.title('sine wave train data')
# plt.show()
#
# plt.scatter(x_test, y_test, label='test')
# plt.legend()
# plt.title('sine wave test data')
# plt.show()

# linear regression 시도------------------------------------
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x_train, y_train)

print('w0: ', reg.intercept_)
print('w1: ', reg.coef_)
Pred = reg.predict(x_train)

# plt.figure()
# plt.scatter(x_train, Pred, label='pred')
# plt.scatter(x_train, y_train, label='target')
# plt.legend()
# plt.title('train data')
# plt.show()
#
# plt.figure()
# plt.scatter(x_test, reg.predict(x_test), label='pred')
# plt.scatter(x_test, y_test, label='target')
# plt.legend()
# plt.title('test data')
# plt.show()

# Polynomial Regression--------------------------------------------
from sklearn.preprocessing import PolynomialFeatures

N = 100

x = np.linspace(0, 2*np.pi, N).reshape(N,1)

y = np.sin(x)
y += 0.3*np.random.rand(N,1)

polynomial = PolynomialFeatures(degree=3, include_bias=False)
sin_new_feature = polynomial.fit_transform(x)

np.random.seed(10)
idx = np.random.permutation(N)
# print(idx)

shuffle_x = sin_new_feature[idx]
shuffle_y = y[idx]

print(shuffle_x[:3])
print(shuffle_y[:3])

n = int(N * (3/4))

x_train = shuffle_x[:n]
y_train = shuffle_y[:n]
print(x_train.shape)
print(y_train.shape)

x_test = shuffle_x[n:]
y_test = shuffle_y[n:]

reg = LinearRegression()
reg.fit(x_train, y_train)

print('w0: ', reg.intercept_)
print('w1: ', reg.coef_)

Pred = reg.predict(x_train)

plt.figure()
plt.scatter(x_train[:,0], Pred, label='pred')
plt.scatter(x_train[:,0], y_train, label='target')
plt.legend()
plt.title('train data')
plt.show()

test_Pred = reg.predict(x_test)

plt.figure()
plt.scatter(x_test[:,0], test_Pred, label='pred')
plt.scatter(x_test[:,0], y_test, label='target')
plt.legend()
plt.title('test data')
plt.show()

x_all = shuffle_x[:]
y_all = shuffle_y[:]

all_Pred = reg.predict(x_all)

plt.figure()
plt.scatter(x_all[:,0], all_Pred, label='pred')
plt.scatter(x_all[:,0], y_all, label='target')
plt.legend()
plt.title('all data')
plt.show()

