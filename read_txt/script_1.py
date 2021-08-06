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
ax.legend()
ax.set_xlim(0, 50)
ax.set_ylim(0, 220)
plt.show()
