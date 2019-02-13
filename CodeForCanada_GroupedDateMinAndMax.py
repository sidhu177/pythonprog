# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 07:57:02 2019


This program is the second challenge in the CodeForCanada 2019 Fullstack Fellowship challenge

This program obtains the earliest date and the latest date of violations in each given category.

@author: sid ramesh
"""
## importing the libraries
import pandas as pd
from datetime import date

## importing the csv
df1 = pd.read_csv("C:/Users/sidra/C4C-dev-challenge-2018.csv")

## creating the dataframe with violation_id as the index
df2 = df1.set_index("violation_id", drop = True)

## creating subsets of the master data with the violation category column
df3 = df2.loc[:,"violation_category"]

## creating subset of the violation date 
df4 = df2.loc[:,"violation_date"]

## as the values are a combination of date and time, separating only the date values 
df4 = pd.to_datetime(df4)

## finding the earliest date
earliest_date = df4.min()

## making sure only the date value is stored 
earliest_date = earliest_date.date()

## creating the subset for violation_date_closed
df5 = df2.loc[:,"violation_date_closed"]

## checking to see if there are any null values
df5.isna()

## filling the null values with the earliest date to avoid complexity
df5 = df5.fillna(earliest_date)

## separating the date values from datetime
df5 = pd.to_datetime(df5)

## creating a dataframe with just the violation category, violation date and violation date closed
df6 = pd.concat([df3, df4, df5], axis=1, keys=['violation_category', 'violation_date', 'violation_date_closed'])

##  grouping the dataframe with respect to violation categories and finding the earliest and latest dates
gbmax = df6.groupby('violation_category').agg({'violation_date': ('min'), 'violation_date_closed': ('max')})

## printing the earliest and the latest dates for each violation category
print('Here are the earliest and latest date of occurence for each category \n', gbmax)






