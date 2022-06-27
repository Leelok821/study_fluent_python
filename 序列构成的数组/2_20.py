# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

示例 2-20 一个浮点型数组的创建、存入文件和从文件读取的过程
"""
from random import random
from array import array

floats = array('d', (random() for i in range(10**7)))
floats3 = array('b', [i for i in range(10)])
print(floats[-1])
print(floats3)

# 将数组写入文件
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats2==floats)