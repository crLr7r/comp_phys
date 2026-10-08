import numpy as np

def trap1(f, a, b, n=100):
    sm = 0
    integral_values = [0]
    x = np.linspace(a, b, n)

    for i in range(len(x)-1):
        area = (f(x[i]) + f(x[i+1]))/2 * (x[i+1] - x[i])
        sm += area
        integral_values.append(sm)

    return x, integral_values