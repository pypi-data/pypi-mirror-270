"""
=====
Inset
=====
You can have an inset by adding another `TernaryAxes`.
"""
import numpy as np

import matplotlib.pyplot as plt
import mpltern


np.random.seed(seed=19)
t0, l0, r0 = np.random.dirichlet(alpha=(2.0, 2.0, 2.0), size=100).T

np.random.seed(seed=68)
t1, l1, r1 = np.random.dirichlet(alpha=(2.0, 2.0, 2.0), size=100).T

fig = plt.figure()
fig.subplots_adjust(left=-0.1)

ax = fig.add_subplot(projection="ternary")

ax.scatter(t0, l0, r0, alpha=0.5)
ax.scatter(t1, l1, r1, alpha=0.5)

# Plot the triangle region for the inset.
ax.fill([0.4, 0.3, 0.3], [0.3, 0.4, 0.3], [0.3, 0.3, 0.4], fc="none", ec="k")

# Create a new `TernaryAxes` for the inset with specifying a rectangle in the
# figure coordinates.
axins = fig.add_axes([0.625, 0.525, 0.30, 0.30], projection="ternary")

# Limit the ploting range to be consistent with the above plotted triangle.
axins.set_ternary_min(0.3, 0.3, 0.3)

axins.scatter(t0, l0, r0, alpha=0.5)
axins.scatter(t1, l1, r1, alpha=0.5)

plt.show()
