#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

def salaries_dict(vec):#using similar definiton from q1 for highest salary person
    dict_sal = {}
    for i in range(1,len(vec)):
        l = vec[i]
        #print('list', l) to check and debug
        salary = l[7]   #sort by the hourly wage which is in list[7]
        #print(salary)  to check and debug
        #print('salary ', salary)  to check and debug
        dict_sal[salary] = l
        #print('dictsal',l)  to check and debug
    return max(sorted(dict_sal.items(),reverse=True))

salaries_dict(vec)

solution = 96.00 # Highest hourly as a float.
