#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")
#defined a function that can sort within the list of the list on specifically the salaries column by making that column specifically
#a list
def salaries_dict(vec):
        dict_sal = {}
        for i in range(1,len(vec)):
        l = vec[i]
        salary = l[6]
        #print(salary)
        #print('salary ', salary)
        dict_sal[salary] = l
        #print('dictsal',l)
        #sorting the dict_sal from reverse gives us the largest to smallest
    return sorted(dict_sal.items(), reverse=True)

salaries_dict(vec)

sorted(vec, key=lambda x: (x[6]), reverse=True) #also can use list comprehension with labda to sort

solution = "EVANS" # LAST NAME IN CAPS.
