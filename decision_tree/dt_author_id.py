#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# calculate feature number of training data
import numpy as np
features_np_train = np.array(features_train)
feature_num = len(features_np_train[0])
print "feature number is",feature_num
#########################################################
### your code goes here ###
from sklearn import  tree
dt_clf = tree.DecisionTreeClassifier( min_samples_split=40)
dt_clf.fit(features_train,labels_train)

accuracy = dt_clf.score(features_test,labels_test)
print "accuracy is",accuracy

#########################################################


