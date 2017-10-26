# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:40:48 2017

@author: Kumar Shikhar Deep
"""

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
