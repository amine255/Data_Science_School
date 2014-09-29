# coding: utf-8
"""
Created on Tue Sep 16 19:25:08 2014

@author: arda
"""
import numpy as np
from tools import *



####################################################       
#IMPORT DATA
####################################################
print "Importing data..."  
corpus_train = "Data/corpus.tache1.learn.utf8"
corpus2predict = "Data/corpus.tache1.test.utf8" 

####################################################       
#DATA MUNGING
####################################################
alltxts = Data_munging(corpus_train)


#########################################################
#DEFINE CLASSIFIER
#########################################################
#print "Defining classifier"
#
#from sklearn import svm
##X = [[0, 0], [1, 1]]
##y = [0, 1]
#clf = svm.LinearSVC(C=100)  # definition du classifieur
#
#print "Training parameters"
#clf.fit(dataSparse.T,labs)   # apprentissage
#
#
##########################################################
##EVALUATE CROSS VALIDATION
##########################################################
#print "Cross Validation..."  
#
#from sklearn import cross_validation
#
### usage basique: split train/test
#X_train, X_test, y_train, y_test = cross_validation.train_test_split( dataSparse.T, labs, test_size=0.4, random_state=0)
#
#scores = cross_validation.cross_val_score( clf, dataSparse.T, labs, cv=3)
#scores
#
##########################################################
##PREDICTING
##########################################################

