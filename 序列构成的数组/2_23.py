# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

示例2-23 使用双向队列
"""

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3) # 旋转
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11,22,33])
print(dq)
dq.extendleft([33,44,55])
print(dq)