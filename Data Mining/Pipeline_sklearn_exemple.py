# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 19:02:25 2014

@author: arda
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA


#########################################################
#IMPORT DATA
#########################################################
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target



#########################################################
#DEFINE CLASSIFIER
#########################################################
from sklearn import svm

#X = [[0, 0], [1, 1]]
#y = [0, 1]
clf = svm.SVC() # definition du classifieur
clf.fit(X, Y) # apprentissage
clf.predict([[2., 2.]]) # usage sur une nouvelle donnée





#########################################################
#EVALUATE
#########################################################
from sklearn import svm
from sklearn import cross_validation


# usage basique: split train/test
X_train, X_test, y_train, y_test = cross_validation.train_test_split( iris.data, iris.target, test_size=0.4, random_state=0)

# usage en boucle implicite
# le classifieur est donné en argument, tout ce fait implicitement (possibilité de paralléliser avec @@n_jobs@@)
scores = cross_validation.cross_val_score( clf, iris.data, iris.target, cv=5)
print scores

## boucle explicite (pour les traitements plus complexe)
#skf = cross_validation.StratifiedKFold(labels, nFolds)
#for train, test in skf:
#    train # contient les indices de train
#    test # contient les indices de test