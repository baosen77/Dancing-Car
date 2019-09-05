# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:16:49 2019

@author: dell
"""
import numpy as np

a=[(415.0, 372.5),(0.5, 6.0),(-1.0, -0.5),(-0.5, 4.5),(1.0, -1.0),(1.0, 7.5),(0.0, 5.5),(1.5, 1.5),(-0.5, 6.5),(2.5, 0.5),(1.5, 8.5),(6.5, 9.5),(3.0, 5.5),(3.5, 6.5),(3.5, 2.5),(3.0, 4.0),(2.0, 2.5),(5.5, 8.0),(6.0, 5.0),(4.0, 3.0),(7.5, 6.5),(2.5, 2.5),(9.0, 6.0),(0.0, 0.0),(12.5, 8.5),(4.5, 3.5),(-0.5, -1.0),(19.5, 13.0),(5.5, 3.0),(0.0, 0.0),(16.0, 8.5),(0.5, 0.5),(12.0, 5.5),(7.5, 4.0),(12.5, 5.0),(6.0, 2.5),(8.0, 3.5),(7.0, 3.0),(15.0, 5.0),(15.0, 5.5),(24.0, 6.5),(9.0, 3.0),(6.0, 3.0),(27.0, 5.0),(0.0, 0.5),(18.0, 4.5),(9.5, 1.5),(18.0, 3.5),(18.5, 4.0),(10.0, 2.0),(18.5, 2.5),(20.0, 3.5),(50.5, 8.5),(40.0, 7.5)]


angle2=[]
len(a)
i=1
f=open("D:deta_angle.txt","w+")

while i<len(a):
    x=np.array(a[i-1])
    y=np.array(a[i])
    Lx=np.sqrt(x.dot(x))
    Ly=np.sqrt(y.dot(y))
    #相当于勾股定理，求得斜线的长度
    cos_angle=x.dot(y)/(Lx*Ly)
    #求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
#    print(cos_angle)
    angle=np.arccos(cos_angle)
    angle2.append(angle*360/2/np.pi)
    #变为角度
    f.write(str(angle2[i-1]))
    f.write(",")
    i+=1

f.close()