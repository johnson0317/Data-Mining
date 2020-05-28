import csv
from sklearn import tree, metrics, cluster
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
data = pd.read_csv(r'csv_file\lsa_csv\lsa_5features.csv')
data_cluster = pd.DataFrame(data)
arr_data = data_cluster.values
num_of_cluster = 4
kmeans_fit = KMeans(n_clusters = num_of_cluster, init = 'k-means++', n_init = 10).fit(arr_data)
cluster_label = kmeans_fit.labels_
with open('Cluster_result.csv', 'w', newline = '') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Cluster'])
    for lbl in cluster_label:
        writer.writerow([lbl])
silhouette_avg = metrics.silhouette_score(arr_data, cluster_label)
cluster_0 = 0
cluster_1 = 0
cluster_2 = 0
cluster_3 = 0
for i in cluster_label:
    if i == 0:
        cluster_0 += 1
    elif i == 1:
        cluster_1 += 1
    elif i == 2:
        cluster_2 += 1
    else:
        cluster_3 += 1
print('First cluster : ', cluster_0, '\nSecond cluster : ', cluster_1, '\nThird cluster : ', cluster_2, '\nForth cluster : ', cluster_3)
print('silhouette_avg : ', silhouette_avg)