import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tikzplotlib

import matplotlib as mpl
mpl.rc('lines', linewidth=2, color='g', markersize=1)

cases = []
cases.append('35x25')
cases.append('69x49')
cases.append('137x97')
cases.append('273x193')
cases.append('545x385')


plt.figure(0)
plt.xlabel(r'$Re_x$')
plt.ylabel(r'$C_f$')
plt.xlim(0,1e7)
plt.ylim(0.002,0.006)

for case in cases:
    path='/home/max/hartmann/masterthesis/finalSimulations/sst_plate/plate_' + case + '_sst/'
    x097data = pd.read_csv(path + '/0.9_0.000000', sep='\s+')
    wallData = pd.read_csv(path + '/x_walldata_0.000000', sep='\s+')
    dwall = wallData['dwall']
    yplus = wallData['yplus']
    mu = wallData['mu']
    rho = wallData['rho_TL_0']
    nu = mu / rho

    utau = yplus * nu / dwall
    tau_w = utau * utau * rho
    idx2 = int(x097data['vx'].size - 4)
    vxin = x097data['vx'].values[idx2]
    vzin = x097data['vz'].values[idx2]
    Uref = np.mean(np.sqrt(vxin**2+vzin**2))
    rhoref = x097data['rho_TL_0'].values[idx2]
    Cf = tau_w / (0.5 * rhoref * Uref * Uref)
    Rex = wallData['xc'] * Uref / nu
    # plt.plot(wallData['xc'], Cf, label=case)
    plt.plot(Rex, Cf, label=case)

nu = np.mean(nu)
data8 = pd.read_csv('/home/max/hartmann/masterthesis/simulations/flatplate/postProcess/nasa_data/skinFriction_cfl3d.dat', sep='\s+')
data8 = data8.head(1000)
plt.plot(data8['x']*Uref/nu, data8['cf'], label='cfl3d')

plt.legend()
# tikzplotlib.clean_figure()
tikzplotlib.save("data/skinFriction.tex", standalone=True, externalize_tables=True, override_externals=True, axis_width='\\figW', axis_height='\\figH')
# plt.show()
