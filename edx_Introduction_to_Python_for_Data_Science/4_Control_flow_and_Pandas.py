# Pandas:
#
# - Huge amounts of data are common
# - 2D Numpy array?
#   - Only one type possible
# - Pandas
#   - High-level data manipulation
#   - Data Frame
#
# CSV file
#
# CSV file -> DataFrame
import pandas as pd

brics = pd.read_csv('brics.csv')

print(brics)

brics = pd.read_csv('brics.csv',index_col=0)

print(brics)
#
#
# Collumn access:
print(brics['country'])
print(brics.country)
#
#
# Add column

brics['on_earth'] = [True, True, True, True, True]

print(brics)
#
# Add column(2)

brics['density'] = brics['population'] / brics['area']*100000
print(brics)
#
#
# Row access:
print(brics.loc['BR'])

#
# Element access:
print(brics.loc['CH','capital'])
print(brics['capital'].loc['CH'])
print(brics.loc['CH']['capital'])
#
