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
with open('Trace1.csv', newline='') as csvfile:
     X = []
     reader = csv.DictReader(csvfile)
     for row in reader:
         if(str(row['flags']).find("R")!=-1 and row['src'] != "172.17.0.2"):
                 counter += 1
                 print(counter)
                 with open('Trace1.csv', newline='') as csvfile2:
                     tmp =[]
                     reader2 = csv.DictReader(csvfile2)
                     for row2 in reader2:
                        if ((str(row2['src']) ==  "172.17.0.2" and row2['dst'] == row['src'] ) ):
                            ttl_d = abs(int(row2['ttl']) - int(row['ttl']))
                            ipid_d = abs(int(row2['id']) - int(row['id']))
                            tmp.append(ttl_d)
                            tmp.append(ipid_d)
                            break
                     if (len(tmp)!=0):
                        X.append(tmp)



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


print(len(X))

from sklearn.cluster import KMeans

# Initialize the class object

kmeans = KMeans(n_clusters= 2).fit(X)

# predict the labels of clusters.
label = kmeans.fit_predict(X)
print(label)
import matplotlib.pyplot as plt
c = 0
s =0
colors = ['r','g']
for i in label:
    if (i==0):
        s +=1
    plt.scatter(X[c][0],X[c][1] ,color = colors[i])

    c+=1
print(s)
plt.show()

