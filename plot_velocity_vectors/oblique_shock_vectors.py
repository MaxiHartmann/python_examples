import numpy as np
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
pi=np.pi

origin = [0, 0]

beta = 20. * pi/180.
sigma = 29.8009155 * pi/180.

M1 = 5.0
M1n = M1 * np.sin(sigma)
M1t = np.sqrt(M1 * M1 - M1n * M1n)

M2 =  3.02215162
M2n = M2 * np.sin(sigma-beta)
M2t = np.sqrt(M2 * M2 - M2n * M2n)

fig, ax = plt.subplots()

# plot wall boundary
h=np.sin(beta)
wall_xcoords = [-1.5, 0, 1, 2, 2, -1.5, -1.5]
wall_ycoords = [0, 0, h, h, 3, 3, 0]
ax.plot(wall_xcoords, wall_ycoords, color='k') 

# plot shock
shock_xcoords = [0, 2]
shock_ycoords = [0, np.sin(sigma)*2]
ax.plot(shock_xcoords, shock_ycoords, color='gray', linestyle='--') 




# Before Shock
x_pos = -M1/3
y_pos = h/2
x_direct = M1/3
y_direct = 0

# Mach1
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='k', scale=1)

# Mach1 normal
ax.quiver(x_pos, y_pos, M1n*np.sin(sigma), -M1n*np.cos(sigma), units='xy', color='b', scale=3)
ax.quiver(x_pos, y_pos, M1t*np.cos(sigma), M1t*np.sin(sigma), units='xy', color='y', scale=3)

ax.set_title('Machnumber relations for oblique shock')
ax.grid(linestyle=':')
ax.axis('equal')

ax.set_xlim(-2, 4)
ax.set_ylim(-2, 4)

plt.show()
