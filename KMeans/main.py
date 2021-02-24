import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv('Mall_Customers.csv')
X = data[["Age", "Annual Income"]]
# print(data.head())
diff = 1
j = 0
K = 3
Centroids = (X.sample(K))
plt.scatter(X["Age"], X["Annual Income"], c='blue')
plt.scatter(Centroids["Age"], Centroids["Annual Income"], c='red')
plt.xlabel('Age')
plt.ylabel('Annual Income (Thousands)')
plt.show()

while diff != 0:
    XD = X
    i = 1
    for index1, first_row in Centroids.iterrows():
        Distance = []
        for index2, second_row in XD.iterrows():
            d1 = (first_row["Age"] - second_row["Age"]) ** 2
            d2 = (first_row["Annual Income"] - second_row["Annual Income"]) ** 2
            d = np.sqrt(d1 + d2)
            Distance.append(d)
        X[i] = Distance
        i = i + 1

    Cluster = []
    for index, row in X.iterrows():
        min_dist = row[1]
        pos = 1
        for i in range(K):
            if row[i + 1] < min_dist:
                min_dist = row[i + 1]
                pos = i + 1
        Cluster.append(pos)
    X["Cluster"] = Cluster
    Centroids_new = X.groupby(["Cluster"]).mean()[["Annual Income", "Age"]]
    if j == 0:
        diff = 1
        j = j + 1
    else:
        diff = (Centroids_new['Annual Income'] - Centroids['Annual Income']).sum() + (Centroids_new['Age']
                                                                                      - Centroids['Age']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Annual Income", "Age"]]

    color = ['blue', 'green', 'yellow']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["Age"], data["Annual Income"], c=color[k])
    plt.scatter(Centroids["Age"], Centroids["Annual Income"], c='red')
    plt.xlabel('Age')
    plt.ylabel('Loan Amount (Thousands)')
    plt.show()
