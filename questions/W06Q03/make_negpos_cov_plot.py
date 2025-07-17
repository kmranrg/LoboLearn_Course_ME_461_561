# ---------------------------------------------------------------
# make_negpos_cov_plot.py
# ---------------------------------------------------------------
# Creates an image with two side-by-side scatter plots:
#   Plot (A) = strong NEGATIVE covariance   (rho = -0.8)
#   Plot (B) = strong POSITIVE covariance   (rho =  +0.8)
# Save as gp_cov_negpos.png  (white background, teal points).
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Reproducible RNG
rng = np.random.default_rng(seed=2025)

mu = np.zeros(2)

rho_neg = -0.8
Sigma_neg = np.array([[1.0, rho_neg],
                      [rho_neg, 1.0]])

rho_pos =  0.8
Sigma_pos = np.array([[1.0, rho_pos],
                      [rho_pos, 1.0]])

N = 1000
data_A = rng.multivariate_normal(mu, Sigma_neg, size=N)   # negative corr
data_B = rng.multivariate_normal(mu, Sigma_pos, size=N)   # positive corr

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

fig.patch.set_facecolor("white")
plt.tight_layout()
fig.savefig("gp_cov_negpos.png", dpi=150, facecolor="white")
plt.show()
