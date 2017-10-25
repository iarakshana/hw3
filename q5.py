#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

def salaries_dict(vec):#using similar definiton from q1 for highest salary person
    dict_sal = {}
    for i in range(1,len(vec)):
        sorted(vec[-4]) #removing the top four highest hourly wages of the doctors and finding the highest wage
        l = vec[i]
        salary = l[7]   #sort by the hourly wage which is in list[7]
        dict_sal[salary] = l
    return max(sorted(dict_sal.items(),reverse=True))

print(salaries_dict(vec))

solution = 53.90 # Non-medical highest.

'''Grader Comments:
Your solution is incorrect. Also, please return one value
'''