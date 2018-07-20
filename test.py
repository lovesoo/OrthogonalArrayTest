# encoding: utf-8

from OAT import *
import json
import requests
from functools import partial
from nose.tools import *

"""
pip install requests
pip install nose
"""


class check_response():
    @staticmethod
    def check_result(response, params, expectNum=None):
        # 由于搜索结果存在模糊匹配的情况，这里简单处理只校验第一个返回结果的正确性
        if expectNum is not None:
            # 期望结果数目不为None时，只判断返回结果数目
            eq_(expectNum, len(response['subjects']), '{0}!={1}'.format(expectNum, len(response['subjects'])))
        else:
            if not response['subjects']:
                # 结果为空，直接返回失败
                assert False
            else:
                # 结果不为空，校验第一个结果
                subject = response['subjects'][0]
                # 先校验搜索条件tag
                if params.get('tag'):
                    for word in params['tag'].split(','):
                        genres = subject['genres']
                        ok_(word in genres, 'Check {0} failed!'.format(word))

                # 再校验搜索条件q
                elif params.get('q'):
                    # 依次判断片名，导演或演员中是否含有搜索词，任意一个含有则返回成功
                    for word in params['q'].split(','):
                        title = [subject['title']]
                        casts = [i['name'] for i in subject['casts']]
                        directors = [i['name'] for i in subject['directors']]
                        total = title + casts + directors
                        ok_(any(word.lower() in i.lower() for i in total),
                            'Check {0} failed!'.format(word))


class test_douban(object):
    """
    豆瓣搜索接口测试demo,文档地址 https://developers.douban.com/wiki/?title=movie_v2#search
    """

    def search(self, params, expectNum=None):
        url = 'https://api.douban.com/v2/movie/search'
        r = requests.get(url, params=params)
        print ('Search Params:\n', json.dumps(params, ensure_ascii=False))
        print ('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))
        code = r.json().get('code', 0)
        if code > 0:
            assert False, 'Invoke Error.Code:\t{0}'.format(code)
        else:
            # 校验搜索结果是否与搜索词匹配
            check_response.check_result(r.json(), params, expectNum)

    def test_q(self):
        # 校验搜索条件
        qs = [u'白夜追凶', u'大话西游', u'周星驰', u'张艺谋', u'周星驰,吴孟达', u'张艺谋,巩俐', u'周星驰,西游', u'白夜追凶,潘粤明']
        tags = [u'科幻', u'喜剧', u'动作', u'犯罪', u'科幻,喜剧', u'动作,犯罪']
        starts = [0, 10, 20]
        counts = [20, 10, 5]

        # 生成原始测试数据 （有序数组）
        cases = OrderedDict([('q', qs), ('tag', tags), ('start', starts), ('count', counts)])

        # 使用正交表裁剪生成测试集
        cases = OAT().genSets(cases, mode=1, num=0)

        # 执行测试用例
        for case in cases:
            f = partial(self.search, case)
            f.description = json.dumps(case, ensure_ascii=False)
            yield (f,)


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

    # 默认mode=0，宽松模式，只裁剪重复测试集（测试用例参数值可能为None）
    print (json.dumps(oat.genSets(case1)))
    print (json.dumps(oat.genSets(case2)))
    print (json.dumps(oat.genSets(case3), ensure_ascii=False))
    print (json.dumps(oat.genSets(case4)))

    # mode=1，严格模式，除裁剪重复测试集外，还裁剪含None测试集(num为允许None测试集最大数目)
    print (json.dumps(oat.genSets(case4, mode=1, num=0)))
    print (json.dumps(oat.genSets(case4, mode=1, num=1)))
    print (json.dumps(oat.genSets(case4, mode=1, num=2)))
    print (json.dumps(oat.genSets(case4, mode=1, num=3)))
