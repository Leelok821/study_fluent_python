# -*- coding:utf-8 -*-

"""
# Author ：li zi hao

示例 2-17 在有序序列中用 bisect 查找某个元素的插入位置
"""
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

FMT = '{0} @ {1} {2}{0}'


def demo(bisect_fn):
    for neddle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, neddle)
        offset = position * ' | '
        print(FMT.format(neddle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
