#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

#trying to find the number of employees in the city with the len function run on salary
#as we want the number of employees only not the header and other unnecessary lines
li = [i for i in range(1,len(vec)) if vec[6]]
print(len(li))

solution = 32658 # Total employees as int.
