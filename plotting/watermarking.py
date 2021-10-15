import numpy as np
import matplotlib.pyplot as plt

def watermarking(ax):
    ax.text(1.0, 0.0, 'created by Max H.\nat XXX', transform=ax.transAxes,
            fontsize=10, color='gray', alpha=0.5,
            ha='right', va='bottom', rotation='0')

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=10, lw=2, alpha=0.7, mfc='red')
ax.grid()

watermarking(ax)

plt.savefig('watermarking.png')

plt.show()
