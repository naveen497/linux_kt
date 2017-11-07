#####################################################################
# gap calculation based on actual hourly sales, htb, eds, shelf stock #
# SC = shelf capacity
# SS = current shelf stock 
# acs = actual hourly sales
# tpnb = product id
# htr = hourly ptp percentages
# eds = expected daily sales 
# hourly_sales = expected hourly sales 
# PSG = probable shelf gap
######################################################################

import MySQLdb
system = "localhost"
user = "root"
password = "narcodes"
db_used = "consolidated"
db = MySQLdb.connect(system,user,password,db_used)
cursor = db.cursor()
from helper_function import *
date ='28/7/2017'
week ='22'		# the week considered for this program
day ='5'		# the day considered for this program
store = '2156'  # the store considered for this program
sub_group = 'F11AC'	# the sub-group under consideration


# fetching the tpnb_list and the associated shelf capacities of a sub-group F11AC from store 2156 from the table "shelf capacity"
col1 = "BPR_TPN"
col3 = "RO_BPR_SCAP"
col2 = "SG_CD"
table = "shelf_capacity"
SC_result = fetch_sc(col1,col3,table)
SC_list=[]
tpnb_list =[]
SG_list = []
for i in range(len(SC_result)):
	temp1 = SC_result[i][0]
	temp = SC_result[i][1]
	SC_list.append(temp)
	tpnb_list.append(temp1)

# iterating through the tpnb_list and calculating the hour in which gap would be created

for i in range(len(tpnb_list)):
	tpnb = int ( tpnb_list[i] )
	SC = int ( SC_list[i] )
	SS = SC
	table = "htb" 
	hr_1 = fetch_htb(table,day,week) 	# fetching the hourly ptp's from the "htb" table 
	htr = hr_1[6:len(hr_1)]
	htr = [int(i) for i in htr]
	col1 = "EXP_DAILY_SALES_5"
	table = "eds"
	eds_1 = fetch_eds(col1,table,tpnb)	# fetching the expected daily sales of that day from the "eds" table
	eds = float(eds_1[0])    
	hourly_sales= []
	
	for i in range(len(htr)):
		if( eds is not None):
			hourly_sales.append(i*eds*0.01)   # getting hourly sales by mulitplying htb with eds
	col1 = "sales_chunk_start"
	col2 = "sales_singles"
	table = "actual_hourly_sales_1"
	row_act = fetch_acs(col1,col2,table,tpnb)  # fetching the actual hourly sales of the previous hours

	start_time = []
	for i in range(len(row_act)):
		temp = row_act[i][0].split('.')
		start_time.append(int(temp[0]))
	acs = [0]*len(htr)
	for i in range(len(row_act)):
		temp = row_act[i][1]
		acs[start_time[i]]= float(temp)

	PSG = [0]*(len(hourly_sales))
	for i in range(len(hourly_sales)):
		SS = SS - hourly_sales[i] 							 	# deducting the expected hourly sales from the current shelf stock
		if((i-1)>=0): SS = SS + (hourly_sales[i-1] - acs[i-1])  # accounting for the actual sales of the previous hour 
		if SS<=0:
			PSG[i]=PSG[i]+1			# incrementing the value of the PSG slot if shelf stock is less than 0
			psg_full = [store,sub_group,day,tpnb,week]+PSG

			for i in psg_full:
				sql_psg = "INSERT INTO psg_2 (ro_no,sg_cd,day_no,tpnb,tesco_week,psg_1,\
					psg_2,psg_3,psg_4,psg_5,psg_6,psg_7,psg_8,psg_9,psg_10,psg_11,psg_12,\
					psg_13,psg_14,psg_15,psg_16,psg_17,psg_18,psg_19,psg_20,psg_21,psg_22,\
					psg_23,psg_24) VALUES("
				for i in range(len(psg_full)-1):
					if i==1:
						sql_psg+= "'"+str(psg_full[i])+"'"+","
					else:
						sql_psg+=str(psg_full[i])+","
				sql_psg+=str(psg_full[-1])
				sql_psg+=")" 
			push_psg(sql_psg) # pushing the probable shelf gap ( psg ) hour to the psg table 
			break

db.close()




