
''' This is the helper function where you can find all the required functions for the project '''
import numpy as np
from matplotlib import pyplot as plt


def norm(input_file,size,percentile):
	"This function uses normalization technique to find the instant at which specified percentile is achieved"
	df = input_file
	saved_column = df.DIFF           #you can also use df['column_name']
	maxi=saved_column.max()
	mini=saved_column.min()
	mean = saved_column.mean()
	median = saved_column.median()
	mode = saved_column.mode()[0]
	# print "mean: "+ str( mean )
	# print "median: "+ str( type(median) )
	# print "mode: "+ str( mode )
	# print "mode: "+ str( type(mode) )
	# print "mode[1]: "+ str( mode[0])
	# print "mini: "+ str( mini)
	# print "maxi: "+ str( maxi )

	bin_size=size
	global_diff = maxi - mini
	global_count = len(saved_column)
	count = [0]*(int(round(global_diff/bin_size)))
	count_size = len(count)
	# print saved_column
	# print "iteration"
	temp=0
	for i in range(len(saved_column)): 
		diff = saved_column[i] - mini
		# print "diff: " + str(diff)
		# print "diff/bin_size: "+ str( diff/bin_size)
		temp = int(round(diff/bin_size))
		# print "temp: "+ str( temp )
		if ( temp >= count_size ):
			temp = count_size -1
		count[temp]+=1		
	# print count
	max_bucket = max(count)

	index_bucket = count.index(max_bucket)

	print "maximum bucket: " + str(max_bucket)
	print "corresponding time: "+ str( index_bucket + mini)

	bins = np.arange(mini, maxi, bin_size) # fixed bin size
	# print "bins: "+ str( bins )


	plt.xlim([mini-5, maxi+5])

	plt.hist(saved_column, bins=bins, alpha=1)
	plt.title('Time profile between between Creation to Release ( 3 months data ) ')
	plt.xlabel('time ( min )---> ( bin = %d min )\n Mean = %.2f,   Median = %.2f, Mode = %d '%(bin_size,mean,median,mode))
	plt.ylabel('count (number of orders per bin)')

	plt.show()
	temp=0
	result=0
	p_cent = percentile

	print "percentile : " + str(p_cent*global_count)
	for t in range(len(count)):
		if ( temp >= int(p_cent*global_count )):
			result = t
			break
		temp+=count[t]
	result = mini + result*bin_size 
	return result


