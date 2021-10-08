import numpy as np
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
from numpy import sin, cos, tan, pi


# INPUTS
M1 = 3.0
beta = 20. * pi/180.



sigma =  37.7636341 * pi/180.

M1n = M1 * sin(sigma)
M1t = M1 * cos(sigma)

M2 =  1.99413166
M2n = M2 * sin(sigma-beta)
M2t = M2 * cos(sigma-beta)

# attention:    v1t == v2t,
# but           M1t =! M2t, 
# cause a1 =! a2 and T1 =! T2

fig, ax = plt.subplots()

# plot wall boundary
ramp_length=2
h = tan(beta)*ramp_length
right_bound = 10
wall_xcoords = [-5, 0, ramp_length, right_bound]
wall_ycoords = [0, 0, h, h]
ax.plot(wall_xcoords, wall_ycoords, color='k') 

# plot shock
shock_xcoords = [0, 10*cos(sigma)]
shock_ycoords = [0, 10*sin(sigma)]
ax.plot(shock_xcoords, shock_ycoords, color='gray', linestyle='-', lw=0.5) 

# origin should be on shock line
orig_x = 2
origin=[orig_x,orig_x*tan(sigma)]


# plot: M1
x_pos = origin[0] - M1
y_pos = origin[1]
x_direct = M1
y_direct = 0
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='g', scale=1, label='Ma')
# plot: M1n
x_direct = M1n*sin(sigma)
y_direct = -M1n*cos(sigma)
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='b', scale=1, label='Ma_n')
# plot: M1t
x_pos = x_pos + M1n*sin(sigma)
y_pos = y_pos - M1n*cos(sigma)
x_direct = M1t*cos(sigma)
y_direct = M1t*sin(sigma)
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='y', scale=1, label='Ma_t')

# Mach2
x_pos = origin[0]
y_pos = origin[1]
x_direct = M2*cos(beta)
y_direct = M2*sin(beta)
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='g', scale=1)
# plot: M2n
x_pos = origin[0]+M2t*cos(sigma)
y_pos = origin[1]+M2t*sin(sigma)
x_direct = M2n*sin(sigma)
y_direct = -M2n*cos(sigma)
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='b', scale=1)
# plot: M2t
x_pos = origin[0]
y_pos = origin[1]
x_direct = M2t*cos(sigma)
y_direct = M2t*sin(sigma)
ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='y', scale=1)

ax.set_title('Machnumber relations for oblique shock')
# ax.grid(linestyle=':')
ax.axis('equal')
# ax.set_xlim(-2, 3)
# ax.set_ylim(0, 3)
ax.legend()

plt.show()
