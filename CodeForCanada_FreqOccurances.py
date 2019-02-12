# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 07:52:53 2019

This program is the first challenge in the CodeForCanada 2019 Fullstack Fellowship challenge

This program obtains the number of violations in each given category.

@author: sid ramesh
"""

## importing the pandas library
import pandas as pd

## importing the csv and creating a data frame
df1 = pd.read_csv("C:/Users/sidra/C4C-dev-challenge-2018.csv")

## setting the index to violation_id for quicker computation
df2 = df1.set_index("violation_id", drop = True)

## creating a subset dataframe with just the violation_categories
df3 = df2.loc[:,"violation_category"]

## printing the total occuranes in each category
print('The number of violations in each category is \n', df3.value_counts())
