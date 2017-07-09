#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import linkedlist as ll


class Test(unittest.TestCase):

    def test_add_one(self):

        linkedlist = ll.LinkedList()
        linkedlist.add_value(1)
        first = linkedlist.get_first()
        self.assertEquals(1, first.value)
        self.assertEquals(1, linkedlist.get_size())

    def test_add_multiple(self):

        linkedlist = ll.LinkedList()
        expected = [1, 12, 3, 45]
        for x in expected:
            linkedlist.add_value(x)

        result = linkedlist.get_all()
        self.assertEquals(4, linkedlist.get_size())
        self.assertEquals(expected, result)

    def test_delete_last(self):
        linkedlist = ll.LinkedList()
        initial = [1, 12, 3, 45]
        for x in initial:
            linkedlist.add_value(x)

        linkedlist.delete_value(45)
        self.assertEquals(3, linkedlist.get_size())
        self.assertEquals([1, 12, 3], linkedlist.get_all())

    def test_delete_first(self):
        linkedlist = ll.LinkedList()
        initial = [1, 12, 3, 45]
        for x in initial:
            linkedlist.add_value(x)

        linkedlist.delete_value(1)
        self.assertEquals(3, linkedlist.get_size())
        self.assertEquals([12, 3, 45], linkedlist.get_all())

    def test_delete_middle(self):
        linkedlist = ll.LinkedList()
        initial = [1, 12, 3, 45]
        for x in initial:
            linkedlist.add_value(x)

        linkedlist.delete_value(3)
        self.assertEquals(3, linkedlist.get_size())
        self.assertEquals([1, 12, 45], linkedlist.get_all())

    def test_delete_multiple_same_value(self):

        linkedlist = ll.LinkedList()
        initial = [1, 12, 3, 45, 3]
        for x in initial:
            linkedlist.add_value(x)

        linkedlist.delete_value(3)
        self.assertEquals(4, linkedlist.get_size())
        self.assertEquals([1, 12, 45, 3], linkedlist.get_all())

    def test_delete_dups(self):
        linkedlist = ll.LinkedList()
        initial = [1, 12, 3, 45, 3, 78, 90, 12, 3, 45]
        for x in initial:
            linkedlist.add_value(x)

        linkedlist.remove_duplicates_no_buffer()
        expected = [1, 12, 3, 45, 78, 90]
        self.assertEquals(expected, linkedlist.get_all())





