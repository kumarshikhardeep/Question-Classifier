# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:30:43 2017

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