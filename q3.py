#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

#replicating full time for part time workers
import csv

data = open('salaries.csv', 'r')
saldata = csv.reader(data,delimiter=',')#using csv reader to easily separate the csv file
sal = []
for row in saldata:
    sal.append(row)

salNoFirstColumn = [sal[i][1:] for i in range(len(cats))]#ignoring the first header column

salFloat = [map(float, salNoFirstColumn[i]) for i in range(len(salNoFirstColumn))]
#trying to fix the float numbers in the list of lists
for i in range(salFloat):
    if 'P' in sal:#if the worker is part time they will have P in their list so code is asking to print
        print(sal)

len(sal)#finding the length of those in our list of only part time workers

solution = 1982 # Part-time as an int.
