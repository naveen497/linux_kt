# import csv
# ls = [1,2,3]
# target_file = 'eggs.csv'
# with open(target_file, 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',')
#     columnTitleRow = 'ACTUAL_DELIVERY_DATE', 'CUST_REQ_DELIVERY_DATE'
#     spamwriter.writerow(columnTitleRow)
#     te = str(ls[0]),str(ls[1])
#     spamwriter.writerow(te)
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

for i in range(10):
	target_file = 'egs'+str(i)
	print target_file