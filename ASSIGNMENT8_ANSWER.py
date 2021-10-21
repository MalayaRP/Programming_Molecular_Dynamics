#This Program will read the unique set of non-zero integrals and generate all the two electron integrals with both zero and non-zero values. 

from numpy import *
from math import *
dim=7
file_read=open('eri.dat','r+') # Place the data file in the working directory
contents = file_read.readlines()
twoe={}
for line in contents:
    line=line.rstrip()
    line=line.split()
    twoe[line[0]+line[1]+line[2]+line[3]]=line[4]
for i in range(1,dim+1):
    for j in range(1,dim+1):
        for k in range(1,dim+1):
            for l in range(1,dim+1):
                if str(i)+str(j)+str(k)+str(l) in twoe:
                    print(i,j,k,l,twoe[str(i)+str(j)+str(k)+str(l)])
                elif str(j)+str(i)+str(k)+str(l) in twoe:
                    print(i,j,k,l,twoe[str(j)+str(i)+str(k)+str(l)])
                elif str(i)+str(j)+str(l)+str(k) in twoe:
                    print(i,j,k,l,twoe[str(i)+str(j)+str(l)+str(k)])
                elif str(j)+str(i)+str(l)+str(k) in twoe:
                    print(i,j,k,l,twoe[str(j)+str(i)+str(l)+str(k)])
                elif str(k)+str(l)+str(i)+str(j) in twoe:
                    print(i,j,k,l,twoe[str(k)+str(l)+str(i)+str(j)])
                elif str(l)+str(k)+str(i)+str(j) in twoe:
                    print(i,j,k,l,twoe[str(l)+str(k)+str(i)+str(j)])
                elif str(k)+str(l)+str(j)+str(i) in twoe:
                    print(i,j,k,l,twoe[str(k)+str(l)+str(j)+str(i)])
                elif str(l)+str(k)+str(j)+str(i) in twoe:
                    print(i,j,k,l,twoe[str(l)+str(k)+str(j)+str(i)])
                else:
                    print(i,j,k,l,0.0)