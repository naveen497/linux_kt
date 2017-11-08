#########################################################
# Main file for finding the soft breach SLAs ###########

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
import scipy
import csv
from helper_2 import norm
import time, os
# from email.utils import parsedate_tz, formatdate


# time_fac = 60
bin_size = 1
perc_list = [0.99,0.98,0.97,0.96,0.95,0.90,0.85]

# perc_list = [0.99]
df = pd.read_csv('~/Downloads/DeliveryData_2.csv')
sample_size = df.shape[0]
# print "sample_size: "+ str( sample_size)
group_csc = df.groupby('CARRIER_SERVICE_CODE')
groups = group_csc.groups.keys()
print groups
groups_list = list(groups)
count_group = []
for i in range(len(groups)):
	temp_group = group_csc.get_group(groups[i])
	temp_order_cnt = temp_group.shape[0]
	count_group.append(temp_order_cnt)
print "count: "+str(count_group)
count_group = sorted(count_group)

target_group_index =[]
target_group_index.append(groups_list.index('Store_Collect-UKMainland')) 
# target_group_index.append(groups_list.index('Store_Collect-UKOOA'))
# target_group_index.append(groups_list.index('Standard2C-UKMainland'))


# print "target_group: "+ str(target_group_index)
# test = group_csc.get_group(groups[4])
# print test
# t=4
# print groups
order_cnt_group =[]
for t in range(len(groups)):
	if ( t not in target_group_index ):
		continue
	print " ========================================================="
	print "       "+" CSC: "+ str(groups[t])
	print " ========================================================="
	# print "group: "+ str(groups[t])x
	group_t = group_csc.get_group(groups[t])
	# print group1
	order_cnt_group.append(group_t.shape[0])
	# print "number of orders: "+ str(group_t.shape[0])
	# gr_act = group_t['ACTUAL_SHIPMENT_DATE']
	# gr_stmp = group_t['CUST_REQ_SHIP_DATE']
	gr_act = group_t['ACTUAL_DELIVERY_DATE']
	gr_stmp = group_t['CUST_REQ_DELIVERY_DATE']
	# print list(gr_act)
	# struct_time = time.strptime("30 Nov 00", "%d %b %y")
	# print "returned tuple: %s " % struct_time
	li_act = list(gr_act)
	li_stmp = list(gr_stmp)
	li_act_ep = []
	li_stmp_ep = []
	# li = str(li)
	# d= li
	p='%d/%m/%y %H:%M'
	print "string of li_act: "+ str( str(li_act[0]))

	# epoch = int(time.mktime(time.strptime(d,p)))
	# print epoch
	for i in range(len(li_act)):
		d = str(li_act[i])
		epoch = int(time.mktime(time.strptime(d,p)))
		li_act_ep.append(epoch)

	for i in range(len(li_stmp)):
		d = str(li_stmp[i])
		epoch = int(time.mktime(time.strptime(d,p)))
		li_stmp_ep.append(epoch)
		# print "epoch of stamped : "+ str(epoch)
	diff_disp = []
	for i in range(len(li_act_ep)):
		diff_temp = li_stmp_ep[i] - li_act_ep[i] 
		diff_disp.append(-diff_temp/60)
	# print "diff_disp: " + str(diff_disp)


	# print li_act_ep
	# print li_stmp_ep
	for perc in range(len(perc_list)):
		# print " ------------------ " + str(perc_list[perc]*100) +" % ---------------------"
		# print " ------ actual shipment details --------- "
		# result_act  = norm(li_act_ep,bin_size,perc_list[perc])
		# result_act  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result_act))
		# print " ------ stamped shipment details --------- "
		# result_stmp = norm(li_stmp_ep,bin_size,perc)
		# result_stmp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result_stmp))
		# print "actual shipment date | stamped shipment date"
		# print result_act + "     "+ result_stmp
		# print "99% of actual shipment date : " + str( final_result_act ) 
		# print "99% of stamped shipment date : " + str( final_result_stmp)
		# print " "time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(final_result))
		result_act  = norm(diff_disp,bin_size,perc_list[perc],groups[t])
		print str(perc_list[perc])+"% : " + str( -result_act ) 
		# result_act  = time.strftime('%Y-%m-%d %H:%M:%S'
# print "order count group wise: " + str(order_cnt_group)

# print parsedate_tz(formatdate(epoch))
# repg = time.strftime('%Y%m%d%H%M%S',parsedate_tz(formatdate(epoch)))
# print 
# print gr.mean()

# print "gr: "+ str(gr)
# print list(gr)
# print "group mean "+ str(gr_mean)
# print group1.shape







# df = pd.read_csv('sample.csv')
# final_result = norm(,1,0.99)
# print "99% : " + str( final_result ) 
# final_result = norm (df,1,0.95)
# print "95% : " + str(final_result)
# final_result = norm(df,1,0.90)
# print "90% : " + str( final_result ) 
# final_result = norm (df,1,0.85)
# print "85% : " + str(final_result)

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


