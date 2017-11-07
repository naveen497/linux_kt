
''' This is the helper function where you can find all the required functions for the project '''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ion,draw
import pandas as pd
import time, os

def norm(input_file,size,percentile,csc_code):
	"This function uses normalization technique to find the instant at which specified percentile is achieved"
	df = input_file
	bin_size = size
	saved_column = pd.DataFrame({'time':df})
	saved_column = saved_column['time']
	maxi=saved_column.max()
	mini=saved_column.min()
	if ( maxi == mini ):
		return mini
		
	mean = saved_column.mean()
	median = saved_column.median()
	mode = saved_column.mode()

	print "mode: "+ str( mode )
	mode_list = list(mode)
	print "mode in list "+ str( mode_list)
	print "minimum: "+ str( mini )
	print "maximum: "+ str( maxi )

	bin_size = size
	global_diff = (maxi - mini)
	global_count = len(saved_column)
	count = [0]*(int(round(global_diff/bin_size))+1)
	count_size = len(count)
	print "# of bins: " + str( count_size )

	temp=0
	for i in range(len(saved_column)): 
		# if ( len(saved_column) ==1 ): 
		# 	break
		diff = (saved_column[i] - mini)
		temp = int(round(diff/bin_size))
		if ( temp >= count_size ):
			print "above upper bound"
			return -1
		if ( temp <0 ):
			print "below lower bound "
			return -1
		count[temp]+=1		
	# print count
	max_bucket = max(count)

	index_bucket = count.index(max_bucket)

	print "maximum bucket: " + str(max_bucket)
	corr_time = index_bucket + mini
	print " corresponding time " + str( corr_time)
	bins = np.arange(mini, maxi, bin_size) # fixed bin size
	# print "bins: "+ str( bins )
	print "figure"
	plt.xlim([mini-5, maxi+5])

	plt.hist(saved_column, bins=bins, alpha=0.7)
	plt.title('SLA between Dispatch and Delivery of csc = %s'%csc_code)
	plt.xlabel('time ( min )--->(bin size = %d) \n Mean = %.2f,   Median = %.2f, Mode = %d'%(bin_size,mean,median,mode_list[0]))
	plt.ylabel('count')
	plt.show()



	temp=0
	result=[0,0]
	p_cent = percentile

	print "percentile : " + str(p_cent*global_count)
	print "1 - percentile : " + str((1-p_cent)*global_count)
	for t in range(len(count)):
		if ( temp >= int(p_cent*global_count )):
			result[0] = t
			break
		temp+=count[t]
	result[0] = mini + result[0]*bin_size 
	
	temp=0
	

	for t in range(len(count))[::-1]:
		if ( temp >= int((1-p_cent)*global_count )):
			result[1] = t
			break
		temp+=count[t]
	result[1] = mini + result[1]*bin_size 
	return result
