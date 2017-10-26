# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:32:53 2017

@author: Kumar Shikhar Deep
"""

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
