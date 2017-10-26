# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:48:18 2017

@author: Kumar Shikhar Deep
"""

#Desired Output
test=open("Questions_test.txt","r")
dependent=open("Actual.txt","w")
x=test.readlines()
for i in x:
    word=i.split(":")
    dependent.write(word[0]+"\n")
test.close()
dependent.close()