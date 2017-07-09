#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import binaryheap as bh


class Test(unittest.TestCase):

    def test_add_one(self):
        binaryheap = bh.BinaryHeap()
        binaryheap.add_value(5)
        self.assertEquals([None, 5], binaryheap.array)
        self.assertEquals(1, binaryheap.size)

    def test_delete_max_one_value(self):
        binaryheap = bh.BinaryHeap()
        binaryheap.add_value(5)
        max_value = binaryheap.delete_max()
        self.assertEquals(5, max_value)

    def test_delete(self):
        binaryheap = bh.BinaryHeap()
        binaryheap.array = [None, 8, 7, 4, 6, 5, 2, 3]
        binaryheap.size = 7

        max_value = binaryheap.delete_max()
        self.assertEquals(8, max_value)
        self.assertEquals([None, 7, 6, 4, 3, 5, 2], binaryheap.array)

    def test_insert_max(self):
        binaryheap = bh.BinaryHeap()
        binaryheap.array = [None, 8, 7, 4, 6, 5, 1, 3]
        binaryheap.size = 7
        # TODO

    def test_insert_intermediary(self):
        binaryheap = bh.BinaryHeap()
        binaryheap.array = [None, 8, 7, 4, 6, 5, 1, 3]
        binaryheap.size = 7
        # TODO

