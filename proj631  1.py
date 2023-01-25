# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:41:27 2023

@author: benflahm
"""
file=open('textesimple.txt','r')
def nbr_carc(f):
   lines = file.read().splitlines()
   for i in lines[0]:
       n=0
       if i=='':
           n+=1
   x=len(lines[0])-n
   return(x)


def calcul_freq(f):
    lines = file.read().splitlines() 
   
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
                    d{w}=t
    return(d)


class node:
    def __init__(self,fils_g,fils_d,label,root):
        self.fils_g=fils_g
        self.fils_d=fils_d
        self.label=label
    def creation_fils(self):
        
                    
class tree:
   def __init__(self,root:
      self.root=root

   def creation_arbre(self):
       self.root=
       
                     
    
    