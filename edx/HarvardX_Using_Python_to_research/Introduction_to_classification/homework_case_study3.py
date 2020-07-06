import numpy as np, random, scipy.stats as ss
import pandas as pd

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

def accuracy(predictions, outcomes):
    return 100*np.mean(predictions == outcomes)

with open("wine.csv", "r") as f:
    text_file = pd.read_csv(f)


text_file["is_red"]=(text_file["color"] == "red").astype(int)
numeric_data = text_file.drop(["color", "high_quality", "quality"], axis=1)

print(numeric_data)
print(numeric_data.groupby('is_red').count())

import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns=numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(text_file.loc[:,numeric_data.columns].values)
principalDf = pd.DataFrame(data = principal_components
             , columns = ['principal component 1', 'principal component 2'])
print(pca)
print(principal_components)
#print(principalDf)
#print(principal_components.shape)


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = text_file['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
#plt.show()


import numpy as np
np.random.seed(1) # do not change this!

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)

print(accuracy(x, y))
print(accuracy(0, text_file["high_quality"]))


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, text_file['high_quality'])
library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, text_file["high_quality"]))

n_rows = text_file.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)
print(selection[9])


predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(text_file["high_quality"])

my_predictions = np.array([knn_predict(p, predictors[training_indices,:], outcomes[training_indices], k=5) for p in predictors[selection]])
#print(my_predictions)
#print(text_file.high_quality.iloc[selection])
#print(library_predictions)
#print(text_file["high_quality"])

percentage = accuracy(my_predictions, text_file.high_quality.iloc[selection])
print(percentage)
