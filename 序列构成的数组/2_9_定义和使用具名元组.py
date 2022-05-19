# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""


from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'Japan', 36.9333, (35.689722, 139.691667))

print(tokyo)
