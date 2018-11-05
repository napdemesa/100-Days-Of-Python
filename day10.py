##MODEL PERSISTENCE IN SCIKIT-LEARN
from sklearn import svm
from sklearn import datasets

clf = svm.SVC(gamma = 'scale')
iris = datasets.load_iris()
X, y = iris.data, iris.target

print(clf.fit(X, y))

import pickle

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(X[0:1]))

print(y[0])

##CONVENTIONS
import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
print(X.dtype)

transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new.dtype)
