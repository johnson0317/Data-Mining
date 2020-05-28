import csv
from sklearn import tree
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import export_graphviz
import numpy as np
train = []
lable = []
test = []
with open(r'lsa_csv\lsa_1000featuresTraining.csv' , newline = '') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        temp = []
        for (k,v) in row.items():
            if k == 'NGCLASS':
                lable.append(float(row[k]))
            else:
                temp.append(float(row[k]))
        train.append(temp)
train_lsa = np.array(train)
with open(r'lsa_csv\lsa_1000featuresTesting.csv' , newline = '') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        temp = []
        for (k, v) in row.items():
            if k != 'NGCLASS':
                temp.append(float(row[k]))
        test.append(temp)
test_lsa = np.array(test)
train_X, test_X, train_y, test_y = train_test_split(train_lsa, lable, test_size = 0.2)
clf = tree.DecisionTreeClassifier(min_samples_split = 35, max_depth =7, min_samples_leaf = 25)
dtree = clf.fit(train_X, train_y)
scores = cross_val_score(dtree, train_X, train_y, cv = 10, scoring = 'accuracy')
test_predicted = dtree.predict(test_lsa)
with open('Classification_result.csv', 'w', newline = '') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Class'])
    for lbl in test_predicted:
        writer.writerow([int(lbl)])
mean_score = scores.mean()
class_0 = 0
class_1 = 0
class_2 = 0
class_3 = 0
for i in test_predicted:
    if i == 0:
        class_0 += 1
    elif i == 1:
        class_1 += 1
    elif i == 2:
        class_2 += 1
    else:
        class_3 += 1
print('First Class : ', class_0, '\nSecond Class : ', class_1, '\nThird Class : ', class_2, '\nFourth Class : ', class_3)
print('Validation Accuracy : ', mean_score)