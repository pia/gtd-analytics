from sklearn.cluster import AffinityPropagation
import xlrd
import numpy as np
from utils import *
import re
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

# #############################################################################
# Import data
book = xlrd.open_workbook('GTD.xlsx')
sheet = book.sheet_by_name('Data')
header = sheet.row_values(0)
unclaimed_cases = []
# year 2015-2016
for row in range(74731, 103286):
    if (sheet.row_values(row)[header.index('claimed')] == 0):
        unclaimed_cases.append(sheet.row_values(row))
filtered_unclaimed_cases = filter_by_year(2015, 2016)


# #############################################################################
# Compute Affinity Propagation
def ap():
    af = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)  # 分成的团伙/个人数

    print('Estimated number of clusters: {}'.format(n_clusters_), file=open('log.txt', 'a'))
    print(labels)
    # 不用算了
    np.savetxt('log.txt', labels, fmt='%d')


# 内存预警，需20GB左右
ap()

# #############################################################################
# Collect data

# load value in task1.txt
v = []
filtered_rows = []
for row in range(74731, 103286):
    if (sheet.row_values(row)[header.index('claimed')] == 0):
        filtered_rows.append(row)
        v.append(value(row, sheet))
# v = np.array(v).reshape(-1, 1)

# load tag in log.txt
tag = []
with open('log_new.txt', 'r') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        tag.append(float(line))

dict = {}
danger_tag = {}
i = 0
for key in tag:
    dict[key] = dict.get(key, 0) + 1
    danger_tag[key] = danger_tag.get(key, 0) + v[i]
    i = i + 1


def sort_by_value(d):
    items = d.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort()
    backitems.reverse()
    return [backitems[i][1] for i in range(0, len(backitems))]


danger = {}
for t in range(int(max(tag) + 1)):
    danger[t] = dict[t] * 0.5 + danger_tag[t]

sorted_danger = sort_by_value(danger)
print('Top 5 danger tag:\n{}'.format(sorted_danger[:5]))
