#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#-------------------------------------------------------------
# find how many people
people_num = len(enron_data)
print "people number is",people_num

#-------------------------------------------------------------
#find how many features of a person
features_num = len(enron_data["SKILLING JEFFREY K"])
print "feature number is",features_num

#-------------------------------------------------------------
#find POIs number   ( dict loop)  data[person_name]["poi"] == 1
poi_num = 0
for key in enron_data:
    if enron_data[key]["poi"] ==1:
        poi_num +=1

print "POI number is",poi_num

#-------------------------------------------------------------
# how man POI in   ../final_project/poi_names.txt
# a executable solution ,but not best efficient
poi_num2 = 0
poi_names = open("../final_project/poi_names.txt")
line = poi_names.readline()
if "(y)"in line:
    poi_num2 += 1
while line:
    line = poi_names.readline()
    if "(y)" in line:
        poi_num2 +=1
    if "(n)" in line:
        poi_num2 += 1

print "poi number in txt is:",poi_num2

#-------------------------------------------------------------
# total stock belonging to James Prentice
keys = enron_data["PRENTICE JAMES"].keys()
print "all features:",keys
print "Total stock belonging to James Prentice is:",enron_data["PRENTICE JAMES"]["total_stock_value"]

#-------------------------------------------------------------
# emails from Wesley Colwell to poi
print "Emails from Wesley Colwell to poi:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#-------------------------------------------------------------
# find  value of stock options exercised by Jeffrey Skilling       Jeffrey Skilling  exercised_stock_options
#jeffrey_exercised_stock_options  = enron_data["SKILLING JEFFREY"]["exercised_stock_options"]
#Jeffrey_name ="Skilling Jeffrey"
Jeffrey_name ="Skilling Jeffrey"
#if Jeffrey_name.upper() in enron_data:
Jeff_stock_options = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "answer is",Jeff_stock_options


#-------------------------------------------------------------
#find the largest total_payments of Lay,Skilling and Fastow
Lay_payment = enron_data["LAY KENNETH L"]["total_payments"]
skilling_payment =  enron_data["SKILLING JEFFREY K"]["total_payments"]
fastow_payment = enron_data["FASTOW ANDREW S"]["total_payments"]
payments = [Lay_payment,skilling_payment,fastow_payment]
largest_payment_index =payments.index(max(payments))
if largest_payment_index == 0:
    print "The largest payments is:","lay","    ","The value is:",Lay_payment
elif largest_payment_index ==1:
    print "The largest payments is:","skilling","    ","The value is:",killing_payment
else:
    print "The largest payments is:","fastow", "   ","The value is:",fastow_payment

#unfilled feature


#----------------quantified salary and known email address------------------
#print enron_data["FOWLER PEGGY"]["salary"]
salary_num = 0
email_num = 0
total_num = 0
def isNaN(x):
    try:
        import math
        return math.isnan(float(x))
    except:
        return False

# print  enron_data["FOWLER PEGGY"]["salary"]
# print  isNaN(enron_data["FOWLER PEGGY"]["salary"])
# print  enron_data["BAXTER JOHN C"]["salary"]
# print  isNaN(enron_data["BAXTER JOHN C"]["salary"])

for key in enron_data:
    total_num = total_num + 1
    if not isNaN(enron_data[key]["salary"]):
        salary_num += 1
    if not isNaN(enron_data[key]["email_address"]):
        email_num += 1

print "The total people number is ",total_num
print "Quantified salary number is:",salary_num,"      ","Email address number is:",email_num

#------------------------------------------------------------------------------------------------
# how many NaN are set for e+f dataset,what percentage is it

nan_num = 0
total_num = 0
for key in enron_data:
    total_num += 1
    if isNaN(enron_data[key]["total_payments"]):
        nan_num +=1
nan_percentage = nan_num/float(total_num)
print "The total payments NaN number is:",nan_num,"     ","Its percentage is:",nan_percentage*100

#------------------------------------------------------------------------------------------------
# how many poi people's total payments is nan
poi_nan_payments = 0
total_num = 0
poi_num_tmp = 0
for key in enron_data:
    total_num += 1
    if enron_data[key]["poi"] == 1:
        poi_num_tmp += 1
        if isNaN(enron_data[key]["total_payments"]):
            poi_nan_payments +=1
poi_nan_payments_percentage = poi_nan_payments/float(total_num)
print "The poi payments NaN number is:",poi_nan_payments,"     ","Its percentage is:",poi_nan_payments_percentage*100

#------------------------------------------------------------------










