#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")
#we sort the names in police officers only and then count the modal occurrences
def salaries_dict(vec):
    dict_sal = []
    for i in range(1,len(vec)):
        l = vec[i]
        #0 is the column for list that has the names
        if 'POLICE OFFICER' in vec and vec[0]: #checking if the words police officer is in the list and in the names column
            dict_sal[salary] = l
        #print('dictsal',l)
    return sorted(dict_sal.items(), reverse=True)#return a sorted list of names
    set(dict_sal.items)).count()#set can find the unique occurences and then use count for the modal names

salaries_dict(vec)
# Solution should contain the single
# police officer name with 37 occurrences.
solution = "JENNIFER"
