# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""


from collections import namedtuple

City = namedtuple('City', 'name county population coordinate')
tokyo = City._make(('Tokyo', 'Japan', 1122231, (129.22, 23.22)))

print(tokyo._asdict())