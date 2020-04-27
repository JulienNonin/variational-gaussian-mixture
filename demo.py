#%%
%load_ext autoreload
%autoreload 2

import numpy as np
from src.viGMM_full import VariationalGaussianMixture

#%%
X = np.loadtxt('data/faithful.txt')
X = (X - X.mean(axis=0)) / X.std(axis=0)

#%%
m_true = np.array([[0, 0], [3, -3], [3, 3], [-3, 3], [-3, -3]])
covs_true = np.array([[[1, 0], [0, 1]], [[1, 0.5], [0.5, 1]], [[1, -0.5], [-0.5, 1]], [[1, 0.5], [0.5, 1]], [[1, -0.5], [-0.5, 1]]])
X = np.concatenate([np.random.multivariate_normal(m_true[k], covs_true[k], 100) for k in range(len(m_true))])

#%%
model = VariationalGaussianMixture(K=10, display=True, max_iter=200, plot_period=20, init_param="kmeans")
model.fit(X)

# %%
