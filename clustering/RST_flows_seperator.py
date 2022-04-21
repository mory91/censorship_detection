import  pandas as pd
import csv
import math
import socket
df = pd.DataFrame()
import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
import socket
counter = 0
ipid0 = 0
ttl = 0
t = pd.DataFrame()
c =1
with open('ALL_RST_Trace2.csv', newline='') as csvfile:
     X = []
     reader = csv.DictReader(csvfile)
     for row in reader:
         if(str(row['flags']).find("R")!=-1 and row['src'] != "172.17.0.2"):
                 df = (pd.DataFrame(row, index=[c]))
                 t = pd.concat([t, df])
                 counter += 1
                 print(counter)
                 with open('ALL_RST_Trace2.csv', newline='') as csvfile2:
                     reader2 = csv.DictReader(csvfile2)
                     for row2 in reader2:
                        if ((str(row2['src']) ==  "172.17.0.2" and row2['dst'] == row['src']) or
                                (str(row2['src']) ==  row['src'] and row2['dst'] == "172.17.0.2" and str(row['flags']).find("R")==-1) ):

                             df = (pd.DataFrame(row2, index=[c]))
                             t = pd.concat([t, df])
                             c += 1



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
print(t)
t.to_csv('Output.csv')

