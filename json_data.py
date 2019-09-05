# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:21:44 2019

@author: dell
"""

import os.path
import time
import json

filenum1=[]
filenum2=[]
milliseconds=[]#毫秒
image_array=[]#对应图像
angle=[]#角度
throttle=[]#动力
time_interval=[]#时间间隔
time_interval.append(0)

num=8881
nummax=10939
while num<=nummax:
    timepoint=time.ctime(os.path.getmtime("D:json/tub_2L_19-09-04/tub_2_19-09-04/record_"+str(num)+".json"))
    if(timepoint=="Wed Sep  4 21:53:41 2019"):
        filenum1.append(num)
    if(timepoint=="Wed Sep  4 21:55:07 2019"):
        filenum2.append(num)
        num=nummax
    num+=1


nummin=min(filenum1)
nummax=min(filenum2)
print("nummax",nummax)
num=nummin

while num<=nummax:
    with open("D:json/tub_2L_19-09-04/tub_2_19-09-04/record_"+str(num)+".json", 'r') as f:
        temp = json.loads(f.read())
        milliseconds.append(temp["milliseconds"])
#        image_array.append(temp["cam/image_array"])
        angle.append(temp["user/angle"])
        throttle.append(temp["user/throttle"])
    num+=1     
    
num_1=1
while num_1<=nummax-nummin:
    time_interval.append(milliseconds[num_1]-milliseconds[0])
    num_1+=1



filename11=input("angle路径：")
filename1="D:Lcircle_angle.txt"
filename2="D:Lcircle_throttle.txt"
filename22=input("throttle路径：")
filename3="D:time.txt"
f1=open(filename1,"a+")
f11=open(filename11,"a+")
f22=open(filename22,"a+")
f2=open(filename2,"a+")
f3=open(filename3,"w+")

i=0
while i<len(angle):
    f1.write(str(angle[i]))
    f1.write(",")
    f2.write(str(throttle[i]))
    f2.write(",")
    f11.write(str(angle[i]))
    f11.write(",")
    f22.write(str(throttle[i]))
    f22.write(",")
    f3.write(str(time_interval[i]))
    f3.write(",")
    i+=1
    
f1.close()
f2.close()
f3.close()
f11.close()
f22.close()
#print("milliseconds:",milliseconds)
#print("image_array:",image_array)  
#print("angle:",angle,'\n','\n',)
#print("throttle:",throttle,'\n','\n')
#print("time_point:",time_interval)
print(len(angle))
