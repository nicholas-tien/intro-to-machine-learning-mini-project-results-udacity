#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
# features_list = ['poi','salary'] # You will need to use more features

features_list = ['poi', 'salary','bonus','exercised_stock_options','total_stock_value','long_term_incentive','deferral_payments']

# features_list = ['poi','salary', 'long_term_incentive', 'total_payments', 'exercised_stock_options', 'deferral_payments','bonus', 'shared_receipt_with_poi', 'total_stock_value', 'restricted_stock',  'director_fees', 'other']


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


#take out total item

#get all the feature names
all_feature = []
for key in data_dict:
    for feature in data_dict[key]:
        all_feature.append(feature)
    break
# print "all the feature name:",all_feature
# ['salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock',
#  'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances',
#  'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive',
#  'email_address', 'from_poi_to_this_person']

data = featureFormat(data_dict, features_list)


### Task 2: Remove outliers
data_dict.pop("TOTAL",0)

# #find outlier
# import matplotlib.pyplot as plt
#
# for i in features:
#     plt.scatter( i[0], i[1] )
#
# plt.xlabel("salary")
# plt.ylabel("bonus")
# plt.show()


### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

my_dataset = data_dict


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()

#refer sklearn pipeline document
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectKBest
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA,NMF
from sklearn.grid_search import GridSearchCV

#--------------test method 1-----------

# anova_filter = SelectKBest(f_regression, k=1)
# kbest_clf = Pipeline([('anova', anova_filter), ('svc', svm.SVC(kernel='rbf'))])
# kbest_clf.fit(features_train,labels_train)
# print "test method 1:kbest_clf test score is:",kbest_clf.score(features_test,labels_test)

#-------------------------------------------

#------------test method 2-------------------
# -----SVM test----------
# C_OPTIONS = [1,2,4,8]
# N_FEATURES_OPTIONS = [2,3,4,5,6]
# param_grid =[{'reduce_dim':[PCA(n_components=3)],'reduce_dim__n_components':N_FEATURES_OPTIONS,'classify':[C_OPTIONS]}]
# pipe = Pipeline([('reduce_dim',PCA()),
#                  ('classify',svm.SVC()])
# -----------GaussianNB test----------
N_FEATURES_OPTIONS = [2,3,4,5,6]
param_grid =[{'reduce_dim':[PCA(n_components=3)],'reduce_dim__n_components':N_FEATURES_OPTIONS}]
pipe = Pipeline([('reduce_dim', PCA()),
                 ('classify',GaussianNB())])

clf = GridSearchCV(pipe, param_grid=param_grid, verbose=10)

# -----------DecisionTree test----------
# N_FEATURES_OPTIONS = [2,3,4,5,6]
# MIN_SPLIT = [1,2,3,4,5]
# param_grid =[{'reduce_dim':[PCA(n_components=3)],'reduce_dim__n_components':N_FEATURES_OPTIONS,
#             'classify':[DecisionTreeClassifier(random_state=0)],
#              'classify__min_samples_split':MIN_SPLIT}]
# pipe = Pipeline([('reduce_dim', PCA()),
#                  ('classify',DecisionTreeClassifier(random_state=0))])
#
# clf = GridSearchCV(pipe, param_grid=param_grid, verbose=10)

#-------------test method 3-------------------
# estimators = [('reduce_dim', PCA(n_components=4)), ('nb', GaussianNB())]
#
# clf = Pipeline(estimators)
#----------------------------------

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


# Example starting point. Try investigating other evaluation techniques!



# clf = svm.SVC()
# clf.set_params(anova__k=4, svc__C=.1).fit(features_train, labels_train)
clf.fit(features_train, labels_train)
print "processed test score:",clf.score(features_test,labels_test)

# svm_clf = svm.SVC()
# svm_clf.fit(features_train,labels_train)
# print "unprocessed test score is:",svm_clf.score(features_test,labels_test)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)