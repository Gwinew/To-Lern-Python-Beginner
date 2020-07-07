import numpy as np
import pandas as pd

with open("whiskies.txt", "r") as f:
	whisky = pd.read_csv(f)
with open("regions.txt", "r") as f:
	whisky["Region"] = pd.read_csv(f)

whisky.head()
whisky.tail()

whisky.iloc[0:10]

whisky.iloc[5:10, 0:5]

whisky.columns


flavors = whisky.iloc[:, 2:14]

# Exploring Correlations

corr_flavors = pd.DataFrame.corr(flavors)

print(corr_flavors)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")


corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
# plt.axis("tight")  # Do this for make tighter plot with values (90 to 86 values)
plt.colorbar()
plt.savefig("corr_whisky.pdf")

# Clustering whiskies by flavor profile with scikit-learn machine learning

# Spectral co-clustering ; eigenvalues and eigenvectors

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)

model.fit(corr_whisky)

model.rows_  #  number of row clusters times number of rows in the data matrix

np.sum(model.rows_, axis=1)  # axis=0 is rows, axis=1 is columns output: array([20,5,19,17,6,19]) - cluster 0,1,2 and so on e.g. 19 is cluster 2

np.sum(model.rows_, axis=0)  # array([1,1,1,...,1,1,1])


model.row_labels_  # array([5,2,3,4...,2,0,2,0], dtype=int32)  observation number 0 belong to cluster number 5, number 1 to cluster number 2 and so on



# Camparing correlation matrices

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)

whisky = whisky.iloc[np.argsort(model.row_labels_)]  # ix has been deprecated in the latest Pandas version. You might want to use .iloc instead.

whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())

correlations = np.array(correlations)


plt.figure(figsize = (14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")
