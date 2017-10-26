# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:38:01 2017

@author: Kumar Shikhar Deep
"""

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