import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import matplotlib as mpl
mpl.rc('lines', linewidth=2, color='g', markersize=1)

x097data = pd.read_csv('0.9_0.000000', sep='\s+')

xc = np.mean(x097data['xc'])
rho = x097data['rho_TL_0']
mu = x097data['mu']
dwall = x097data['dwall']
vx = x097data['vx']
vz = x097data['vz']
idx2 = int(x097data['vx'].size - 4)
# V = np.sqrt(vx**2 + vz**2)
Uref = vx.values[idx2]
rhoref = rho.values[idx2]
muref = mu.values[idx2]

print(Uref)

Uref99 = Uref * 0.99

idxDelta = 0
for v in vx:
    diff2 = Uref99 - v
    if (diff2 > 0.0):
        idxDelta += 1

# boundaryLayerThickness        
delta = x097data['zc'].values[idxDelta]

# momentum thickness
# compressible: 
# see: https://turbmodels.larc.nasa.gov/flatplate_val.html

theta = 0
for x in range(0, idxDelta):
    dy = dwall[x+1] - dwall[x]
    theta += rho[x]/ rhoref * vx[x]/Uref * (1 - vx[x]/Uref) * dy
    

Re_theta = rhoref * Uref * theta / muref
Re_x = rhoref * Uref * xc / muref

print('delta    = %e ' % (delta))
print('Re_theta = %e ' % (Re_theta))
print('Re_x     = %e ' % (Re_x))
