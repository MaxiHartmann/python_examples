import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# import experimental data
data = pd.read_csv('pseudo_exp.csv')
print(data)
x=data.x
y1=data.y1
y2=data.y2


# Plotting
fig, ax = plt.subplots()
ax.plot(x,y1, 'r.', label='performance curve')
ax.plot(x,y2, 'g.', label='throttle')
ax.set_xlim(0,50)
ax.set_ylim(0,220)

ax.set_xlabel('flow rate [l/s]')
ax.set_ylabel('pressure difference [hPa]')

# polynomal fitting 
polyfit_y1 = np.polyfit(x,y1,3)
p1 = np.poly1d(polyfit_y1)
print("cubic regression curve for f1: \n")
print(p1)
polyfit_y2 = np.polyfit(x,y2,3)
p2 = np.poly1d(polyfit_y2)
print("cubic regression curve for f1: \n")
print(p2)

ax.plot(x, p1(x), 'r-', linewidth=1, label=p1)
ax.plot(x, p2(x), 'g-', linewidth=1, label=p2)

plt.legend()

# find intersection point:
from intersect_function import intersection
x,y = intersection(x, p1(x), x, p2(x))

print("Intersection point: %0.4f %0.4f" % (x, y))

plt.plot(x,y, '*k')


plt.show()
