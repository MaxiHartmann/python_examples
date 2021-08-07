import numpy as np
import pandas as pd

filename='example_data_1.txt'

# find number of rows to skip
any_header_name = 'orifice'

n=0
with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
        if any_header_name in line:
            # print('found at line:'+ str(num))
            n=num-1

data = pd.read_csv(filename, delimiter="\t", skiprows=n)
# print(data)

# print(data.mean(axis=1))


# print columnnames
# print(data.columns)

# print(data.flow_rate)





# plotting
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(data.flow_rate, data.dp_1, label='A')
ax.plot(data.flow_rate, data.dp_2, label='B')
ax.set_xlim(0, 50)
ax.set_ylim(0, 220)


# polynomal fitting 
x= data.flow_rate
y1= data.dp_1
y2= data.dp_2

polyfit_y1 = np.polyfit(x,y1,3)
p1 = np.poly1d(polyfit_y1)
print("cubic regression curve for f1: \n")
print(p1)
polyfit_y2 = np.polyfit(x,y2,3)
p2 = np.poly1d(polyfit_y2)
print("cubic regression curve for f1: \n")
print(p2)

# finer discretization:
x=np.linspace(0,max(data.flow_rate)*2, 100)
ax.plot(x, p1(x), 'r-', linewidth=1, label=p1)
ax.plot(x, p2(x), 'g-', linewidth=1, label=p2)

# find intersection point:
from intersect_function import intersection
x,y = intersection(x, p1(x), x, p2(x))
print("Intersection point: %0.4f %0.4f" % (x, y))
ax.plot(x,y, '*k')

plt.legend()
plt.show()
