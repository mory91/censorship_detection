import  pandas as pd
import csv
import math
import socket
df = pd.DataFrame()
import socket
counter = 0
ipid0 = 0
ttl = 0
with open('Output.csv', newline='') as csvfile:
     X = []
     reader = csv.DictReader(csvfile)
     for row in reader:
         if(str(row['flags']).find("R")!=-1 and row['src'] != "172.17.0.2"):
                 counter +=1
                 # print(counter)
                 # print(row['ttl'])
                 if (int (row['id']) != 0):
                    print(row['ttl'])
                    # print(row['len'])
                 # print(row['id'])
                 # with open('Output.csv', newline='') as csvfile2:
                 #     reader2 = csv.DictReader(csvfile2)
                 #     tmp = []
                 #     for row2 in reader2:
                 #         if (str(row2['src']) ==  "172.17.0.2" and row2['dst'] == row['src']):
                 #             ttl_d = int(row2['ttl']) - int(row['ttl'])
                 #             ipid_d = abs(int(row2['id']) - int(row['id']))
                 #             print(ttl_d)
                 #             break
                 #     tmp.append(ttl_d)
                 #     tmp.append(ipid_d)
                 # X.append(tmp)


print(X)



