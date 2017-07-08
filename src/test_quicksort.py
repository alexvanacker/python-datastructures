#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import unittest
import quicksort as qs


class Test(unittest.TestCase):

    def test_simple_sort(self):
        array = [2, 1]
        result = qs.simple_sort(array)
        expected = [1, 2]
        self.assertEquals(expected, result)

    def test_sort_1(self):
        array = [5, 3, 34, 3, 2, 5, 1, 24]
        result = qs.quicksort_simple(array)
        expected = [1, 2, 3, 3, 5, 5, 24, 34]
        self.assertEquals(expected, result)
