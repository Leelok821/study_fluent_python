# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

如果你需要一个列表，列表里是 3 种不同尺寸的 T 恤衫，每个尺寸都有 2 个颜色，示例
2-4 用列表推导算出了这个列表，列表里有 6 种组合。
"""

colors = ['blue', 'red']
sizes = ['S', 'M', 'L']
shirts = [(x, y) for x in colors for y in sizes]
print(shirts)