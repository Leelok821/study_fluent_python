# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""

# 推导式
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]

# map filter函数组合

codes2 = filter(lambda c: c > 127, map(ord, symbols))

print(codes, list(codes2))
