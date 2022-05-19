# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""

colors = ['blue', 'red']
sizes = ['S', 'M', 'L']

for shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(shirt)