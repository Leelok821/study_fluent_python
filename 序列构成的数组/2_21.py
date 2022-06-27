# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

示例 2-21 通过改变数组中的一个字节来更新数组里某个元素的值
"""
import array

number = array.array('h', [-2,-1,0,1,2])
memv = memoryview(number)
print(memv[-1],len(memv))

memv_oct = memv.cast('B')
print(memv_oct.tolist())


c = [-2,-1,0,1,2]
c.extend((1,2))
print(c)