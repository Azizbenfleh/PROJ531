# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:43:56 2023

@author: benflahm
"""

f=open('textesimple_freq.txt','w')
file=open('textesimple.txt','r')
lines = f.read().splitlines()
for i in lines[0]:
    n=0
    if i=='':
        n+=1
x=len(lines[0])-n
f.write(x)
d={}
for j in lines[0]:
    if j=='': 
       continue
    else:
            t=j
            w=0
            for p in lines[0]:
                if p==t and not(t in d.values()):
                    w+=1
            
            f.write(tw/n)

        

                