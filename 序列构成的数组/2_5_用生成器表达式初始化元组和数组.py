# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""
import array

symbols = '$¢£¥€¤'
t = tuple(ord(s) for s in symbols)
a = array.array('I',(ord(s) for s in symbols))

print(t, a)