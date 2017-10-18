#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

def salaries_dict(vec):#using similar definiton from q1 for highest salary person
    dict_sal = {}
    for i in range(1,len(vec)):
        l = vec[i]
        salary = l[7]   #sort by the hourly wage which is in list[7]
        dict_sal[salary] = l
    return sum(sorted((salary[7])))/len(dict_sal)#to get the median salary we try to find the middle of the sorted salary list of the sum divided by length

salaries_dict(vec)

solution = 92274.00 # Median salary as a float (note, different from HW)
