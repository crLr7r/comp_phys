import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x,y)
# plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc,x))

# plt.scatter(x,y, color="blue", label="Data Points")
# plt.plot(x,mymodel, color="red", label=f"Regression Line (r={r_value:.2f}, std_err={std_err:.2f})")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Linear Regression Plot")
# plt.show()

prediction = myfunc(10)
print(prediction)

#-------------------------------------------------------------
import numpy as np
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# plt.scatter(x,y)
# plt.show()

coefs = np.polyfit(x,y,3)
coefs_refined = [round(coef,3).item() for coef in coefs]

mymodel = np.poly1d(coefs)

myline = np.linspace(1,22,100)

r2 = r2_score(y, mymodel(x))

# plt.scatter(x,y, color="blue", label="Data Points")
# plt.plot(myline, mymodel(myline), color="red",
#          label=fr"Regression Line ($R^2$={r2:.2f})"
#                +f"\nW={coefs_refined}")
#
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title(r"Polynomial Regression with $R^2$ Score")
# plt.legend()
# plt.legend()
# plt.show()

#------------------------------------------------------------------
N = 100
x = np.linspace(0,2*np.pi,N).reshape(N,1)

np.random.seed(1)
y = np.sin(x)
y += 0.3*np.random.rand(N,1)

print(x.shape)
print(y.shape)

plt.scatter(x,y)
plt.plot(x, np.sin(x))
plt.title("Sine wave noise data")
plt.show()
