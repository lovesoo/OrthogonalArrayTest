# encoding: utf-8

"""
@version:python 2.7
@author: weili8
@contact: weili8@iflytek.com
@file: test.py
@time: 2017/7/14 16:22
"""

from OAT import *
import json

if __name__ == "__main__":
    oat=OAT()
    case1= OrderedDict( [ ('K1', [ 0,1]),
                           ('K2', [ 0,1 ]),
                           ('K3', [ 0,1])])

    case2=OrderedDict([('A',['A1','A2','A3']),
                   ('B',['B1','B2','B3','B4']),
                   ('C',['C1','C2','C3']),
                   ('D',['D1','D2'])])

    case3=OrderedDict([(u'对比度',[u'正常',u'极低',u'低',u'高',u'极高']),
                      (u'色彩效果',[u'无',u'黑白',u'棕褐色',u'负片',u'水绿色']),
                      (u'感光度',[u'自动',100,200,400,800]),
                      (u'白平衡',[u'自动',u'白炽光',u'日光',u'荧光',u'阴光']),
                      (u'照片大小',['5M','3M','2M','1M','VGA']),
                      (u'闪光模式',[u'开',u'关'])])

    print json.dumps(oat.genSets(case1))
    print json.dumps( oat.genSets( case2 ) )
    print json.dumps( oat.genSets( case3) )
