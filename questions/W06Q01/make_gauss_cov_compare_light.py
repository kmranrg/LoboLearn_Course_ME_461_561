# ---------------------------------------------------------------
# make_gauss_cov_compare_light.py
# ---------------------------------------------------------------
# Creates two 1 000-sample scatter plots from bivariate Gaussians:
#   • Plot (A)  – strong positive covariance
#   • Plot (B)  – weak covariance
# Image saved on a white background so it’s easy to embed in HTML.
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# 1) reproducible RNG
rng = np.random.default_rng(seed=42)

# 2) means & covariance matrices
mu = np.array([0.0, 0.0])

rho_strong = 0.9          # large off-diag
Sigma_strong = np.array([[1.0, rho_strong],
                         [rho_strong, 1.0]])

rho_weak   = 0.2          # small off-diag
Sigma_weak = np.array([[1.0, rho_weak],
                       [rho_weak, 1.0]])

# 3) sample data
N = 1000
data_A = rng.multivariate_normal(mu, Sigma_strong, size=N)
data_B = rng.multivariate_normal(mu, Sigma_weak,   size=N)

# 4) plotting on white background
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)

for ax, d, title in zip(axes,
                        [data_A, data_B],
                        ["Plot (A)", "Plot (B)"]):
    ax.scatter(d[:, 0], d[:, 1],
               s=10, alpha=0.65,
               color="teal", edgecolors="teal")
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(r"$Y_1$")
    ax.set_ylabel(r"$Y_2$")
    ax.set_aspect("equal")

fig.patch.set_facecolor("white")         #  ← overall white canvas
plt.tight_layout()

# 5) save
fig.savefig("gp_cov_compare_light.png", dpi=150, facecolor="white")
plt.show()
