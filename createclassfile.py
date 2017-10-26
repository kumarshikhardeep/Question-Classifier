# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:36:31 2017

@author: Kumar Shikhar Deep
"""

#creating file for each class 
desc= open("DESC.txt","w")
enty= open("ENTY.txt","w")
abbr= open("ABBR.txt","w")
hum= open("HUM.txt","w")
num= open("NUM.txt","w")
loc= open("LOC.txt","w")
train=open("Questions_train.txt","r")
content=train.readlines()
for lines in content:
   # print (lines)
    x=lines.split(sep=":")
    if (x[0]=="DESC"):
        desc.write(x[1])
       # desc.write("\n")
    if (x[0]=="ENTY"):
        enty.write(x[1])
       # enty.write("\n")
    if (x[0]=="ABBR"):
        abbr.write(x[1])
       # abbr.write("\n")
    if (x[0]=="HUM"):
        hum.write(x[1])
       # hum.write("\n")
    if (x[0]=="NUM"):
        num.write(x[1])
       # num.write("\n")
    if (x[0]=="LOC"):
        loc.write(x[1])
        #loc.write("\n")
   
desc.close()
enty.close()
abbr.close()
hum.close()
num.close()
loc.close()
