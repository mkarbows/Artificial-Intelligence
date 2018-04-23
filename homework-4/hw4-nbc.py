import numpy as np
import csv

np.genfromtxt('hw4-data.csv', delimiter=',')

print(np.genfromtxt('hw4-data.csv', delimiter=','))

printed = np.genfromtxt('hw4-data.csv', delimiter=',', skip_header=1)
print('all', printed)

X = np.genfromtxt('hw4-data.csv', delimiter=',', usecols=(0,1,2,3,4), skip_header=1)
print('X only', X)

Y = np.genfromtxt('hw4-data.csv', delimiter=',', usecols=(5), skip_header=1)
print('Y only', Y)

from sklearn.naive_bayes import BernoulliNB
nbc = BernoulliNB()
nbc.fit(X, Y)
print(nbc.predict_proba([[1,0,0,0,0]]))
