import csv
from sklearn import tree
from sklearn import metrics
train = []
with open(r'lsa_csv\lsa_10featuresTraining.csv' , newline = '') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
       train.append(row)

clf = tree.DecisionTreeClassifier()
lbl_clf = clf.fit(train)