# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:51:52 2017

@author: Kumar Shikhar Deep
"""

#creating confusion matrix
from sklearn.metrics import confusion_matrix


with open('Actual.txt', 'r') as infile:
    true_values = [i for i in infile]
with open('Predicted.txt', 'r') as infile:
    predictions = [i for i in infile]


confusion = confusion_matrix(true_values, predictions)

print(confusion)