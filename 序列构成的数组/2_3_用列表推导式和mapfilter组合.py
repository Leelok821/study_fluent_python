# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

用列表推导和 map/filter 组合来创建同样的表单
"""

# 推导式
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]

# map filter函数组合

codes2 = list(filter(lambda x: x > 127, map(ord, symbols)))
print(codes, codes2)
