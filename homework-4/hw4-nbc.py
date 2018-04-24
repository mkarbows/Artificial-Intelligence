import numpy as np
import csv

np.genfromtxt('hw4-data.csv', delimiter=',')

print(np.genfromtxt('hw4-data.csv', delimiter=','))

data = np.genfromtxt('hw4-data.csv', delimiter=',', skip_header=1)
print('all', data)

xVals = np.genfromtxt('hw4-data.csv', delimiter=',', usecols=(0,1,2,3,4), skip_header=1)
print('X only', xVals)

yVals = np.genfromtxt('hw4-data.csv', delimiter=',', usecols=(5), skip_header=1)
print('Y only', yVals)

from sklearn.naive_bayes import BernoulliNB
bernNB = BernoulliNB()
bernNB.fit(xVals, yVals)
# put these in report:
#                   P(V| A=0, P=1, I=0, D=0, G=0)
print(bernNB.predict_proba([[ 1, 0, 0, 0, 0 ]]))
#                   P(V| A=0, P=1, I=1, D=1, G=0)
print(bernNB.predict_proba([[ 1, 0, 1, 1, 0 ]]))
#                   P(V| A=1, P=0, I=0, D=0, G=1)
print(bernNB.predict_proba([[ 0, 1, 0, 0, 1 ]]))
