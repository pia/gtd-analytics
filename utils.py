from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale


# 计算事件的严重程度
def value0(row, sheet):
    header = sheet.row_values(0)
    # 死亡人数  nkill      w1=0.2169
    # 受伤人数  nwound     w2=0.2899
    # 财产损失  property   w3=0.1826
    # 持续事件  extended   w4=0.1257
    # 国际     INT_ANY    w5=0.1849
    w1, w2, w3, w4, w5 = 0.2169, 0.2899, 0.1826, 0.1257, 0.1849
    c1, c2, c3, c4, c5 = header.index('nkill'), header.index('nwound'), header.index('property'), \
                         header.index('extended'), header.index('INT_ANY')

    a = sheet.row_values(row)[c1]
    b = sheet.row_values(row)[c2]
    c = sheet.row_values(row)[c3]
    d = sheet.row_values(row)[c4]
    e = sheet.row_values(row)[c5]
    if (isinstance(a, str)): a = 0
    if (isinstance(b, str)): b = 0
    if (isinstance(c, str)): c = 0
    if (isinstance(d, str)): d = 0
    if (isinstance(e, str)): e = 0

    result = w1 * a + w2 * b + w3 * c + w4 * d + w5 * e
    return result


def value(exl):
    # 死亡人数  nkill      w1=0.2169
    # 受伤人数  nwound     w2=0.2899
    # 财产损失  property   w3=0.1826
    # 持续事件  extended   w4=0.1257
    # 国际     INT_ANY    w5=0.1849
    # exl: norminalized data
    w = [0.2169, 0.2899, 0.1826, 0.1257, 0.1849]
    v = [0]
    for line in range(len(exl[0])):
        v_this = 0.0
        for p in range(len(exl)):
            v_this += v_this * w[p]
        v.append(v_this)
    return v


def normalization(sheet, columns=['nkill', 'nwound', 'property', 'extended', 'INT_ANY']):
    header = sheet.row_values(0)
    data = []
    t = []
    for i in range(len(columns)):
        each_property = columns[i]
        for line in range(1, sheet.nrows):
            unit = 0 if (isinstance(sheet.row_values(line)[header.index(each_property)], str)) else \
                sheet.row_values(line)[
                    header.index(each_property)]
            t.append(unit)
        t = scale(t)
        data.append(t)
        return data
