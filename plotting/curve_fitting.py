import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# One way to perform an curve fitting with an self-defined function and scipy:


# Here exponential function
# first parameter must be x
# a,b,c will be optimized
def func_exp(x, a, b, c):
    return a * np.exp(-b * x) + c

def func_lin(x, a, b):
    return a * x + b


x = np.linspace(0,4,50)
y = func_exp(x, 2.5, 1.3, 0.5)
yn = y + 0.2*np.random.normal(size=len(x))

popt, pcov = curve_fit(func_exp, x, yn)
print(popt)
[a, b, c] = popt

# Plotting:
plt.figure()
plt.plot(x, yn, 'ko', label="Original Noised Data")
plt.plot(x, func_exp(x, *popt), 'r-', label="Fitted Curve: exp")
textstr = '\n'.join((
    r'$f(x)=ae^{-bx}+c$',
    r'$a={:.02f}, b={:.02f}, c={:.02f}$'.format(a,b,c)))
props = dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=1.0)
plt.text(2.0, 2.0, textstr, fontsize=10, bbox=props)


popt, pcov = curve_fit(func_lin, x, yn)
print(popt)
[a, b] = popt
plt.plot(x, func_lin(x, *popt), 'g-', label="Fitted Curve: lin")
textstr = '\n'.join((
    r'$f(x)=ax+b$',
    r'$a={:.02f}, b={:.02f}$'.format(a,b)))
props = dict(boxstyle='round', facecolor='white', edgecolor='green', alpha=1.0)
plt.text(2.0, 1.5, textstr, fontsize=10, bbox=props)

plt.legend()
plt.savefig('curve_fitting.png')
plt.show()
