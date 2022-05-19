# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

codes2 = [ord(symbol) for symbol in symbols]

print(codes, codes2)
