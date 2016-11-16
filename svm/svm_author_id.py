#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

#take 1% training data
#labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn import svm
#clf = svm.SVC(kernel="linear")
clf = svm.SVC(C =10000.0,kernel="rbf")

clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print "acuuracy is :",accuracy
#########################################################
acu1 = clf.predict(features_test[10])
print acu1
print  clf.predict(features_test[26])
print  clf.predict(features_test[50])

#predict how much sample belong to chris
result =  clf.predict(features_test)
import numpy as np
chris_num = np.sum(result)
print chris_num


