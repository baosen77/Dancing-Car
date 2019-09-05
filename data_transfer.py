# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:18:58 2019

@author: Chenzy
"""
import re
import numpy as np



#data=re.split('b|,|2',data)

#print(data)


with open('a4.txt', 'r') as fpr: 
    content = fpr.read() 
content = content.replace('(','') 
content = content.replace(')','')
content = content.replace(',',' ')
with open('a4_r.txt', 'w') as fpw: 
    fpw.write(content)    
data=np.loadtxt('a4_r.txt')
print(len(data))



with open('t4.txt', 'r') as fpr: 
    content = fpr.read() 
content = content.replace('(','') 
content = content.replace(')','')
content = content.replace(',',' ')
with open('t4_r.txt', 'w') as fpw: 

    fpw.write(content)
    
data=np.loadtxt('t4_r.txt')
print(len(data))



with open('detaright4.txt', 'r') as fpr: 
    content = fpr.read() 
content = content.replace('(','') 
content = content.replace(')','')
content = content.replace(',',' ')
with open('detaright4_r.txt', 'w') as fpw: 
    fpw.write(content)   
data=np.loadtxt('detaright4_r.txt')

print(len(data))





with open('locationright4.txt', 'r') as fpr: 
    content = fpr.read() 
content = content.replace('(','') 
content = content.replace(')','')
content = content.replace(',',' ')
with open('locationright4_r.txt', 'w') as fpw: 
    fpw.write(content)   
data=np.loadtxt('locationright4_r.txt')
print(len(data))