#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import unittest
import binarysearchtree as bst


class Test(unittest.TestCase):

    def test_put_simple_values(self):
        tree = bst.BinarySearchTree()
        tree.add_value(2, 'b')
        tree.add_value(1, "a")
        tree.add_value(3, 'c')

        rootNode = tree.rootNode
        self.assertEquals(3, rootNode.size())
        node2 = tree.get(2)
        self.assertEquals(node2, rootNode)
        node1 = tree.get(1)
        self.assertEquals(1, node1.size())
