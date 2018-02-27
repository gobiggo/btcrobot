# -*- coding: utf-8 -*-


class Array:
    """实现__getitem__，支持序列获取元素、Slice等特性"""

    def __init__(self, lst):
        self.__coll = lst

    def __repr__(self):
        """显示列表"""

        return '{!r}'.format(self.__coll)

    def __getitem__(self, key):
        """获取元素"""
        slice1, slice2 = key
        row1 = slice1.start
        row2 = slice1.stop
        col1 = slice2.start
        col2 = slice2.stop
        return [self.__coll[r][col1:col2] for r in range(row1, row2)]