#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    filter_data = []
    data_len = len(predictions)


    diff_worth = []
    diff_worth = abs(predictions - net_worths)
    # for predict_worth,real_worthin in zip(predictions,net_worths):
    #       diff_worth.append(predict_worth - real_worth)

    worth_index = range(data_len)
    diff_worth_with_index = []
    for i,diff_value in zip(worth_index,diff_worth):
        diff_worth_with_index.append([i,diff_value])

    # sort with index
    for i in xrange(data_len):
        for j in xrange(i + 1, data_len):
            if diff_worth_with_index[i][1] < diff_worth_with_index[j][1]:
                tmp = diff_worth_with_index[i][1]
                tmp_index = diff_worth_with_index[i][0]
                diff_worth_with_index[i][1] = diff_worth_with_index[j][1]
                diff_worth_with_index[i][0] = diff_worth_with_index[j][0]
                diff_worth_with_index[j][1] = tmp
                diff_worth_with_index[j][0] = tmp_index

    #
    # for i in xrange(data_len):
    #     worth_index[i] = i
    #     for j in xrange(i+1,data_len):
    #         if diff_worth[i] < diff_worth[j]:
    #             tmp = diff_worth[i]
    #             diff_worth[i] = diff_worth[j]
    #             diff_worth[j] = tmp
    #             worth_index[i] = j


    # for age, real_worth in in zip(ages, net_worths):

    int_start = int(data_len*0.1)
    for i in range(int_start,data_len):
        cleaned_data.append((ages[diff_worth_with_index[i][0]], net_worths[diff_worth_with_index[i][0]], diff_worth[diff_worth_with_index[i][0]]))
        # cleaned_data.append((ages[worth_index[i]],net_worths[worth_index[i]],diff_worth[[i]]))


    
    return cleaned_data

