"""
Write a Pandas program to display the dimensions or shape of the World alcohol consumption dataset.
Also extract the column names from the dataset.
Test Data:
  Year       WHO region                Country Beverage Types  Display Value
0  1986  Western Pacific               Viet Nam           Wine           0.00
1  1986         Americas                Uruguay          Other           0.50
2  1985           Africa           Cte d'Ivoire           Wine           1.62
3  1986         Americas               Colombia           Beer           4.27
4  1987         Americas  Saint Kitts and Nevis           Beer           1.98

Solution:
"""


import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print('\nShape of the dataframe: ',w_a_con.shape)
print('\nNumber of rows: ',w_a_con.shape[0])
print('\nNumber of column: ',w_a_con.shape[1])
print("\nExtract Column Names:")
print(w_a_con.columns)
