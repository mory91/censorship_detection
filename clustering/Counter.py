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
         if ( (int(row['ack']) == 0 and int(row['len']) == 40) and int(row['id']) != 0 and row['src'] != "172.17.0.2" ):
             counter += 1
             print(counter)
         # if(str(row['flags']).find("R")!=-1 and row['src'] != "172.17.0.2" and int(row['id'])!=0 and (not(int(row['ack'])== 1 and int(row['len']) ==0))):



