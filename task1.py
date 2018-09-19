import xlrd
from utils import *

book = xlrd.open_workbook('GTD.xlsx')
sheet = book.sheet_by_name('Data')
header = sheet.row_values(0)

r, v = [], []
# 归一化
exl = normalization(sheet)
v = value(exl)
r = range(sheet.nrows)

data = [(v, r) for v, r in zip(v, r)][1:]  # 去掉第一行
raw_data = data  # 备用
data.sort()
data.reverse()

print('top10: ======================================================', file=open('task1.txt', 'w'))
for i in range(10):
    print('Top{}. {}'.format(i + 1, sheet.row_values(data[i][1])[0]), file=open('task1.txt', 'a'))
print('max(v): {}\nmin(v): {}'.format(max(v), min(v)), file=open('task1.txt', 'a'))


# 200108110012 5141   5140
# 200511180002 11702  11701
# 200901170021 22896  22895
# 201402110015 59673  59672
# 201405010071 63640  63639
# 201411070002 72624  72625
# 201412160041 74132  74131
# 201508010015 83769  83768
# 201705080012 107033 107032
def selected_cases(rows):
    for i in range(len(rows)):
        print(value(rows[i], sheet))


print('表格中数据的严重程度：')
# selected_cases([5140, 11701, 22895, 59672, 63639, 72625, 74131, 83768, 107032])
print('sorted cases:\n {}'.format(data), file=open('task1.txt', 'a'))
