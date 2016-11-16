#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

#take out the total
data_dict.pop("TOTAL",0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

salary_bonus = []

for point in data:
    salary = point[0]
    bonus = point[1]
    if salary > 1000000:
        if bonus > 5000000:
            salary_bonus.append([salary,bonus])

print  salary_bonus


# find people who have the big salary and bonus
# all the data stored in data_dict,loop to look for the one  match
for key in data_dict:
    if data_dict[key]["salary"] == salary_bonus[0][0] and data_dict[key]["bonus"] == salary_bonus[0][1]:
        print "The name is:",key
    elif data_dict[key]["salary"] == salary_bonus[1][0] and data_dict[key]["bonus"] == salary_bonus[1][1]:
        print  "The name is:",key

## is turns out to be  LAY KENNETH L and SKILLING JEFFREY K




