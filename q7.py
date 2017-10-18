#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

def salaries_dict(vec):
    dict_sal = []
    for i in range(1,len(vec)):#checking i in the full range of list vec
        l = vec[i]
        #print('list', l)
        if 'POLICE OFFICER' and 'DETECTIVE' in vec:#adding both conditions in the vec list to count number
        #of detectives that are police officers
            dict_sal[salary] = l
        #print('dictsal',l)
    return dict_sal.count()

salaries_dict(vec)

solution = 845 # Detectives as int.
