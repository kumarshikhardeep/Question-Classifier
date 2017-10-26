# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:38:45 2017

@author: Kumar Shikhar Deep
"""

#cleaning the training set(removing punctuations)
train=open("Questions_train.txt","r")
train1=open("Questions_train1.txt","w")
content=train.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    print(line)
    train1.write(line)
    train1.write("\n")
train1.close()
train.close()

#vocabulary of distinct words without cleaning
vocabulary=open("vocabulary.txt","w")
train1=open("Questions_train1.txt","r")
line=train1.read()
x=line.split()
unique=set(x)
unique=sorted(unique)
print(len(unique))
for i in unique:
    vocabulary.write(i)
    vocabulary.write("\n")
vocabulary.close()
    

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


#cleaning each class file
enty= open("ENTY.txt","r")
enty1=open("ENTY1.txt","w")
content=enty.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    enty1.write(line)
    enty1.write("\n")
enty1.close()
enty.close()

hum= open("HUM.txt","r")
hum1=open("HUM1.txt","w")
content=hum.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    hum1.write(line)
    hum1.write("\n")
hum1.close()
hum.close()

num= open("NUM.txt","r")
num1=open("NUM1.txt","w")
content=num.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    num1.write(line)
    num1.write("\n")
num1.close()
num.close()

abbr= open("ABBR.txt","r")
abbr1=open("ABBR1.txt","w")
content=abbr.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    abbr1.write(line)
    abbr1.write("\n")
abbr1.close()
abbr.close()

loc= open("LOC.txt","r")
loc1=open("LOC1.txt","w")
content=loc.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    loc1.write(line)
    loc1.write("\n")
loc1.close()
loc.close()

desc= open("DESC.txt","r")
desc1=open("DESC1.txt","w")
content=desc.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    desc1.write(line)
    desc1.write("\n")
desc1.close()
desc.close()


#count of each word and its probability in each class file

Questions_train_lines = sum(1 for line in open('Questions_train.txt'))
DESC_lines = sum(1 for line in open('DESC.txt'))
ABBR_lines = sum(1 for line in open('ABBR.txt'))
HUM_lines = sum(1 for line in open('HUM.txt'))
NUM_lines = sum(1 for line in open('NUM.txt'))
LOC_lines = sum(1 for line in open('LOC.txt'))
ENTY_lines = sum(1 for line in open('ENTY.txt'))

vocabulary=open("vocabulary.txt","r")
desc=open("DESC1.txt","r")
desc_freq=open("DESC_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofdesc=desc.readlines()
for word in contentofvocab:    
    word=word.replace("\n","")
    count=0
    for line in contentofdesc:
        x=line.split()
        for i in x:
           # print(i)
            if word == i:                 
                count=count+1
    prob=(count+1)/(DESC_lines+Questions_train_lines)
    desc_freq.write(word+",%d"%count+",%f"%prob)
    desc_freq.write("\n")
vocabulary.close()
desc.close()
desc_freq.close()

vocabulary=open("vocabulary.txt","r")
enty=open("ENTY1.txt","r")
enty_freq=open("ENTY_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofenty=enty.readlines()
for word in contentofvocab:
    word=word.replace("\n","")
    count=0
    for line in contentofenty:
        x=line.split()
        for i in x:
            if word == i:                 
                count=count+1
    prob=(count+1)/(ENTY_lines+Questions_train_lines)
    enty_freq.write(word+",%d"%count+",%f"%prob)
    enty_freq.write("\n")
vocabulary.close()
enty.close()
enty_freq.close()

vocabulary=open("vocabulary.txt","r")
abbr=open("ABBR1.txt","r")
abbr_freq=open("ABBR_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofabbr=abbr.readlines()
for word in contentofvocab:
    word=word.replace("\n","")
    count=0
    for line in contentofabbr:
        x=line.split()
        for i in x:
            if word == i:                 
                count=count+1
    prob=(count+1)/(ABBR_lines+Questions_train_lines)
    abbr_freq.write(word+",%d"%count+",%f"%prob)
    abbr_freq.write("\n")
vocabulary.close()
abbr.close()
abbr_freq.close()

vocabulary=open("vocabulary.txt","r")
hum=open("HUM1.txt","r")
hum_freq=open("HUM_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofhum=hum.readlines()
for word in contentofvocab:
    word=word.replace("\n","")
    count=0
    for line in contentofhum:
        x=line.split()
        for i in x:            
            if word == i:                 
                count=count+1
    prob=(count+1)/(HUM_lines+Questions_train_lines)
    hum_freq.write(word+",%d"%count+",%f"%prob)
    hum_freq.write("\n")
vocabulary.close()
hum.close()
hum_freq.close()

vocabulary=open("vocabulary.txt","r")
num=open("NUM1.txt","r")
num_freq=open("NUM_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofnum=num.readlines()
for word in contentofvocab:
    word=word.replace("\n","")
    count=0
    for line in contentofnum:
        x=line.split()
        for i in x:            
            if word == i:                 
                count=count+1
    prob=(count+1)/(NUM_lines+Questions_train_lines)
    num_freq.write(word+",%d"%count+",%f"%prob)
    num_freq.write("\n")
vocabulary.close()
num.close()
num_freq.close()

vocabulary=open("vocabulary.txt","r")
loc=open("LOC1.txt","r")
loc_freq=open("LOC_FREQ.txt","w")
contentofvocab=vocabulary.readlines()
contentofloc=loc.readlines()
for word in contentofvocab:
    word=word.replace("\n","")
    count=0
    for line in contentofloc:
        x=line.split()
        for i in x:            
            if word == i:                 
                count=count+1
    prob=(count+1)/(LOC_lines+Questions_train_lines)
    loc_freq.write(word+",%d"%count+",%f"%prob)
    loc_freq.write("\n")
vocabulary.close()
loc.close()
loc_freq.close()



#testing starts

#probalility of each class
Questions_train_lines = sum(1 for line in open('Questions_train.txt'))
DESC_lines = sum(1 for line in open('DESC.txt'))
ABBR_lines = sum(1 for line in open('ABBR.txt'))
HUM_lines = sum(1 for line in open('HUM.txt'))
NUM_lines = sum(1 for line in open('NUM.txt'))
LOC_lines = sum(1 for line in open('LOC.txt'))
ENTY_lines = sum(1 for line in open('ENTY.txt'))

Prob_DESC=DESC_lines/Questions_train_lines
Prob_ABBR=ABBR_lines/Questions_train_lines
Prob_HUM=HUM_lines/Questions_train_lines
Prob_NUM=NUM_lines/Questions_train_lines
Prob_LOC=LOC_lines/Questions_train_lines
Prob_ENTY=ENTY_lines/Questions_train_lines

prob=open("ProbOfClass.txt","w")
prob.write("DESC,%f"%Prob_DESC+"\n"+"ABBR,%f"%Prob_ABBR+"\n"+"HUM,%f"%Prob_HUM+"\n"+"NUM,%f"%Prob_NUM+"\n"+"ENTY,%f"%Prob_ENTY+"\n"+"LOC,%f"%Prob_LOC)
prob.close()


#cleaning the test file
test=open("Questions_test.txt","r")
test1=open("Questions_test1.txt","w")
content=test.readlines()
import re
for i in content:
    line = i.lower()
    line=re.sub('[^a-z]', ' ',line)
    line=line.split()
    line = ' '.join(line)
    test1.write(line)
    test1.write("\n")
test1.close()
test.close()

#Desired Output
test=open("Questions_test.txt","r")
dependent=open("Actual.txt","w")
x=test.readlines()
for i in x:
    word=i.split(":")
    dependent.write(word[0]+"\n")
test.close()
dependent.close()

#Predicted Output
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


#creating confusion matrix and finding accuracy
from sklearn.metrics import confusion_matrix


with open('Actual.txt', 'r') as infile:
    true_values = [i for i in infile]
with open('Predicted.txt', 'r') as infile:
    predictions = [i for i in infile]


confusion = confusion_matrix(true_values, predictions)

print(confusion)
tot=0
for i in confusion:
    for j in i:
        tot=tot+j
match=confusion[0][0]+confusion[1][1]+confusion[2][2]+confusion[3][3]+confusion[4][4]+confusion[5][5]
accuracy=match/tot *100
print (accuracy)   