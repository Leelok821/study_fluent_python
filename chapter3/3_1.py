# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""
import time

DIAL_CODES = [(86, 'China'),
              (91, 'India'),
              (1, 'United States'),
              (62, 'Indonesia'),
              (55, 'Brazil'),
              (92, 'Pakistan'),
              (880, 'Bangladesh'),
              (234, 'Nigeria'),
              (7, 'Russia'),
              (81, 'Japan'),
              ]
d1 = {number: name for number, name in DIAL_CODES}
d2 = {number: name for number, name in DIAL_CODES if number > 100}

print(d1.get(112121,'lee'))