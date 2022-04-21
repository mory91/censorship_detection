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
with open('Output.csv', newline='') as csvfile:
     X = []
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['id'])
         # try:
         #    print(socket.gethostbyaddr(row['src']))
         # except socket.herror:
         #     print("Not found")



         tmp = []
         with open('Output.csv', newline='') as csvfile2:
             reader2 = csv.DictReader(csvfile2)
             for row2 in reader2:
                 if (str(row2['src']) ==  "172.17.0.2" and row2['dst'] == row['src'] and int(row2['payload']) > 0):
                     ttl_d = int(row2['ttl']) - int(row['ttl'])
                     ipid_d = abs(int(row2['id']) - int(row['id']))
                     seq = abs(int(row2['seq']) - int(row['seq']))
                     print(seq)
                     break
             # tmp.append(ttl_d)
             # tmp.append(ipid_d)
     X.append(tmp)
print(t)
t.to_csv('Output.csv')

