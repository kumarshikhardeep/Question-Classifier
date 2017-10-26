# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:49:25 2017

@author: Kumar Shikhar Deep
"""

#Predicted Output
Questions_train_lines = sum(1 for line in open('Questions_train.txt'))
DESC_lines = sum(1 for line in open('DESC.txt'))
ABBR_lines = sum(1 for line in open('ABBR.txt'))
HUM_lines = sum(1 for line in open('HUM.txt'))
NUM_lines = sum(1 for line in open('NUM.txt'))
LOC_lines = sum(1 for line in open('LOC.txt'))
ENTY_lines = sum(1 for line in open('ENTY.txt'))


desc=open("DESC_FREQ.txt","r")
descline=desc.readlines()
enty=open("ENTY_FREQ.txt","r")
entyline=enty.readlines()
num=open("NUM_FREQ.txt","r")
numline=num.readlines()
hum=open("HUM_FREQ.txt","r")
humline=hum.readlines()
abbr=open("ABBR_FREQ.txt","r")
abbrline=abbr.readlines()
loc=open("LOC_FREQ.txt","r")
locline=loc.readlines()
test=open("Questions_test1.txt","r")
x=test.readlines()
pred=open("Predicted.txt","w")
pclass=open("ProbOfClass.txt","r")
pclassline=pclass.readlines()
for m in pclassline:
    w=m.split(",")
    if w[0]=="DESC":
        Prob_DESC=float(w[1])
    if w[0]=="ENTY":
        Prob_ENTY=float(w[1])
    if w[0]=="LOC":
        Prob_LOC=float(w[1])
    if w[0]=="NUM":
        Prob_NUM=float(w[1])
    if w[0]=="HUM":
        Prob_HUM=float(w[1])
    if w[0]=="ABBR":
        Prob_ABBR=float(w[1])
        

   

import math
for i in x:
    words=i.split()
    descgivendoc=0
    entygivendoc=0
    locgivendoc=0
    abbrgivendoc=0
    humgivendoc=0
    numgivendoc=0
    #for desc class
    for word in words:
        found=0
        for classline in descline:
            d=classline.split(",")
            if d[0]==word:
                descgivendoc=descgivendoc+float(d[2])
                found=1
        if found==0:
            descgivendoc=descgivendoc + (1/(DESC_lines+Questions_train_lines))
    descgivendoc=math.log(descgivendoc)
    allprob=[descgivendoc]
    
    #for enty class
    for word in words:
        found=0
        for classline in entyline:
            d=classline.split(",")
            if d[0]==word:
                entygivendoc=entygivendoc+float(d[2])
                found=1
        if found==0:
            entygivendoc=entygivendoc + (1/(ENTY_lines+Questions_train_lines))
    entygivendoc=math.log(entygivendoc)
    allprob.append(entygivendoc)
    
    #for abbr class
    for word in words:
        found=0
        for classline in abbrline:
            d=classline.split(",")
            if d[0]==word:
                abbrgivendoc=abbrgivendoc+float(d[2])
                found=1
        if found==0:
            abbrgivendoc=abbrgivendoc + (1/(ABBR_lines+Questions_train_lines))
    abbrgivendoc=math.log(abbrgivendoc)
    allprob.append(abbrgivendoc)
    
    #for loc class
    for word in words:
        found=0
        for classline in locline:
            d=classline.split(",")
            if d[0]==word:
                locgivendoc=locgivendoc+float(d[2])
                found=1
        if found==0:
            locgivendoc=locgivendoc + (1/(LOC_lines+Questions_train_lines))
    locgivendoc=math.log(locgivendoc)
    allprob.append(locgivendoc)
    
    #for hum class
    for word in words:
        found=0
        for classline in humline:
            d=classline.split(",")
            if d[0]==word:
                humgivendoc=humgivendoc+float(d[2])
                found=1
        if found==0:
            humgivendoc=humgivendoc + (1/(HUM_lines+Questions_train_lines))
    humgivendoc=math.log(humgivendoc)
    allprob.append(humgivendoc)
                
    #for num class
    for word in words:
        found=0
        for classline in numline:
            d=classline.split(",")
            if d[0]==word:
                numgivendoc=numgivendoc+float(d[2])
                found=1
        if found==0:
            numgivendoc=numgivendoc + (1/(NUM_lines+Questions_train_lines))
    numgivendoc=math.log(numgivendoc)
    allprob.append(numgivendoc)
    
    res=max(allprob)
    if(res==numgivendoc):
        pred.write("NUM\n")
    if(res==humgivendoc):
        pred.write("HUM\n")
    if(res==entygivendoc):
        pred.write("ENTY\n")
    if(res==abbrgivendoc):
        pred.write("ABBR\n")
    if(res==locgivendoc):
        pred.write("LOC\n")
    if(res==descgivendoc):
        pred.write("DESC\n")
        
desc.close()
enty.close()
abbr.close()
loc.close()
num.close()
hum.close()
test.close()
pred.close()
pclass.close()
