import pandas as pd #I am importing pandas as pd
from pandas import Series, DataFrame # Series and Data Frame are two data structures available in python
import numpy as np
mjp= Series([5,4,3,2,1])# a simple series
''' print mjp        # A series is represented by index on the left and values on the right
print mjp.values # similar to dictionary. ".values" command returns values in a series 
print " index "
print str( mjp.index) # returns the index values of the series
jeeva = Series([5,4,3,2,1,-7,-29], index =['a','b','c','d','e','f','h']) # The index is specified
 print jeeva # try jeeva.index and jeeva.values
print jeeva['a'] # selecting a particular value from a Series, by using index
jeeva['d'] = 9 # change the value of a particular element in series
print jeeva
print jeeva[['a','b','c']] # select a group of values
print jeeva[jeeva>0] # returns only the positive values
print jeeva *2 # multiplies 2 to each element of a series
print np.mean(jeeva) # you can apply numpy functions to a Series '''
 

states ={'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
                  'Population': [36, 44, 67,89,34],
                  'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states) # creating a data frame
print india
