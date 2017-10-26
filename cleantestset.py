# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:47:26 2017

@author: Kumar Shikhar Deep
"""

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