# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""


def add(obj_a, obj_b):
    """
    >>> add(1,2)
    3
    >>> add(3,4)
    7

    :param obj_a:
    :param obj_b:
    :return:
    """
    return obj_a + obj_b


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
