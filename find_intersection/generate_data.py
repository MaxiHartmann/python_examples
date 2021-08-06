import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


points = 15
c=200.
a=-c/(45*45)
d=250/(45*45)
x=np.linspace(0,50, points)
y1=a*x*x+c
y2=d*x*x

# let y fluctuate:
noise=np.random.normal(0, 5.0, y1.shape)
y1 = y1+noise
noise=np.random.normal(0, 2.0, y2.shape)
y2 = y2+noise

fig, ax = plt.subplots()
ax.plot(x,y1, 'r.-', label='performance curve')
ax.plot(x,y2, 'g.-', label='throttle')
ax.set_xlim(0,50)
ax.set_ylim(0,220)

ax.plot(x,y1, 'r.-', label='performance curve')

ax.set_xlabel('flow rate [l/s]')
ax.set_ylabel('pressure difference [hPa]')

# np.savetxt('pseudo_exp.csv', (x,y1,y2), fmt='%1.4e', delimiter=', ')
pd.DataFrame({'x': x, 'y1': y1, 'y2': y2}).to_csv('pseudo_exp.csv', index=False)
plt.show()
