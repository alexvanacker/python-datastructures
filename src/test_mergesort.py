#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import unittest
import mergesort as ms


class Test(unittest.TestCase):

    def test_merge(self):

        result = ms.merge_sorted_arrays([2], [5])
        self.assertEquals([2, 5], result)

    def test_merge_2(self):
        array1 = [3, 5]
        array2 = [1, 4]
        result = ms.merge_sorted_arrays(array1, array2)
        self.assertEquals([1, 3, 4, 5], result)

    def test_sort_one_value(self):
        array = [4]
        result = ms.merge_sort(array)
        self.assertEquals(array, result)

    def test_sort_already_sorted(self):
        array = [1, 2]
        result = ms.merge_sort(array)
        self.assertEquals(array, result)

    def test_sort_simple_2_values(self):
        array = [2, 1]
        result = ms.merge_sort(array)
        self.assertEquals([1, 2], result)

    def test_sort_uneven(self):
        array = [11, 5, 3, 4, 1]
        result = ms.merge_sort(array)
        expected = [1, 3, 4, 5, 11]
        self.assertEquals(expected, result)

