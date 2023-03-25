# OrthogonalArrayTest
Use the orthogonal experiment method to design test cases and generate test sets. 

[中文版README](https://github.com/lovesoo/OrthogonalArrayTest/blob/master/README_CN.md)

### 1.Introduction
Orthogonal test method is a multi-factor and multi-level test method. It uses the orthogonal table to design the test, replaces the comprehensive test with a small number of tests, and selects from the comprehensive test according to the orthogonality of the orthogonal table. An appropriate amount of representative points are tested, and these representative points have the characteristics of "evenly dispersed, neat and comparable".

Use orthogonal experiment method to design test cases, the basic steps are as follows:

1. Extract the functional description of test requirements, determine the number of factors and levels
2. Determine the n value based on the number of factors and the number of levels
2. Select the appropriate orthogonal table
3. Map the values of the variables to the table according to the orthogonal table, and design the test case data set

Referring to the above steps, this article uses Python to implement the complete process of automatically designing test cases using orthogonal tables.

Supported Python 2.7 ~ 3.8.

### 2.Demo
Input case1, case2, case3, respectively calculate m (number of levels), k (number of factors), n (number of experiments), and then query to select the appropriate orthogonal table, crop and finally generate the relevant test set

```
# encoding: utf-8


from OAT import *
import json

if __name__ == "__main__":
    oat = OAT()
    case1 = OrderedDict([('K1', [0, 1]),
                         ('K2', [0, 1]),
                         ('K3', [0, 1])])

    case2 = OrderedDict([('A', ['A1', 'A2', 'A3']),
                         ('B', ['B1', 'B2', 'B3', 'B4']),
                         ('C', ['C1', 'C2', 'C3']),
                         ('D', ['D1', 'D2'])])

    case3 = OrderedDict([(u'对比度', [u'正常', u'极低', u'低', u'高', u'极高']),
                         (u'色彩效果', [u'无', u'黑白', u'棕褐色', u'负片', u'水绿色']),
                         (u'感光度', [u'自动', 100, 200, 400, 800]),
                         (u'白平衡', [u'自动', u'白炽光', u'日光', u'荧光', u'阴光']),
                         (u'照片大小', ['5M', '3M', '2M', '1M', 'VGA']),
                         (u'闪光模式', [u'开', u'关'])])

    case4 = OrderedDict([('A', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']),
                         ('B', ['B1']),
                         ('C', ['C1'])])

    print json.dumps(oat.genSets(case1))
    print json.dumps(oat.genSets(case2))
    print json.dumps(oat.genSets(case3), ensure_ascii=False)
    print json.dumps(oat.genSets(case4))
    print json.dumps(oat.genSets(case4, 1, 0))
    print json.dumps(oat.genSets(case4, 1, 1))
    print json.dumps(oat.genSets(case4, 1, 2))
    print json.dumps(oat.genSets(case4, 1, 3))

```

Run Result：

```
[{"K1": 0, "K2": 0, "K3": 0}, {"K1": 0, "K2": 1, "K3": 1}, {"K1": 1, "K2": 0, "K3": 1}, {"K1": 1, "K2": 1, "K3": 0}]
[{"A": "A1", "B": "B1", "C": "C1", "D": "D1"}, {"A": "A1", "B": "B2", "C": "C2", "D": "D2"}, {"A": "A1", "B": "B3", "C": "C3", "D": null}, {"A": "A1", "B": "B4", "C": null, "D": null}, {"A": "A2", "B": "B1", "C": "C2", "D": null}, {"A": "A2", "B": "B2", "C": "C1", "D": null}, {"A": "A2", "B": "B3", "C": null, "D": "D1"}, {"A": "A2", "B": "B4", "C": "C3", "D": "D2"}, {"A": "A3", "B": "B1", "C": "C3", "D": null}, {"A": "A3", "B": "B2", "C": null, "D": null}, {"A": "A3", "B": "B3", "C": "C1", "D": "D2"}, {"A": "A3", "B": "B4", "C": "C2", "D": "D1"}, {"A": null, "B": "B1", "C": null, "D": "D2"}, {"A": null, "B": "B2", "C": "C3", "D": "D1"}, {"A": null, "B": "B3", "C": "C2", "D": null}, {"A": null, "B": "B4", "C": "C1", "D": null}]
[{"对比度": "正常", "色彩效果": "无", "感光度": "自动", "白平衡": "自动", "照片大小": "5M", "闪光模式": "开"}, {"对比度": "正常", "色彩效果": "黑白", "感光度": 200, "白平衡": "荧光", "照片大小": "VGA", "闪光模式": "关"}, {"对比度": "正常", "色彩效果": "棕褐色", "感光度": 800, "白平衡": "白炽光", "照片大小": "1M", "闪光模式": null}, {"对比度": "正常", "色彩效果": "负片", "感光度": 100, "白平衡": "阴光", "照片大小": "2M", "闪光模式": null}, {"对比度": "正常", "色彩效果": "水绿色", "感光度": 400, "白平衡": "日光", "照片大小": "3M", "闪光模式": null}, {"对比度": "极低", "色彩效果": "无", "感光度": 800, "白平衡": "荧光", "照片大小": "2M", "闪光模式": null}, {"对比度": "极低", "色彩效果": "黑白", "感光度": 100, "白平衡": "白炽光", "照片大小": "3M", "闪光模式": "开"}, {"对比度": "极低", "色彩效果": "棕褐色", "感光度": 400, "白平衡": "阴光", "照片大小": "5M", "闪光模式": "关"}, {"对比度": "极低", "色彩效果": "负片", "感光度": "自动", "白平衡": "日光", "照片大小": "VGA", "闪光模式": null}, {"对比度": "极低", "色彩效果": "水绿色", "感光度": 200, "白平衡": "自动", "照片大小": "1M", "闪光模式": null}, {"对比度": "低", "色彩效果": "无", "感光度": 400, "白平衡": "白炽光", "照片大小": "VGA", "闪光模式": null}, {"对比度": "低", "色彩效果": "黑白", "感光度": "自动", "白平衡": "阴光", "照片大小": "1M", "闪光模式": null}, {"对比度": "低", "色彩效果": "棕褐色", "感光度": 200, "白平衡": "日光", "照片大小": "2M", "闪光模式": "开"}, {"对比度": "低", "色彩效果": "负片", "感光度": 800, "白平衡": "自动", "照片大小": "3M", "闪光模式": "关"}, {"对比度": "低", "色彩效果": "水绿色", "感光度": 100, "白平衡": "荧光", "照片大小": "5M", "闪光模式": null}, {"对比度": "高", "色彩效果": "无", "感光度": 200, "白平衡": "阴光", "照片大小": "3M", "闪光模式": null}, {"对比度": "高", "色彩效果": "黑白", "感光度": 800, "白平衡": "日光", "照片大小": "5M", "闪光模式": null}, {"对比度": "高", "色彩效果": "棕褐色", "感光度": 100, "白平衡": "自动", "照片大小": "VGA", "闪光模式": null}, {"对比度": "高", "色彩效果": "负片", "感光度": 400, "白平衡": "荧光", "照片大小": "1M", "闪光模式": "开"}, {"对比度": "高", "色彩效果": "水绿色", "感光度": "自动", "白平衡": "白炽光", "照片大小": "2M", "闪光模式": "关"}, {"对比度": "极高", "色彩效果": "无", "感光度": 100, "白平衡": "日光", "照片大小": "1M", "闪光模式": "关"}, {"对比度": "极高", "色彩效果": "黑白", "感光度": 400, "白平衡": "自动", "照片大小": "2M", "闪光模式": null}, {"对比度": "极高", "色彩效果": "棕褐色", "感光度": "自动", "白平衡": "荧光", "照片大小": "3M", "闪光模式": null}, {"对比度": "极高", "色彩效果": "负片", "感光度": 200, "白平衡": "白炽光", "照片大小": "5M", "闪光模式": null}, {"对比度": "极高", "色彩效果": "水绿色", "感光度": 800, "白平衡": "阴光", "照片大小": "VGA", "闪光模式": "开"}]
[{"A": "A1", "B": "B1", "C": "C1"}, {"A": "A1", "B": null, "C": null}, {"A": "A2", "B": "B1", "C": null}, {"A": "A2", "B": null, "C": null}, {"A": "A2", "B": null, "C": "C1"}, {"A": "A3", "B": "B1", "C": null}, {"A": "A3", "B": null, "C": "C1"}, {"A": "A3", "B": null, "C": null}, {"A": "A4", "B": "B1", "C": null}, {"A": "A4", "B": null, "C": null}, {"A": "A4", "B": null, "C": "C1"}, {"A": "A5", "B": "B1", "C": null}, {"A": "A5", "B": null, "C": null}, {"A": "A5", "B": null, "C": "C1"}, {"A": "A6", "B": "B1", "C": null}, {"A": "A6", "B": null, "C": null}, {"A": "A6", "B": null, "C": "C1"}, {"A": null, "B": "B1", "C": null}, {"A": null, "B": null, "C": null}, {"A": null, "B": null, "C": "C1"}]
[{"A": "A1", "B": "B1", "C": "C1"}]
[{"A": "A1", "B": "B1", "C": "C1"}, {"A": "A2", "B": "B1", "C": null}, {"A": "A2", "B": null, "C": "C1"}, {"A": "A3", "B": "B1", "C": null}, {"A": "A3", "B": null, "C": "C1"}, {"A": "A4", "B": "B1", "C": null}, {"A": "A4", "B": null, "C": "C1"}, {"A": "A5", "B": "B1", "C": null}, {"A": "A5", "B": null, "C": "C1"}, {"A": "A6", "B": "B1", "C": null}, {"A": "A6", "B": null, "C": "C1"}]
[{"A": "A1", "B": "B1", "C": "C1"}, {"A": "A1", "B": null, "C": null}, {"A": "A2", "B": "B1", "C": null}, {"A": "A2", "B": null, "C": null}, {"A": "A2", "B": null, "C": "C1"}, {"A": "A3", "B": "B1", "C": null}, {"A": "A3", "B": null, "C": "C1"}, {"A": "A3", "B": null, "C": null}, {"A": "A4", "B": "B1", "C": null}, {"A": "A4", "B": null, "C": null}, {"A": "A4", "B": null, "C": "C1"}, {"A": "A5", "B": "B1", "C": null}, {"A": "A5", "B": null, "C": null}, {"A": "A5", "B": null, "C": "C1"}, {"A": "A6", "B": "B1", "C": null}, {"A": "A6", "B": null, "C": null}, {"A": "A6", "B": null, "C": "C1"}, {"A": null, "B": "B1", "C": null}, {"A": null, "B": null, "C": "C1"}]
[{"A": "A1", "B": "B1", "C": "C1"}, {"A": "A1", "B": null, "C": null}, {"A": "A2", "B": "B1", "C": null}, {"A": "A2", "B": null, "C": null}, {"A": "A2", "B": null, "C": "C1"}, {"A": "A3", "B": "B1", "C": null}, {"A": "A3", "B": null, "C": "C1"}, {"A": "A3", "B": null, "C": null}, {"A": "A4", "B": "B1", "C": null}, {"A": "A4", "B": null, "C": null}, {"A": "A4", "B": null, "C": "C1"}, {"A": "A5", "B": "B1", "C": null}, {"A": "A5", "B": null, "C": null}, {"A": "A5", "B": null, "C": "C1"}, {"A": "A6", "B": "B1", "C": null}, {"A": "A6", "B": null, "C": null}, {"A": "A6", "B": null, "C": "C1"}, {"A": null, "B": "B1", "C": null}, {"A": null, "B": null, "C": null}, {"A": null, "B": null, "C": "C1"}]

```

### 3.To-Do List
1. Decision table query logic optimization
2. Test case set tailoring and optimization

### 4.Reference
1. [https://wenku.baidu.com/view/a54724156edb6f1aff001f79.html](https://wenku.baidu.com/view/a54724156edb6f1aff001f79.html)
2. [http://www.york.ac.uk/depts/maths/tables/orthogonal.htm](http://www.york.ac.uk/depts/maths/tables/orthogonal.htm)
3. [http://support.sas.com/techsup/technote/ts723_Designs.txt](http://support.sas.com/techsup/technote/ts723_Designs.txt)
