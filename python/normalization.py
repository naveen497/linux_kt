#########################################################
# Main file for finding the soft breach SLAs ###########

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
import scipy
import csv
from helper import norm


df = pd.read_csv('~/Downloads/export.csv')
sample_size = df.shape[0]
print "sample_size: "+ str(sample_size)
# df = pd.read_csv('sample.csv')
# print df['DIFF`'].mean()
plt.close('all')

# final_result = norm(df,1,0.99)
# print "99% : " + str( final_result ) 
# final_result = norm(df,1,0.98)
# print "98% : " + str( final_result ) 
# final_result = norm(df,1,0.97)
# print "97% : " + str( final_result ) 

# final_result = norm(df,1,0.96)
# print "96% : " + str( final_result ) 

# final_result = norm (df,1,0.95)
# print "95% : " + str(final_result)

# final_result = norm (df,1,0.95)
# print "94% : " + str(final_result)
# 
# final_result = norm (df,1,0.95)
# print "93% : " + str(final_result)
final_result = norm(df,1,0.90)
print "90% : " + str( final_result ) 
final_result = norm (df,1,0.85)
print "85% : " + str(final_result)

# saved_column = df.time           #you can also use df['column_name']
# maxi=saved_column.max()
# mini=saved_column.min()

# bin_size = 1
# global_diff = maxi - mini
# global_count = len(saved_column)
# count = [0]*(int(round(global_diff/bin_size)))
# count_size = len(count)
# print saved_column
# print "iteration"
# temp=0
# for i in range(len(saved_column)): 
# 	diff = saved_column[i] - mini
# 	temp = int(round(diff/bin_size))
# 	if ( temp >= count_size ):
# 		temp = count_size -1
# 	count[temp]+=1		
# print count



# temp=0
# result=0
# percentile =0.5


# for t in range(len(count)):

# 	if ( temp >= int(percentile*global_count )):
# 		result = t
# 		break
# 	temp+=count[t]

# result= result*bin_size +mini
# print result


