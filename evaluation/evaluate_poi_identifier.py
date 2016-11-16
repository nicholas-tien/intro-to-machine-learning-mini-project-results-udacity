#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### your code goes here 

from sklearn.cross_validation import train_test_split
feature_train,feature_test,target_train,target_test = train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(feature_train,target_train )
print "accuracy is:",clf.score(feature_test,target_test)
print "predict result is:",clf.predict(feature_test)
print "how many people is in test set:",len(feature_test)
# print "target test data is:",target_test
# print (29-4)/float(29)

from sklearn.metrics import confusion_matrix,recall_score
print "confusion matrix is:"
print confusion_matrix(target_test,clf.predict(feature_test))

from sklearn.metrics import precision_score
print "precision score is:",precision_score(target_test,clf.predict(feature_test))
print "recall score is:",recall_score(target_test,clf.predict(feature_test))


print "precision and recall test:"
test_pred =  [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
test_true =  [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "test confusion matrix"
print confusion_matrix(test_true,test_pred)
print "test precision score is:",precision_score(test_true,test_pred)
print "test recall score is:",recall_score(test_true,test_pred)



