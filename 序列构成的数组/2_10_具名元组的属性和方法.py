# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
del_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(del_data)
print(delhi._asdict())
