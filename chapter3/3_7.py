# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

示例 3-7 StrKeyDict0 在查询的时候把非字符串的键转换为字符串
"""


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict0([('2','two'),('4', 'four')])
    print(d[3])
