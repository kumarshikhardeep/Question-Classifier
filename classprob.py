# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:46:03 2017

@author: Kumar Shikhar Deep
"""

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