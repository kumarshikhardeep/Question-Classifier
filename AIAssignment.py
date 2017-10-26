# -*- coding: utf-8 -*-

# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Questions.txt', sep = ':',names=['Class','Question'], error_bad_lines=False , encoding='latin-1')
dataset_test = pd.read_csv('Questions_test.txt', sep = ':',names=['Class','Question'], error_bad_lines=False , encoding='latin-1')

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
corpus1 = []
for i in range(0, 5452):
    ques1 = re.sub('[^a-zA-Z]', ' ', dataset['Question'][i])
    ques1 = ques1.lower()
    ques1 = ques1.split()
#    ps1 = PorterStemmer()
    ques1 = [word for word in ques1[1:] if not word in set(stopwords.words('english'))]
    ques1 = ' '.join(ques1)
    corpus1.append(ques1)
corpus2 = []
for i in range(0, 500):
    ques2 = re.sub('[^a-zA-Z]', ' ', dataset_test['Question'][i])
    ques2 = ques2.lower()
    ques2 = ques2.split()
#    ps2 = PorterStemmer()
    ques2 = [word for word in ques2[1:] if not word in set(stopwords.words('english'))]
    ques2 = ' '.join(ques2)
    corpus2.append(ques2)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv1 = CountVectorizer(analyzer='word', ngram_range=(1,3), max_features=1000 )
X_train = cv1.fit_transform(corpus1).toarray()
y_train = dataset.iloc[:, 0].values
cv2 = CountVectorizer()
X_test = cv1.fit_transform(corpus2).toarray()
y_test = dataset_test.iloc[:, 0].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
y_train = labelencoder.fit_transform(y_train)
#onehotencoder = OneHotEncoder(categorical_features = [6])
#y_train = onehotencoder.fit_transform(y_train).toarray()
y_test = labelencoder.fit_transform(y_test)
#onehotencoder = OneHotEncoder(categorical_features = [6])



# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)