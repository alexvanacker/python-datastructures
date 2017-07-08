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

    def test_construction(self):
        tree = bst.BinarySearchTree()
        tree.add_value(2, 'b')
        tree.add_value(1, "a")
        tree.add_value(4, 'c')
        tree.add_value(3, 'd')
        tree.add_value(7, 'e')
        tree.add_value(5, 'f')
        tree.add_value(8, 'g')

        node4 = tree.get(4)
        self.assertEquals(7, node4.right.key)
        self.assertEquals(3, node4.left.key)

    def test_get_dont_exist(self):
        tree = bst.BinarySearchTree()
        tree.add_value(2, 'b')

        node = tree.get(1)
        self.assertIsNone(node)

    def test_min(self):
        tree = bst.BinarySearchTree()
        tree.add_value(2, 'b')
        tree.add_value(1, "a")
        tree.add_value(3, 'c')

        node = tree.min()
        self.assertEquals(1, node.key)

    def test_delete(self):
        tree = bst.BinarySearchTree()
        tree.add_value(2, 'b')
        tree.add_value(1, "a")
        tree.add_value(4, 'c')
        tree.add_value(3, 'd')
        tree.add_value(7, 'e')
        tree.add_value(5, 'f')
        tree.add_value(8, 'g')
        tree.print_tree()
        self.assertEquals(2, tree.rootNode.key)
        tree.delete(4)

        tree.print_tree()

        # Should be what replaced the node with key 4
        node5 = tree.get(5)
        self.assertEquals(3, node5.left.key)
        self.assertEquals(7, node5.right.key)







if __name__ == '__main__':
    unittest.main()
