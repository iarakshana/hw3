#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

def salaries_dict(vec):
    dict_sal = []
    for i in range(1,len(vec)):
        l = vec[i]
        #print('list', l)
        if 'POLICE OFFICER' in vec:
            dict_sal[salary] = l
        #print('dictsal',l)
    return dict_sal.count()

salaries_dict(vec)

solution = 12973 # Police workers as an int.
