import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tikzplotlib

import matplotlib as mpl
mpl.rc('lines', linewidth=2, color='g', markersize=1)

# example 1
data = pd.read_csv('0.9_0.000000', sep='\s+')
data = data.head(1000)
plt.figure(0)
plt.xscale('log')
plt.rc('text', usetex=True)
plt.xlabel(r'$y^+$')
plt.ylabel(r'$u^+$')
plt.xlim(1e-1, 1e4)
plt.ylim(0, 30)

tikzplotlib.clean_figure()
plt.plot(data['yplus'], data['uplus'], linestyle='-', marker='.', color='black', label='sim')

tikzplotlib.save("data/example1.tex", standalone=True, externalize_tables=True,override_externals=True,axis_width='\\figW',axis_height='\\figH' )

# example 2
plt.figure(1)
plt.xscale('log')
plt.rc('text', usetex=True)
plt.xlabel(r'$y^+$')
plt.ylabel(r'$u^+$')
plt.xlim(1e-1, 1e4)
plt.ylim(0, 30)

plt.plot(data['yplus'], data['tplus'], label='plot2')

tikzplotlib.save("data/example2.tex", standalone=True, externalize_tables=True,override_externals=True,axis_width='\\figW',axis_height='\\figH' )

# example 3
# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x, y)
ax2.plot(x, y**2, 'tab:orange')
ax3.plot(x, -y, 'tab:green')
ax4.plot(x, -y**2, 'tab:red')

for ax in fig.get_axes():
    ax.label_outer()

tikzplotlib.save("data/example3.tex", standalone=True, externalize_tables=True,override_externals=True,axis_width='\\figW',axis_height='\\figH' )

# example 4
fig, axs = plt.subplots(3, sharex=True, sharey=True)
axs[0].plot(x, y ** 2)
axs[1].plot(x, 0.3 * y, 'o')
axs[2].plot(x, y, '+')

tikzplotlib.save("data/example4.tex", standalone=True, externalize_tables=True,override_externals=True,axis_width='\\figW',axis_height='\\figH' )

# example 5
plt.figure(5)
plt.xscale('log')
plt.rc('text', usetex=True)
plt.xlabel(r'$y^+$')
plt.ylabel(r'$u^+$')
plt.xlim(1e-1, 1e4)
plt.ylim(0, 30)
x = np.logspace(1e-1,4,100)
y = x

plt.plot(x, y, linestyle='-', marker='.', color='black', label='viscous')
plt.plot(data['yplus'], data['uplus'], linestyle='-', marker='.', color='black', label='sim')
plt.legend()

tikzplotlib.clean_figure()
tikzplotlib.save("data/example5.tex", standalone=True, externalize_tables=True,override_externals=True,axis_width='\\figW',axis_height='\\figH' )
